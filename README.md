# DevOps: CLI-інструменти на Python

Три підходи до створення CLI: `sys.argv`, `click` та `fire`.

## Встановлення

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Структура

```
src/
├── __init__.py
├── sys_tool.py      # 1) прямий запуск + sys.argv
├── click_tool.py    # 2) утиліта на click
├── utils.py         # функції greet / goodbye
└── fire_expose.py   # 3) експорт utils через fire
```

## 1. sys_tool.py

Друкує «командна строка» лише при прямому запуску.

```bash
python src/sys_tool.py
# командна строка

python src/sys_tool.py --help
# Використання: python src/sys_tool.py [--help] ...

python -c "import src.sys_tool"
# (нічого не друкує)
```

## 2. click_tool.py

```bash
python src/click_tool.py say --name Alice
# Alice

python src/click_tool.py say --name peter
# Ім'я не підходить

python src/click_tool.py --help
python src/click_tool.py say --help
```

## 3. fire_expose.py

```bash
python src/fire_expose.py greet Alice
# Привіт, Alice!

python src/fire_expose.py goodbye Bob
# До побачення, Bob!

python src/fire_expose.py -- --help
python src/fire_expose.py greet --help
```
