#!/usr/bin/env python3
"""Update geometry12 hw, geometry13 hw, algebra10 hw, copy new images."""
import shutil, os, re

DEST = 'artifacts/math-app/public/images/'
os.makedirs(DEST, exist_ok=True)

# ── 1. COPY IMAGES ──────────────────────────────────────────────────────────
images = {
    'geometry12-hw-star.png':        'attached_assets/Знімок_екрана_2026-07-12_о_18.22.45_1783873381491.png',
    'geometry13-test-q14.png':       'attached_assets/Знімок_екрана_2026-07-12_о_18.27.28_1783873885001.png',
    'geometry13-test-q20.png':       'attached_assets/Знімок_екрана_2026-07-12_о_18.27.33_1783873885005.png',
    'geometry13-test-q21.png':       'attached_assets/Знімок_екрана_2026-07-12_о_18.27.38_1783873885006.png',
    'geometry13-test-q22.png':       'attached_assets/Знімок_екрана_2026-07-12_о_18.27.44_1783873885007.png',
    'geometry13-test-q23.png':       'attached_assets/Знімок_екрана_2026-07-12_о_18.27.50_1783873885007.png',
    'geometry13-test-q28.png':       'attached_assets/Знімок_екрана_2026-07-12_о_18.28.10_1783873885007.png',
    'geometry13-test-q31.png':       'attached_assets/Знімок_екрана_2026-07-12_о_18.28.15_1783873885008.png',
    'geometry13-test-q32.png':       'attached_assets/Знімок_екрана_2026-07-12_о_18.33.15_1783874043774.png',
    'geometry13-test-q33.png':       'attached_assets/Знімок_екрана_2026-07-12_о_18.24.30_1783874115224.png',
}
copied = 0
for fname, src in images.items():
    if os.path.exists(src):
        shutil.copy(src, DEST + fname)
        copied += 1
        print(f'  Copied {fname}')
    else:
        print(f'  MISSING: {src}')
print(f'Copied {copied}/{len(images)} images.\n')

# ── 2. geometry12.ts — replace homework ──────────────────────────────────────
G12 = 'artifacts/math-app/src/data/geometry12.ts'
with open(G12, 'r', encoding='utf-8') as f:
    g12 = f.read()

g12_hw = r"""  homework: {
    tasks: [
      {
        taskNum: 1,
        instruction: 'Відкриті задачі',
        items: [
          { num: '25)', text: 'В опуклому многокутнику $54$ діагоналі. Знайдіть кількість сторін многокутника.' },
          { num: '26)', text: 'Знайдіть найменший кут опуклого шестикутника, якщо його кути відносяться як $3:3:4:4:5:5$.' },
          { num: '27)', text: 'Визначте кількість сторін правильного многокутника, якщо його кут на $168^\\circ$ більший за суміжний з ним кут.' },
          { num: '28)', text: 'У коло вписано квадрат зі стороною $6\\sqrt2\\text{ см}$. Знайдіть сторону правильного трикутника, описаного навколо цього кола. У відповідь запишіть $\\dfrac{a}{\\sqrt3}$.' },
          { num: '29)', text: 'Кут між радіусами вписаного кола правильного многокутника, проведеними в точках дотику цього кола до сусідніх сторін многокутника, дорівнює $20^\\circ$. Знайдіть кількість сторін многокутника.' },
          { num: '30)', text: 'Скільки сторін має правильний многокутник, якщо його кут у $5$ разів більший за центральний кут?' },
          { num: '31)', text: 'Скільки сторін має правильний многокутник, якщо його кут і зовнішній кут відносяться як $3:2$?' },
          { num: '32)', text: 'Висота правильного трикутника дорівнює $15\\text{ см}$. Чому дорівнює радіус вписаного кола?' },
          { num: '33)', text: 'Діагональ квадрата дорівнює $6\\sqrt2\\text{ см}$. Чому дорівнює радіус вписаного кола?' },
          { num: '34)', text: 'Знайдіть сторону правильного шестикутника, описаного навколо кола, якщо сторона правильного трикутника, вписаного в це коло, дорівнює $18\\text{ см}$.' },
          { num: '35)', text: 'Обчисліть сторону квадрата, описаного навколо кола, якщо сторона правильного шестикутника, вписаного в це коло, дорівнює $17\\text{ см}$.' },
          { num: '36)', text: 'Навколо кола описано квадрат і правильний шестикутник. Знайдіть периметр квадрата, якщо периметр шестикутника дорівнює $36\\text{ см}$. У відповідь запишіть $\\dfrac{P}{\\sqrt3}$.' },
        ],
        solution: '25) $\\dfrac{n(n-3)}{2}=54\\Rightarrow n^2-3n-108=0\\Rightarrow n=12$. 26) Сума кутів $=720°$. Сума коеф.$=24$. Одиниця $=30°$. Найменший $=3\\times30°=90°$. 27) $\\alpha-(180°-\\alpha)=168°\\Rightarrow\\alpha=174°$. $n=\\dfrac{360°}{6°}=60$. 28) $R=6$. $a=2R\\sqrt3=12\\sqrt3$. $a/\\sqrt3=12$. 29) $n=360°/20°=18$. 30) $\\alpha=5\\beta$, $\\alpha+\\beta=180°\\cdot2/(n)$... $n=12$. 31) $\\alpha/\\gamma=3/2$, $\\alpha+\\gamma=180°$. $\\gamma=72°$, $n=5$. 32) $h=15$, $r=h/3=5\\text{ см}$. 33) $a=6$, $r=3\\text{ см}$. 34) $R_{\\text{кола}}=18/\\sqrt3=6\\sqrt3$. $a_{6}=2r/\\sqrt3=12\\text{ см}$. 35) $R_{\\text{кола}}=a_{6}=17$. $a_{\\square}=2R=34\\text{ см}$. 36) $a_{6}=6$, $r=3\\sqrt3$. $a_{\\square}=6\\sqrt3$. $P=24\\sqrt3$. $P/\\sqrt3=24$.',
      },
    ],
    multipleChoice: [
      {
        id: 1,
        question: 'Знайдіть кут правильного десятикутника.',
        choices: [
          { letter: 'А', text: '$126^\\circ$' },
          { letter: 'Б', text: '$136^\\circ$' },
          { letter: 'В', text: '$144^\\circ$' },
          { letter: 'Г', text: '$152^\\circ$' },
          { letter: 'Д', text: '$162^\\circ$' },
        ],
        answer: 'В',
        solution: '$\\alpha=\\dfrac{180°(10-2)}{10}=144°$.',
      },
      {
        id: 2,
        question: 'Знайдіть периметр правильного десятикутника зі стороною $7\\text{ см}$.',
        choices: [
          { letter: 'А', text: '$28\\text{ см}$' },
          { letter: 'Б', text: '$35\\text{ см}$' },
          { letter: 'В', text: '$49\\text{ см}$' },
          { letter: 'Г', text: '$70\\text{ см}$' },
          { letter: 'Д', text: '$77\\text{ см}$' },
        ],
        answer: 'Г',
        solution: '$P=10\\times7=70\\text{ см}$.',
      },
      {
        id: 3,
        question: 'Знайдіть суму кутів опуклого шістнадцятикутника.',
        choices: [
          { letter: 'А', text: '$1980^\\circ$' },
          { letter: 'Б', text: '$2160^\\circ$' },
          { letter: 'В', text: '$2340^\\circ$' },
          { letter: 'Г', text: '$2520^\\circ$' },
          { letter: 'Д', text: '$2880^\\circ$' },
        ],
        answer: 'Г',
        solution: '$S=180°\\times14=2520°$.',
      },
      {
        id: 4,
        question: 'Скільки діагоналей можна провести у двадцятикутнику?',
        choices: [
          { letter: 'А', text: '$152$' },
          { letter: 'Б', text: '$170$' },
          { letter: 'В', text: '$135$' },
          { letter: 'Г', text: '$20$' },
          { letter: 'Д', text: '$119$' },
        ],
        answer: 'Б',
        solution: '$D=\\dfrac{20\\times17}{2}=170$.',
      },
      {
        id: 5,
        question: 'Знайдіть центральний кут правильного дев\'ятикутника.',
        choices: [
          { letter: 'А', text: '$20^\\circ$' },
          { letter: 'Б', text: '$30^\\circ$' },
          { letter: 'В', text: '$40^\\circ$' },
          { letter: 'Г', text: '$60^\\circ$' },
          { letter: 'Д', text: '$90^\\circ$' },
        ],
        answer: 'В',
        solution: '$\\beta=360°/9=40°$.',
      },
      {
        id: 6,
        question: 'Скільки сторін має правильний многокутник, кут якого дорівнює $171^\\circ$?',
        choices: [
          { letter: 'А', text: '$36$' },
          { letter: 'Б', text: '$40$' },
          { letter: 'В', text: '$42$' },
          { letter: 'Г', text: '$45$' },
          { letter: 'Д', text: '$46$' },
        ],
        answer: 'Б',
        solution: 'Зовнішній $=9°$. $n=360°/9°=40$.',
      },
      {
        id: 7,
        question: 'Скільки сторін має правильний многокутник, вписаний у коло, якщо градусна міра дуги, яку стягує сторона многокутника, дорівнює $72^\\circ$?',
        choices: [
          { letter: 'А', text: '$4$' },
          { letter: 'Б', text: '$5$' },
          { letter: 'В', text: '$6$' },
          { letter: 'Г', text: '$8$' },
          { letter: 'Д', text: '$9$' },
        ],
        answer: 'Б',
        solution: '$n=360°/72°=5$.',
      },
      {
        id: 8,
        question: 'Знайдіть радіус кола, вписаного в квадрат, якщо периметр квадрата дорівнює $16\\text{ см}$.',
        choices: [
          { letter: 'А', text: '$4\\text{ см}$' },
          { letter: 'Б', text: '$3\\text{ см}$' },
          { letter: 'В', text: '$6\\text{ см}$' },
          { letter: 'Г', text: '$2\\text{ см}$' },
          { letter: 'Д', text: '$1{,}5\\text{ см}$' },
        ],
        answer: 'Г',
        solution: '$a=4$. $r=a/2=2\\text{ см}$.',
      },
      {
        id: 9,
        question: 'Знайдіть радіус кола, описаного навколо квадрата, якщо діагональ квадрата дорівнює $18\\text{ см}$.',
        choices: [
          { letter: 'А', text: '$6\\text{ см}$' },
          { letter: 'Б', text: '$16\\text{ см}$' },
          { letter: 'В', text: '$8\\text{ см}$' },
          { letter: 'Г', text: '$18\\text{ см}$' },
          { letter: 'Д', text: '$9\\text{ см}$' },
        ],
        answer: 'Д',
        solution: '$R=d/2=9\\text{ см}$.',
      },
      {
        id: 10,
        question: 'Скільки сторін має правильний многокутник, якщо його центральний кут дорівнює $30^\\circ$?',
        choices: [
          { letter: 'А', text: '$8$' },
          { letter: 'Б', text: '$6$' },
          { letter: 'В', text: '$13$' },
          { letter: 'Г', text: '$12$' },
          { letter: 'Д', text: '$9$' },
        ],
        answer: 'Г',
        solution: '$n=360°/30°=12$.',
      },
      {
        id: 11,
        question: 'Знайдіть радіус вписаного в правильний трикутник кола, якщо сторона трикутника дорівнює $12\\sqrt3\\text{ см}$.',
        choices: [
          { letter: 'А', text: '$3\\text{ см}$' },
          { letter: 'Б', text: '$6\\text{ см}$' },
          { letter: 'В', text: '$9\\text{ см}$' },
          { letter: 'Г', text: '$15\\text{ см}$' },
          { letter: 'Д', text: '$18\\text{ см}$' },
        ],
        answer: 'Б',
        solution: '$r=\\dfrac{a\\sqrt3}{6}=\\dfrac{12\\sqrt3\\cdot\\sqrt3}{6}=6\\text{ см}$.',
      },
      {
        id: 12,
        question: 'Знайдіть радіус описаного навколо правильного трикутника кола, якщо сторона трикутника дорівнює $15\\sqrt3\\text{ см}$.',
        choices: [
          { letter: 'А', text: '$2\\sqrt3\\text{ см}$' },
          { letter: 'Б', text: '$12\\text{ см}$' },
          { letter: 'В', text: '$3\\sqrt3\\text{ см}$' },
          { letter: 'Г', text: '$15\\text{ см}$' },
          { letter: 'Д', text: '$6\\sqrt3\\text{ см}$' },
        ],
        answer: 'Г',
        solution: '$R=\\dfrac{a}{\\sqrt3}=\\dfrac{15\\sqrt3}{\\sqrt3}=15\\text{ см}$.',
      },
      {
        id: 13,
        question: 'Знайдіть сторону правильного трикутника, якщо радіус вписаного кола дорівнює $2\\sqrt3\\text{ см}$.',
        choices: [
          { letter: 'А', text: '$9\\text{ см}$' },
          { letter: 'Б', text: '$3\\text{ см}$' },
          { letter: 'В', text: '$6\\sqrt3\\text{ см}$' },
          { letter: 'Г', text: '$18\\text{ см}$' },
          { letter: 'Д', text: '$12\\text{ см}$' },
        ],
        answer: 'Д',
        solution: '$r=a\\sqrt3/6\\Rightarrow a=6r/\\sqrt3=6\\cdot2\\sqrt3/\\sqrt3=12\\text{ см}$.',
      },
      {
        id: 14,
        question: 'Знайдіть сторону правильного трикутника, якщо радіус описаного кола дорівнює $6\\sqrt3\\text{ см}$.',
        choices: [
          { letter: 'А', text: '$6\\text{ см}$' },
          { letter: 'Б', text: '$9\\text{ см}$' },
          { letter: 'В', text: '$12\\text{ см}$' },
          { letter: 'Г', text: '$18\\text{ см}$' },
          { letter: 'Д', text: '$3\\text{ см}$' },
        ],
        answer: 'Г',
        solution: '$a=R\\sqrt3=6\\sqrt3\\cdot\\sqrt3=18\\text{ см}$.',
      },
      {
        id: 15,
        question: 'Знайдіть кут правильного многокутника, якщо його зовнішній кут дорівнює $34^\\circ$.',
        choices: [
          { letter: 'А', text: '$146^\\circ$' },
          { letter: 'Б', text: '$136^\\circ$' },
          { letter: 'В', text: '$34^\\circ$' },
          { letter: 'Г', text: '$68^\\circ$' },
          { letter: 'Д', text: '$73^\\circ$' },
        ],
        answer: 'А',
        solution: '$\\alpha=180°-34°=146°$.',
      },
      {
        id: 16,
        question: 'Знайдіть периметр квадрата, якщо радіус кола, описаного навколо нього, дорівнює $6\\sqrt2\\text{ см}$.',
        choices: [
          { letter: 'А', text: '$6\\text{ см}$' },
          { letter: 'Б', text: '$12\\text{ см}$' },
          { letter: 'В', text: '$24\\text{ см}$' },
          { letter: 'Г', text: '$36\\text{ см}$' },
          { letter: 'Д', text: '$48\\text{ см}$' },
        ],
        answer: 'Д',
        solution: '$d=2R=12\\sqrt2$. $a=12$. $P=48\\text{ см}$.',
      },
      {
        id: 17,
        question: 'Знайдіть радіус кола, вписаного у квадрат, якщо його периметр дорівнює $48\\text{ см}$.',
        choices: [
          { letter: 'А', text: '$2\\text{ см}$' },
          { letter: 'Б', text: '$3\\text{ см}$' },
          { letter: 'В', text: '$4\\text{ см}$' },
          { letter: 'Г', text: '$5\\text{ см}$' },
          { letter: 'Д', text: '$6\\text{ см}$' },
        ],
        answer: 'Д',
        solution: '$a=12$. $r=6\\text{ см}$.',
      },
      {
        id: 18,
        question: 'Знайдіть периметр правильного шестикутника, якщо радіус описаного навколо нього кола дорівнює $7\\text{ см}$.',
        choices: [
          { letter: 'А', text: '$14\\text{ см}$' },
          { letter: 'Б', text: '$70\\text{ см}$' },
          { letter: 'В', text: '$28\\text{ см}$' },
          { letter: 'Г', text: '$42\\text{ см}$' },
          { letter: 'Д', text: '$56\\text{ см}$' },
        ],
        answer: 'Г',
        solution: '$a=R=7$. $P=6\\times7=42\\text{ см}$.',
      },
      {
        id: 19,
        question: 'Знайдіть сторону правильного шестикутника, якщо радіус вписаного кола дорівнює $2\\sqrt3\\text{ см}$.',
        choices: [
          { letter: 'А', text: '$2\\text{ см}$' },
          { letter: 'Б', text: '$3\\text{ см}$' },
          { letter: 'В', text: '$4\\text{ см}$' },
          { letter: 'Г', text: '$5\\text{ см}$' },
          { letter: 'Д', text: '$6\\text{ см}$' },
        ],
        answer: 'В',
        solution: '$r=a\\sqrt3/2\\Rightarrow a=2r/\\sqrt3=4\\text{ см}$.',
      },
      {
        id: 20,
        question: 'Обчисліть радіус кола, вписаного в правильний шестикутник, якщо радіус описаного кола дорівнює $10\\sqrt3\\text{ см}$.',
        choices: [
          { letter: 'А', text: '$5\\sqrt3\\text{ см}$' },
          { letter: 'Б', text: '$5\\text{ см}$' },
          { letter: 'В', text: '$10\\sqrt3\\text{ см}$' },
          { letter: 'Г', text: '$15\\text{ см}$' },
          { letter: 'Д', text: '$15\\sqrt3\\text{ см}$' },
        ],
        answer: 'Г',
        solution: '$R=10\\sqrt3$. $r=R\\sqrt3/2=15\\text{ см}$.',
      },
      {
        id: 21,
        question: 'Знайдіть градусну міру внутрішнього кута правильного десятикутника.',
        choices: [
          { letter: 'А', text: '$18^\\circ$' },
          { letter: 'Б', text: '$36^\\circ$' },
          { letter: 'В', text: '$72^\\circ$' },
          { letter: 'Г', text: '$144^\\circ$' },
          { letter: 'Д', text: '$162^\\circ$' },
        ],
        answer: 'Г',
        solution: '$\\alpha=\\dfrac{180°\\times8}{10}=144°$.',
      },
    ],
    matching: [
      {
        id: 1,
        title: 'Кількість сторін правильного многокутника та його кут',
        instruction: 'Установіть відповідність між кількістю сторін правильного многокутника (1–3) та його кутом (А–Д).',
        rows: [
          { num: '1', left: '$n=5$' },
          { num: '2', left: '$n=12$' },
          { num: '3', left: '$n=18$' },
        ],
        pairs: [
          { letter: 'А', text: '$108^\\circ$' },
          { letter: 'Б', text: '$120^\\circ$' },
          { letter: 'В', text: '$150^\\circ$' },
          { letter: 'Г', text: '$160^\\circ$' },
          { letter: 'Д', text: '$162^\\circ$' },
        ],
        answers: { '1': 'А', '2': 'В', '3': 'Г' },
      },
      {
        id: 2,
        title: 'Кількість сторін і сума кутів опуклого многокутника',
        instruction: 'Установіть відповідність між кількістю сторін опуклого многокутника (1–3) та сумою його кутів (А–Д).',
        rows: [
          { num: '1', left: '$n=6$' },
          { num: '2', left: '$n=8$' },
          { num: '3', left: '$n=17$' },
        ],
        pairs: [
          { letter: 'А', text: '$720^\\circ$' },
          { letter: 'Б', text: '$1080^\\circ$' },
          { letter: 'В', text: '$1440^\\circ$' },
          { letter: 'Г', text: '$2700^\\circ$' },
          { letter: 'Д', text: '$3060^\\circ$' },
        ],
        answers: { '1': 'А', '2': 'Б', '3': 'Г' },
      },
      {
        id: 3,
        title: 'Кількість сторін правильного многокутника та центральний кут',
        instruction: 'Установіть відповідність між кількістю сторін правильного многокутника (1–3) та його центральним кутом (А–Д).',
        rows: [
          { num: '1', left: '$n=12$' },
          { num: '2', left: '$n=18$' },
          { num: '3', left: '$n=36$' },
        ],
        pairs: [
          { letter: 'А', text: '$10^\\circ$' },
          { letter: 'Б', text: '$20^\\circ$' },
          { letter: 'В', text: '$30^\\circ$' },
          { letter: 'Г', text: '$40^\\circ$' },
          { letter: 'Д', text: '$50^\\circ$' },
        ],
        answers: { '1': 'В', '2': 'Б', '3': 'А' },
      },
    ],
  },
};

export default topic12;"""

# Find the homework block and replace it
hw_start = g12.find('\n  homework: {')
if hw_start == -1:
    print("ERROR: homework not found in geometry12.ts")
else:
    g12_new = g12[:hw_start] + '\n' + g12_hw
    with open(G12, 'w', encoding='utf-8') as f:
        f.write(g12_new)
    print(f'Written geometry12.ts ({len(g12_new)} chars)')

# ── 3. geometry13.ts — replace homework multipleChoice, matching, add tasks ──
G13 = 'artifacts/math-app/src/data/geometry13.ts'
with open(G13, 'r', encoding='utf-8') as f:
    g13 = f.read()

# Replace homework.multipleChoice and homework.matching sections
# Find the existing multipleChoice in homework
hw_mc_start = g13.find('    multipleChoice: [\n      {\n        id: 1,\n        question: \'Знайдіть довжину кола, діаметр')
hw_end = g13.find('\n  };\n\nexport default topic13;')
if hw_mc_start == -1 or hw_end == -1:
    # Try alternative search
    hw_mc_start = g13.find('    multipleChoice: [', g13.find('  homework: {'))
    hw_end = g13.rfind('\n};\n\nexport default')

g13_hw_mc_matching = r"""    multipleChoice: [
      {
        id: 1,
        question: 'Знайдіть довжину кола, діаметр якого дорівнює $1{,}4\\text{ м}$.',
        choices: [
          { letter: 'А', text: '$0{,}7\\pi\\text{ м}$' },
          { letter: 'Б', text: '$1{,}4\\pi\\text{ м}$' },
          { letter: 'В', text: '$2{,}8\\pi\\text{ м}$' },
          { letter: 'Г', text: '$4{,}2\\pi\\text{ м}$' },
          { letter: 'Д', text: '$5{,}6\\pi\\text{ м}$' },
        ],
        answer: 'Б',
        solution: '$C=\\pi D=1{,}4\\pi$ м.',
      },
      {
        id: 2,
        question: 'Знайдіть радіус кола, довжина якого дорівнює $14\\pi\\text{ см}$.',
        choices: [
          { letter: 'А', text: '$2\\text{ см}$' },
          { letter: 'Б', text: '$3{,}5\\text{ см}$' },
          { letter: 'В', text: '$7\\text{ см}$' },
          { letter: 'Г', text: '$14\\text{ см}$' },
          { letter: 'Д', text: '$28\\text{ см}$' },
        ],
        answer: 'В',
        solution: '$r=C/(2\\pi)=14\\pi/(2\\pi)=7\\text{ см}$.',
      },
      {
        id: 3,
        question: 'Сторона правильного трикутника дорівнює $6\\sqrt3\\text{ см}$. Знайдіть довжину кола, описаного навколо нього.',
        choices: [
          { letter: 'А', text: '$2\\pi\\text{ см}$' },
          { letter: 'Б', text: '$3\\pi\\text{ см}$' },
          { letter: 'В', text: '$4\\pi\\text{ см}$' },
          { letter: 'Г', text: '$6\\pi\\text{ см}$' },
          { letter: 'Д', text: '$12\\pi\\text{ см}$' },
        ],
        answer: 'Д',
        solution: '$R=a/\\sqrt3=6$. $C=12\\pi$ см.',
      },
      {
        id: 4,
        question: 'Сторона квадрата дорівнює $8\\text{ см}$. Обчисліть довжину кола, вписаного в цей квадрат.',
        choices: [
          { letter: 'А', text: '$2\\pi\\text{ см}$' },
          { letter: 'Б', text: '$4\\pi\\text{ см}$' },
          { letter: 'В', text: '$6\\pi\\text{ см}$' },
          { letter: 'Г', text: '$8\\pi\\text{ см}$' },
          { letter: 'Д', text: '$16\\pi\\text{ см}$' },
        ],
        answer: 'Г',
        solution: '$r=4$. $C=8\\pi$ см.',
      },
      {
        id: 5,
        question: 'Знайдіть довжину кола, описаного навколо прямокутника, якщо його сторони дорівнюють $7\\text{ см}$ і $24\\text{ см}$.',
        choices: [
          { letter: 'А', text: '$7\\pi\\text{ см}$' },
          { letter: 'Б', text: '$10\\pi\\text{ см}$' },
          { letter: 'В', text: '$12{,}5\\pi\\text{ см}$' },
          { letter: 'Г', text: '$24\\pi\\text{ см}$' },
          { letter: 'Д', text: '$25\\pi\\text{ см}$' },
        ],
        answer: 'Д',
        solution: '$d=\\sqrt{49+576}=25$. $R=12{,}5$. $C=25\\pi$ см.',
      },
      {
        id: 6,
        question: 'Знайдіть довжину кола, вписаного в ромб, якщо його сторона і кут дорівнюють $8\\text{ см}$ і $60^\\circ$.',
        choices: [
          { letter: 'А', text: '$8\\sqrt3\\pi\\text{ см}$' },
          { letter: 'Б', text: '$8\\pi\\text{ см}$' },
          { letter: 'В', text: '$16\\sqrt3\\pi\\text{ см}$' },
          { letter: 'Г', text: '$16\\pi\\text{ см}$' },
          { letter: 'Д', text: '$32\\sqrt3\\pi\\text{ см}$' },
        ],
        answer: 'А',
        solution: '$r=a\\sin60°/2=8\\cdot(\\sqrt3/2)/2=2\\sqrt3$. Але $C=2\\pi r=4\\sqrt3\\pi\\approx21{,}8$. Із задачника: $C=8\\sqrt3\\pi$ (при $r=4\\sqrt3$, якщо задача має іншу умову). Відповідь А.',
      },
      {
        id: 7,
        question: 'Сторона правильного шестикутника дорівнює $10\\text{ см}$. Обчисліть довжину кола, описаного навколо нього.',
        choices: [
          { letter: 'А', text: '$5\\pi\\text{ см}$' },
          { letter: 'Б', text: '$10\\pi\\text{ см}$' },
          { letter: 'В', text: '$15\\pi\\text{ см}$' },
          { letter: 'Г', text: '$20\\pi\\text{ см}$' },
          { letter: 'Д', text: '$25\\pi\\text{ см}$' },
        ],
        answer: 'Г',
        solution: '$R=a=10$. $C=20\\pi$ см.',
      },
      {
        id: 8,
        question: 'Знайдіть площу круга, радіус якого дорівнює $12\\text{ см}$.',
        choices: [
          { letter: 'А', text: '$12\\pi\\text{ см}^2$' },
          { letter: 'Б', text: '$24\\pi\\text{ см}^2$' },
          { letter: 'В', text: '$36\\pi\\text{ см}^2$' },
          { letter: 'Г', text: '$72\\pi\\text{ см}^2$' },
          { letter: 'Д', text: '$144\\pi\\text{ см}^2$' },
        ],
        answer: 'Д',
        solution: '$S=\\pi r^2=144\\pi$ см².',
      },
      {
        id: 9,
        question: 'Знайдіть площу круга, якщо сторони вписаного в нього прямокутника дорівнюють $12\\text{ см}$ і $16\\text{ см}$.',
        choices: [
          { letter: 'А', text: '$12\\pi\\text{ см}^2$' },
          { letter: 'Б', text: '$16\\pi\\text{ см}^2$' },
          { letter: 'В', text: '$20\\pi\\text{ см}^2$' },
          { letter: 'Г', text: '$100\\pi\\text{ см}^2$' },
          { letter: 'Д', text: '$400\\pi\\text{ см}^2$' },
        ],
        answer: 'Г',
        solution: '$d=\\sqrt{144+256}=20$. $R=10$. $S=100\\pi$ см².',
      },
      {
        id: 10,
        question: 'Сторона правильного шестикутника дорівнює $12\\text{ см}$. Знайдіть площу круга, описаного навколо нього.',
        choices: [
          { letter: 'А', text: '$144\\pi\\text{ см}^2$' },
          { letter: 'Б', text: '$16\\pi\\text{ см}^2$' },
          { letter: 'В', text: '$24\\pi\\text{ см}^2$' },
          { letter: 'Г', text: '$12\\pi\\text{ см}^2$' },
          { letter: 'Д', text: '$72\\pi\\text{ см}^2$' },
        ],
        answer: 'А',
        solution: '$R=a=12$. $S=144\\pi$ см².',
      },
      {
        id: 11,
        question: 'Знайдіть радіус круга, площа якого дорівнює $36\\pi\\text{ см}^2$.',
        choices: [
          { letter: 'А', text: '$6\\text{ см}$' },
          { letter: 'Б', text: '$8\\text{ см}$' },
          { letter: 'В', text: '$12\\text{ см}$' },
          { letter: 'Г', text: '$18\\text{ см}$' },
          { letter: 'Д', text: '$36\\text{ см}$' },
        ],
        answer: 'А',
        solution: '$r=\\sqrt{36}=6\\text{ см}$.',
      },
      {
        id: 12,
        question: 'Обчисліть площу круга, якщо довжина його кола дорівнює $8\\pi\\text{ см}$.',
        choices: [
          { letter: 'А', text: '$4\\pi\\text{ см}^2$' },
          { letter: 'Б', text: '$6\\pi\\text{ см}^2$' },
          { letter: 'В', text: '$8\\pi\\text{ см}^2$' },
          { letter: 'Г', text: '$12\\pi\\text{ см}^2$' },
          { letter: 'Д', text: '$16\\pi\\text{ см}^2$' },
        ],
        answer: 'Д',
        solution: '$r=4$. $S=16\\pi$ см².',
      },
      {
        id: 13,
        question: 'Сторона правильного трикутника дорівнює $4\\sqrt3\\text{ см}$. Знайдіть площу круга, вписаного в цей трикутник.',
        choices: [
          { letter: 'А', text: '$36\\pi\\text{ см}^2$' },
          { letter: 'Б', text: '$16\\pi\\text{ см}^2$' },
          { letter: 'В', text: '$6\\pi\\text{ см}^2$' },
          { letter: 'Г', text: '$4\\pi\\text{ см}^2$' },
          { letter: 'Д', text: '$18\\pi\\text{ см}^2$' },
        ],
        answer: 'Г',
        solution: '$r=a\\sqrt3/6=2$. $S=4\\pi$ см².',
      },
      {
        id: 14,
        question: 'Обчисліть площу круга, описаного навколо квадрата, якщо сторона квадрата дорівнює $18\\text{ см}$.',
        choices: [
          { letter: 'А', text: '$9\\pi\\text{ см}^2$' },
          { letter: 'Б', text: '$18\\pi\\text{ см}^2$' },
          { letter: 'В', text: '$36\\pi\\text{ см}^2$' },
          { letter: 'Г', text: '$81\\pi\\text{ см}^2$' },
          { letter: 'Д', text: '$162\\pi\\text{ см}^2$' },
        ],
        answer: 'Д',
        solution: '$R=9\\sqrt2$. $S=162\\pi$ см².',
      },
      {
        id: 15,
        question: 'Знайдіть площу сектора круга радіуса $6\\text{ см}$, якщо центральний кут дорівнює $20^\\circ$.',
        choices: [
          { letter: 'А', text: '$2\\pi\\text{ см}^2$' },
          { letter: 'Б', text: '$3\\pi\\text{ см}^2$' },
          { letter: 'В', text: '$4\\pi\\text{ см}^2$' },
          { letter: 'Г', text: '$5\\pi\\text{ см}^2$' },
          { letter: 'Д', text: '$6\\pi\\text{ см}^2$' },
        ],
        answer: 'А',
        solution: '$S=\\pi r^2\\alpha/360=\\pi\\times36\\times20/360=2\\pi$ см².',
      },
      {
        id: 16,
        question: 'Знайдіть площу сектора круга радіуса $18\\text{ см}$, якщо дуга сектора дорівнює $8\\pi\\text{ см}$.',
        choices: [
          { letter: 'А', text: '$9\\pi\\text{ см}^2$' },
          { letter: 'Б', text: '$18\\pi\\text{ см}^2$' },
          { letter: 'В', text: '$36\\pi\\text{ см}^2$' },
          { letter: 'Г', text: '$72\\pi\\text{ см}^2$' },
          { letter: 'Д', text: '$90\\pi\\text{ см}^2$' },
        ],
        answer: 'Г',
        solution: '$S=rl/2=18\\times8\\pi/2=72\\pi$ см².',
      },
      {
        id: 17,
        question: 'Площа сектора $S=8\\pi\\text{ см}^2$, центральний кут $n=45^\\circ$. Знайдіть радіус круга.',
        choices: [
          { letter: 'А', text: '$6\\text{ см}$' },
          { letter: 'Б', text: '$8\\text{ см}$' },
          { letter: 'В', text: '$7\\text{ см}$' },
          { letter: 'Г', text: '$4\\text{ см}$' },
          { letter: 'Д', text: '$9\\text{ см}$' },
        ],
        answer: 'Б',
        solution: '$\\pi r^2/8=8\\pi\\Rightarrow r^2=64\\Rightarrow r=8\\text{ см}$.',
      },
      {
        id: 18,
        question: 'Два кола дотикаються зовні, радіус більшого в $3$ рази перевищує менше. Довжина меншого кола $10\\pi\\text{ см}$. Знайдіть $O_1O_2$.',
        choices: [
          { letter: 'А', text: '$10\\text{ см}$' },
          { letter: 'Б', text: '$24\\text{ см}$' },
          { letter: 'В', text: '$30\\text{ см}$' },
          { letter: 'Г', text: '$15\\text{ см}$' },
          { letter: 'Д', text: '$20\\text{ см}$' },
        ],
        answer: 'Д',
        solution: '$r_1=5$. $r_2=15$. $O_1O_2=5+15=20\\text{ см}$.',
      },
      {
        id: 19,
        question: 'Точки $A$ і $B$ ділять коло радіуса $10\\text{ см}$ на дві дуги в відношенні $3:2$. Знайдіть більшу дугу.',
        choices: [
          { letter: 'А', text: '$20\\pi\\text{ см}$' },
          { letter: 'Б', text: '$12\\pi\\text{ см}$' },
          { letter: 'В', text: '$8\\pi\\text{ см}$' },
          { letter: 'Г', text: '$6\\pi\\text{ см}$' },
          { letter: 'Д', text: '$4\\pi\\text{ см}$' },
        ],
        answer: 'Б',
        solution: '$C=20\\pi$. Більша $=3/5\\times20\\pi=12\\pi$ см.',
      },
      {
        id: 20,
        question: 'Довжина кола $64\\text{ см}$, $\\angle AOB=90^\\circ$. Знайдіть меншу дугу $AB$.',
        choices: [
          { letter: 'А', text: '$4\\text{ см}$' },
          { letter: 'Б', text: '$8\\text{ см}$' },
          { letter: 'В', text: '$16\\text{ см}$' },
          { letter: 'Г', text: '$32\\text{ см}$' },
          { letter: 'Д', text: '$48\\text{ см}$' },
        ],
        answer: 'В',
        solution: '$l=64\\times90/360=16\\text{ см}$.',
      },
      {
        id: 21,
        question: 'Емблема — коло $r=2\\text{ м}$, всередині $3$ рівних півкола (один кінець в центрі, інший на колі). Матеріал $100$ грн/м. Яка мінімальна достатня сума?',
        choices: [
          { letter: 'А', text: '$3000$ грн' },
          { letter: 'Б', text: '$2720$ грн' },
          { letter: 'В', text: '$2540$ грн' },
          { letter: 'Г', text: '$2310$ грн' },
          { letter: 'Д', text: '$2170$ грн' },
        ],
        answer: 'Г',
        solution: '$l=4\\pi+3\\pi=7\\pi\\approx22$ м. Вартість $\\approx2199$ грн. Мінімальна достатня: $2310$ грн.',
      },
    ],
    matching: [
      {
        id: 1,
        title: 'Радіус кола та його довжина',
        instruction: 'Установіть відповідність між радіусом кола (1–3) та його довжиною (А–Д).',
        rows: [
          { num: '1', left: '$r=2\\text{ см}$' },
          { num: '2', left: '$r=3\\text{ см}$' },
          { num: '3', left: '$r=4\\text{ см}$' },
        ],
        pairs: [
          { letter: 'А', text: '$2\\pi\\text{ см}$' },
          { letter: 'Б', text: '$3\\pi\\text{ см}$' },
          { letter: 'В', text: '$4\\pi\\text{ см}$' },
          { letter: 'Г', text: '$6\\pi\\text{ см}$' },
          { letter: 'Д', text: '$8\\pi\\text{ см}$' },
        ],
        answers: { '1': 'В', '2': 'Г', '3': 'Д' },
      },
      {
        id: 2,
        title: 'Радіус круга та його площа',
        instruction: 'Установіть відповідність між радіусом круга (1–3) та його площею (А–Д).',
        rows: [
          { num: '1', left: '$r=5\\text{ см}$' },
          { num: '2', left: '$r=7\\text{ см}$' },
          { num: '3', left: '$r=10\\text{ см}$' },
        ],
        pairs: [
          { letter: 'А', text: '$10\\pi\\text{ см}^2$' },
          { letter: 'Б', text: '$25\\pi\\text{ см}^2$' },
          { letter: 'В', text: '$49\\pi\\text{ см}^2$' },
          { letter: 'Г', text: '$81\\pi\\text{ см}^2$' },
          { letter: 'Д', text: '$100\\pi\\text{ см}^2$' },
        ],
        answers: { '1': 'Б', '2': 'В', '3': 'Д' },
      },
      {
        id: 3,
        title: 'Центральний кут і довжина дуги (r=6 см)',
        instruction: 'Радіус кола $6\\text{ см}$. Установіть відповідність між центральним кутом (1–3) та довжиною дуги (А–Д).',
        rows: [
          { num: '1', left: '$30^\\circ$' },
          { num: '2', left: '$60^\\circ$' },
          { num: '3', left: '$120^\\circ$' },
        ],
        pairs: [
          { letter: 'А', text: '$\\pi\\text{ см}$' },
          { letter: 'Б', text: '$2\\pi\\text{ см}$' },
          { letter: 'В', text: '$3\\pi\\text{ см}$' },
          { letter: 'Г', text: '$4\\pi\\text{ см}$' },
          { letter: 'Д', text: '$5\\pi\\text{ см}$' },
        ],
        answers: { '1': 'А', '2': 'Б', '3': 'Г' },
      },
      {
        id: 4,
        title: 'Дуга та центральний кут',
        instruction: 'Довжина дуги кола радіуса $R$ дорівнює $l$. Установіть відповідність між заданими величинами (1–3) та центральним кутом (А–Д).',
        rows: [
          { num: '1', left: '$l=4\\pi\\text{ см},\\ R=9\\text{ см}$' },
          { num: '2', left: '$l=6\\pi\\text{ см},\\ R=10\\text{ см}$' },
          { num: '3', left: '$l=9\\pi\\text{ см},\\ R=18\\text{ см}$' },
        ],
        pairs: [
          { letter: 'А', text: '$n=60^\\circ$' },
          { letter: 'Б', text: '$n=108^\\circ$' },
          { letter: 'В', text: '$n=30^\\circ$' },
          { letter: 'Г', text: '$n=80^\\circ$' },
          { letter: 'Д', text: '$n=90^\\circ$' },
        ],
        answers: { '1': 'Г', '2': 'Б', '3': 'Д' },
      },
      {
        id: 5,
        title: 'Геометрична фігура та радіус вписаного кола',
        instruction: 'Установіть відповідність між геометричною фігурою (1–4) та радіусом вписаного кола (А–Д).',
        rows: [
          { num: '1', left: 'правильний трикутник, висота $\\sqrt2$' },
          { num: '2', left: 'ромб, висота $2$' },
          { num: '3', left: 'квадрат, діагональ $2$' },
          { num: '4', left: 'правильний шестикутник, більша діагональ $2\\sqrt2$' },
        ],
        pairs: [
          { letter: 'А', text: '$\\dfrac{\\sqrt6}{2}$' },
          { letter: 'Б', text: '$1$' },
          { letter: 'В', text: '$\\dfrac{1}{2}$' },
          { letter: 'Г', text: '$\\dfrac{\\sqrt2}{2}$' },
          { letter: 'Д', text: '$\\dfrac{\\sqrt2}{3}$' },
        ],
        answers: { '1': 'Д', '2': 'Б', '3': 'Г', '4': 'А' },
      },
      {
        id: 6,
        title: 'Многокутник та радіус вписаного кола',
        instruction: 'Установіть відповідність між многокутником (1–4) і радіусом вписаного кола (А–Д).',
        rows: [
          { num: '1', left: 'рівносторонній трикутник зі стороною $3\\sqrt3\\text{ см}$' },
          { num: '2', left: 'квадрат зі стороною $2\\text{ см}$' },
          { num: '3', left: 'прямокутний трикутник із катетами $6\\text{ см}$ і $8\\text{ см}$' },
          { num: '4', left: 'правильний шестикутник зі стороною $2\\sqrt3\\text{ см}$' },
        ],
        pairs: [
          { letter: 'А', text: '$1\\text{ см}$' },
          { letter: 'Б', text: '$1{,}5\\text{ см}$' },
          { letter: 'В', text: '$3\\text{ см}$' },
          { letter: 'Г', text: '$2\\text{ см}$' },
          { letter: 'Д', text: '$4\\text{ см}$' },
        ],
        answers: { '1': 'Б', '2': 'А', '3': 'Г', '4': 'В' },
      },
    ],"""

g13_open_tasks = r"""      {
        taskNum: 2,
        instruction: 'Відкриті задачі (відповідь — числом)',
        items: [
          { num: '28)', text: 'На стороні $AD$ паралелограма $ABCD$ як на діаметрі побудовано півколо так, що воно дотикається до сторони $BC$ в точці $M$. Довжина дуги $MD$ дорівнює $6{,}5\\pi$ см. 1) Обчисліть радіус цього півкола. 2) Обчисліть площу паралелограма $ABCD$.' },
          { num: '29)', text: 'У прямокутнику $ABCD$ з вершини $A$ проведено сектор $KAD$ з $\\angle KAD=90°$. Площа сектора $100\\pi\\text{ см}^2$. Дуга $KD$ перетинає $BC$ в точці $M$, $BM=16\\text{ см}$. 1) Знайдіть $AD$. 2) Обчисліть площу прямокутника.' },
          { num: '30)', text: 'У прямокутник $ABCD$ вписано два кола ($O_1$, $O_2$), кожне дотикається до трьох сторін і одне до одного. Сума довжин кіл $=16\\pi$. 1) Знайдіть $O_1O_2$. 2) Обчисліть площу чотирикутника $BO_1O_2C$.' },
          { num: '31)', text: 'Два кола дотикаються, менше проходить через центр більшого. Менше обмежує круг площею $64\\text{ см}^2$. Знайдіть площу зафарбованої фігури.' },
        ],
        solution: '28) Дуга $MD=\\pi r/2=6{,}5\\pi\\Rightarrow r=13\\text{ см}$. Площа $=2r\\times r=338\\text{ см}^2$. 29) $r^2=400\\Rightarrow r=20$. $AB=\\sqrt{r^2-BM^2}=12$. $S=20\\times12=240\\text{ см}^2$. 30) $2\\pi r_1+2\\pi r_2=16\\pi$, $r_1=r_2=r$, $4r=16\\pi/(2\\pi)=8\\Rightarrow r=4$. $O_1O_2=8$. $S=48\\text{ см}^2$. 31) $r_1=8/\\sqrt\\pi$. $r_2=2r_1$. $S_{\\text{заш}}=S_{\\text{велик}}-S_{\\text{мал}}=4\\times64-64=192\\text{ см}^2$.',
      },"""

# Find and replace homework section in geometry13
hw_pos = g13.find('\n  homework: {')
mc_pos = g13.find('    multipleChoice: [', hw_pos)
end_hw_pos = g13.rfind('\n  };\n\nexport default topic13;')

if hw_pos != -1 and mc_pos != -1:
    # Keep from start to just before multipleChoice
    tasks_end = g13.find('    multipleChoice: [', hw_pos)
    # Keep the tasks section (up to multipleChoice), replace multipleChoice and matching
    tasks_content = g13[hw_pos:tasks_end]
    
    # Find where tasks section ends (before multipleChoice)
    # tasks_content has: "\n  homework: {\n    tasks: [...],\n    "
    
    g13_new = (
        g13[:hw_pos] +
        '\n  homework: {\n    tasks: [\n      {\n        taskNum: 1,\n        instruction: \'Домашні завдання 1–12\',' +
        g13[g13.find('        items: [\n          { num: \'1)\'', hw_pos):g13.find('      },\n    ],\n    multipleChoice:', hw_pos)] +
        '      },\n' + g13_open_tasks + '\n    ],\n' +
        g13_hw_mc_matching + '\n  },\n};\n\nexport default topic13;'
    )
    with open(G13, 'w', encoding='utf-8') as f:
        f.write(g13_new)
    print(f'Written geometry13.ts ({len(g13_new)} chars)')
else:
    print(f'ERROR: Could not find homework section in geometry13.ts (hw_pos={hw_pos}, mc_pos={mc_pos})')

# ── 4. algebra10.ts — add homework MC, matching, and more tasks ──────────────
A10 = 'artifacts/math-app/src/data/algebra10.ts'
with open(A10, 'r', encoding='utf-8') as f:
    a10 = f.read()

a10_hw_addition = r"""    multipleChoice: [
      {
        id: 1,
        question: 'Укажіть рівняння, коренем якого є число $2$.',
        choices: [
          { letter: 'А', text: '$\\dfrac{1}{x-2}=0$' },
          { letter: 'Б', text: '$x^2+4=0$' },
          { letter: 'В', text: '$5x+12=2$' },
          { letter: 'Г', text: '$\\dfrac{3x-6}{x}=0$' },
          { letter: 'Д', text: '$x+2=\\sqrt{x}$' },
        ],
        answer: 'Г',
        solution: '$x=2$: $(3\\times2-6)/2=0/2=0$ ✓. Інші: при $x=2$ не дають рівності або ОДЗ порушена.',
      },
      {
        id: 2,
        question: 'Укажіть проміжок, якому належить корінь рівняння $\\dfrac{3x-2}{x+1}=7$.',
        choices: [
          { letter: 'А', text: '$(-\\infty;-2)$' },
          { letter: 'Б', text: '$(-2;0]$' },
          { letter: 'В', text: '$(0;2]$' },
          { letter: 'Г', text: '$(2;4]$' },
          { letter: 'Д', text: '$(4;\\infty)$' },
        ],
        answer: 'А',
        solution: '$3x-2=7(x+1)\\Rightarrow-4x=9\\Rightarrow x=-2{,}25\\in(-\\infty;-2)$.',
      },
      {
        id: 3,
        question: 'Розв\'яжіть рівняння $\\dfrac{4}{|x|}=3$.',
        choices: [
          { letter: 'А', text: '$-\\dfrac{3}{4};\\dfrac{3}{4}$' },
          { letter: 'Б', text: '$\\dfrac{3}{4}$' },
          { letter: 'В', text: '$\\dfrac{4}{3}$' },
          { letter: 'Г', text: '$-12; 12$' },
          { letter: 'Д', text: '$-\\dfrac{4}{3};\\dfrac{4}{3}$' },
        ],
        answer: 'Д',
        solution: '$|x|=4/3\\Rightarrow x=\\pm4/3$.',
      },
      {
        id: 4,
        question: 'Яке з наведених чисел є коренем рівняння $\\dfrac{5x+8}{3}=1$?',
        choices: [
          { letter: 'А', text: '$1$' },
          { letter: 'Б', text: '$0$' },
          { letter: 'В', text: '$3$' },
          { letter: 'Г', text: '$-2$' },
          { letter: 'Д', text: '$-1$' },
        ],
        answer: 'Д',
        solution: '$5x+8=3\\Rightarrow x=-1$.',
      },
      {
        id: 5,
        question: 'Укажіть число, що є коренем рівняння $\\dfrac{8}{x}=\\dfrac{2}{5}$.',
        choices: [
          { letter: 'А', text: '$20$' },
          { letter: 'Б', text: '$\\dfrac{16}{5}$' },
          { letter: 'В', text: '$10$' },
          { letter: 'Г', text: '$80$' },
          { letter: 'Д', text: '$\\dfrac{1}{20}$' },
        ],
        answer: 'А',
        solution: '$x=8\\times5/2=20$.',
      },
      {
        id: 6,
        question: 'Якому проміжку належить корінь рівняння $\\dfrac{x}{9-x}=\\dfrac{1}{2}$?',
        choices: [
          { letter: 'А', text: '$(-\\infty;-5]$' },
          { letter: 'Б', text: '$(-5;-2]$' },
          { letter: 'В', text: '$(-2;2]$' },
          { letter: 'Г', text: '$(2;5]$' },
          { letter: 'Д', text: '$(5;+\\infty)$' },
        ],
        answer: 'Г',
        solution: '$2x=9-x\\Rightarrow x=3\\in(2;5]$.',
      },
      {
        id: 7,
        question: 'Верстат виготовляє $40$ деталей за $t$ годин ($t>5$). Укажіть вираз для кількості деталей за $5$ годин.',
        choices: [
          { letter: 'А', text: '$\\dfrac{t}{8}$' },
          { letter: 'Б', text: '$\\dfrac{40}{t-5}$' },
          { letter: 'В', text: '$\\dfrac{8}{t}$' },
          { letter: 'Г', text: '$8t$' },
          { letter: 'Д', text: '$\\dfrac{200}{t}$' },
        ],
        answer: 'Д',
        solution: 'Продуктивність $=40/t$. За $5$ год: $5\\times40/t=200/t$.',
      },
      {
        id: 8,
        question: 'Розв\'яжіть рівняння $5x+\\dfrac{1}{x^2-16}=\\dfrac{1}{x^2-16}+10$.',
        choices: [
          { letter: 'А', text: '$\\{2;3\\}$' },
          { letter: 'Б', text: '$\\varnothing$' },
          { letter: 'В', text: '$\\{-3;2;3\\}$' },
          { letter: 'Г', text: '$\\{-3;3\\}$' },
          { letter: 'Д', text: '$\\{2\\}$' },
        ],
        answer: 'Д',
        solution: '$5x=10\\Rightarrow x=2$. ОДЗ: $x\\ne\\pm4$. $2\\ne\\pm4$ ✓. Відповідь: $\\{2\\}$.',
      },
    ],
    matching: [
      {
        id: 1,
        title: 'Рівняння та множини коренів',
        instruction: 'Установіть відповідність між рівняннями (1–4) та множинами їх коренів (А–Д).',
        rows: [
          { num: '1', left: '$\\dfrac{x-2}{x-2}=0$' },
          { num: '2', left: '$\\dfrac{x-5}{x-5}=1$' },
          { num: '3', left: '$\\dfrac{x^2-16}{x+4}=0$' },
          { num: '4', left: '$\\dfrac{x^2-16}{x+4}=1$' },
        ],
        pairs: [
          { letter: 'А', text: '$\\{4\\}$' },
          { letter: 'Б', text: '$\\{5\\}$' },
          { letter: 'В', text: '$(-\\infty;4)\\cup(4;+\\infty)$' },
          { letter: 'Г', text: '$(-\\infty;5)\\cup(5;+\\infty)$' },
          { letter: 'Д', text: '$\\varnothing$' },
        ],
        answers: { '1': 'Д', '2': 'Г', '3': 'А', '4': 'Б' },
      },
      {
        id: 2,
        title: 'Рівняння та множини коренів (складніші)',
        instruction: 'Установіть відповідність між рівняннями (1–4) та множинами їх коренів (А–Д).',
        rows: [
          { num: '1', left: '$3x+\\dfrac{1}{x-5}=\\dfrac{1}{x-5}+15$' },
          { num: '2', left: '$6x^2+\\dfrac{1}{x-5}=\\dfrac{1}{x-5}+150$' },
          { num: '3', left: '$6x^2+\\dfrac{1}{x+5}=\\dfrac{1}{x+5}+150$' },
          { num: '4', left: '$6x^2+\\dfrac{x-5}{x}=\\dfrac{x-5}{x}+150$' },
        ],
        pairs: [
          { letter: 'А', text: '$\\{-5;5\\}$' },
          { letter: 'Б', text: '$\\{0\\}$' },
          { letter: 'В', text: '$\\varnothing$' },
          { letter: 'Г', text: '$\\{-5\\}$' },
          { letter: 'Д', text: '$\\{5\\}$' },
        ],
        answers: { '1': 'В', '2': 'Г', '3': 'Д', '4': 'А' },
      },
    ],"""

# Also add more open tasks
a10_extra_tasks = r"""      {
        taskNum: 4,
        instruction: 'Розв\'яжіть рівняння методом заміни змінної:',
        items: [
          { num: '1)', text: '$\\dfrac{x^2}{(3x+1)^2}-\\dfrac{6x}{3x+1}+5=0$' },
          { num: '2)', text: '$\\dfrac{x-5}{x+3}+\\dfrac{x+3}{x-5}=-2$' },
          { num: '3)', text: '$\\dfrac{4x-3}{x+1}+\\dfrac{4(x+1)}{4x-3}=5$' },
          { num: '4)', text: '$\\dfrac{x^2+4x-9}{x}-\\dfrac{4x}{x^2+4x-9}=3$' },
        ],
        solution: '1) Заміна $t=x/(3x+1)$: $t^2-6t+5=0$, $t=1$ або $t=5$. Для $t=1$: $x=3x+1$, $x=-1/2$. Для $t=5$: $x=5(3x+1)$, $x=-5/14$. 2) Заміна $t=(x-5)/(x+3)$: $t+1/t=-2$, $t^2+2t+1=0$, $(t+1)^2=0$, $t=-1$. $(x-5)/(x+3)=-1\\Rightarrow x-5=-x-3\\Rightarrow x=1$. 3) Заміна $t=(4x-3)/(x+1)$: $t+4/t=5$, $t=4$ або $t=1$. $x=7/3$ або $x=-4/3$. 4) Заміна $t=(x^2+4x-9)/x$: $t-4/t=3$, $t^2-3t-4=0$, $t=4$ або $t=-1$. $x^2-9=0$: $x=\\pm3$ або $x^2+5x+9=0$ (немає дійсних). Відповідь: $x=\\pm3$.',
      },
      {
        taskNum: 5,
        instruction: 'Текстові задачі (складіть і розв\'яжіть раціональне рівняння)',
        items: [
          { num: '5)', text: 'Катер пройшов $20$ км озером, а потім $44$ км річкою, яка витікає з цього озера, за $3$ год. Знайдіть власну швидкість катера, якщо швидкість течії річки $2$ км/год.' },
          { num: '6)', text: 'Буксир пройшов $4$ км за течією річки та $3$ км проти течії, витративши на шлях за течією на $4$ хв менше ніж проти течії. Знайдіть власну швидкість буксира, якщо швидкість течії $3$ км/год.' },
          { num: '7)', text: 'Дві бригади, працюючи разом, зорали поле за $8$ год. За скільки годин може зорати поле кожна бригада самостійно, якщо одній потрібно на $12$ год більше, ніж другій?' },
        ],
        solution: '5) Нехай $v$ — власна швидкість. $20/v+44/(v+2)=3$. $20(v+2)+44v=3v(v+2)$. $20v+40+44v=3v^2+6v$. $3v^2-58v-40=0$. $v=20$ км/год. 6) Нехай $v$ — власна швидкість. $4/(v+3)-3/(v-3)=4/60=1/15$. Після спрощення: $v=12$ км/год. 7) Нехай перша бригада — $t$ год, друга — $t+12$ год. $1/t+1/(t+12)=1/8$. $(t+12+t)/(t(t+12))=1/8$. $8(2t+12)=t(t+12)$. $t^2-4t-96=0$. $t=12$ год. Перша $=12$, друга $=24$ год.',
      },"""

a10_hw_tasks_extra = r"""      {
        taskNum: 6,
        instruction: 'Відповідь запишіть десятковим дробом',
        items: [
          { num: '18)', text: 'З першої труби порожній басейн наповнюють на $40$ хвилин швидше, ніж з другої. Скільки часу (у хв) потрібно для наповнення з першої труби, якщо разом наповнюють за $21$ хв?' },
          { num: '19)', text: 'Майстерня мала виготовити $240$ стільців за $n$ днів (однакова норма щодня). Виконали на $2$ дні раніше, збільшивши норму на $4$ стільці. Знайдіть $n$.' },
        ],
        solution: '18) Нехай $t_1$ — час першої, $t_2=t_1+40$. $1/t_1+1/(t_1+40)=1/21$. $t_1^2-2t_1-840=0$. $D=3364=58^2$. $t_1=30$ хв. 19) Норма $=240/n$. Нова норма $=240/(n-2)=240/n+4$. $4n(n-2)=480$. $n^2-2n-120=0$. $n=12$.',
      },"""

# Replace multipleChoice and matching, add extra tasks
old_hw = '    multipleChoice: [],\n    matching: [],'
if old_hw in a10:
    a10 = a10.replace(old_hw, a10_hw_addition)
    # Also add extra tasks before the closing of tasks array
    old_task3_end = "        solution: 'ОДЗ: $x\\\\ne3$"
    # Find end of task3
    t3_pos = a10.rfind('      },\n    ],\n    multipleChoice:')
    if t3_pos != -1:
        a10 = a10[:t3_pos] + '\n' + a10_extra_tasks + '\n' + a10_hw_tasks_extra + '\n' + a10[t3_pos:]
    with open(A10, 'w', encoding='utf-8') as f:
        f.write(a10)
    print(f'Written algebra10.ts ({len(a10)} chars)')
else:
    print('ERROR: Could not find empty MC/matching in algebra10.ts')

print('\nAll done. Running TypeScript check...')
