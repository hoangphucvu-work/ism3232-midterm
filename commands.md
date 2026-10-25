# Terminal Record: Copper Kettle Coffee Roasters

1. BUILDING THE PROJECT

cd ~Documents/ism3232/ism3232-midterm
python3 -m venv .venv 
source .venv/bin/activate
pip install pytest ruff 
pip freeze > requirements.txt
echo '.venv/' > .gitignore
echo '__pycache__/' >> .gitignore
touch main.py 
touch business_rules.py
mkdir -p tests && touch tests/__init__.py tests/test_business_rules.py

Github Connect:
echo "# ism3232-midterm" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/hoangphucvu-work/ism3232-midterm.git
git push -u origin main

for every git commit:
git add .
git commit -m "context of the commit"
git push -u origin main

2. THE VIRTUAL ENVIRONMENT
/Users/hoangphucvu.v2.0.m5pro/Documents/ism3232/ism3232-midterm/.venv/bin/python3

The private environment is a private "room". which python3 shows the system paths, in this case shows that venv is still activated.

3. THE PROJECT STRUCTURE
├── README.md
├── __pycache__
│   └── business_rules.cpython-314.pyc
├── business_rules.py
├── commands.md
├── main.py
├── requirements.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    └── test_business_rules.py

4 directories, 8 files

__pycache__ is not in the Github repo, because it is added to .gitignore

4. EVERY FUNCTION AND TEST

business_rules.py defines 8 functions and tests/test_business_rules.py defines 24 functions.

5. WHICH FILES PRINT
main.py is in the list, business_rules.py is not in the list because it does not have any print commands

6. THE COMMIT HISTORY



