/* Math Tutor Service Worker */
const CACHE_VERSION = 'v1';
const STATIC_CACHE  = `mt-static-${CACHE_VERSION}`;
const PAGES_CACHE   = `mt-pages-${CACHE_VERSION}`;
const ASSETS_CACHE  = `mt-assets-${CACHE_VERSION}`;

const STATIC_ASSETS = [
  '/',
  '/offline.html',
  '/manifest.json',
];

/* ──────────────────────────────────────────── install */
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(STATIC_CACHE).then((cache) =>
      cache.addAll(STATIC_ASSETS)
    ).then(() => self.skipWaiting())
  );
});

/* ──────────────────────────────────────────── activate */
self.addEventListener('activate', (event) => {
  const VALID = [STATIC_CACHE, PAGES_CACHE, ASSETS_CACHE];
  event.waitUntil(
    caches.keys()
      .then((keys) =>
        Promise.all(keys.filter((k) => !VALID.includes(k)).map((k) => caches.delete(k)))
      )
      .then(() => self.clients.claim())
  );
});

/* ──────────────────────────────────────────── helpers */
function isApiRequest(url) {
  return url.pathname.startsWith('/api/') ||
         url.pathname.startsWith('/auth/') ||
         url.hostname !== self.location.hostname;
}

function isStaticAsset(url) {
  return /\.(js|css|woff2?|ttf|otf|eot|svg|png|jpg|jpeg|gif|ico|webp)(\?.*)?$/.test(url.pathname);
}

function isNavigationRequest(request) {
  return request.mode === 'navigate';
}

/* ──────────────────────────────────────────── fetch */
self.addEventListener('fetch', (event) => {
  const url = new URL(event.request.url);

  // Never cache API / auth / cross-origin requests
  if (isApiRequest(url)) return;

  // Static assets → Cache First
  if (isStaticAsset(url)) {
    event.respondWith(
      caches.open(ASSETS_CACHE).then(async (cache) => {
        const cached = await cache.match(event.request);
        if (cached) return cached;
        const response = await fetch(event.request);
        if (response.ok) cache.put(event.request, response.clone());
        return response;
      })
    );
    return;
  }

  // Navigation → Network First, cache success, fallback to offline
  if (isNavigationRequest(event.request)) {
    event.respondWith(
      fetch(event.request)
        .then((response) => {
          if (response.ok) {
            caches.open(PAGES_CACHE).then((cache) =>
              cache.put(event.request, response.clone())
            );
          }
          return response;
        })
        .catch(async () => {
          const cached = await caches.match(event.request, { ignoreSearch: true });
          // SPA fallback: serve cached index for any navigation
          const index = await caches.match('/');
          return cached || index || caches.match('/offline.html');
        })
    );
    return;
  }

  // Everything else → Network First, fallback to cache
  event.respondWith(
    fetch(event.request)
      .then((response) => {
        if (response.ok) {
          caches.open(PAGES_CACHE).then((cache) =>
            cache.put(event.request, response.clone())
          );
        }
        return response;
      })
      .catch(() => caches.match(event.request))
  );
});

/* ──────────────────────────────────────────── messages */
self.addEventListener('message', (event) => {
  if (event.data?.type === 'SKIP_WAITING') {
    self.skipWaiting();
  }
});
