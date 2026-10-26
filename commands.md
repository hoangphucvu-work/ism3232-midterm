# Terminal Record: Copper Kettle Coffee Roasters

# 1. BUILDING THE PROJECT

'''cd ~Documents/ism3232/ism3232-midterm
python3 -m venv .venv 
source .venv/bin/activate
pip install pytest ruff 
pip freeze > requirements.txt
echo '.venv/' > .gitignore
echo '__pycache__/' >> .gitignore
touch main.py 
touch business_rules.py
mkdir -p tests && touch tests/__init__.py tests/test_business_rules.py'''

Github Connect:
'''echo "# ism3232-midterm" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/hoangphucvu-work/ism3232-midterm.git
git push -u origin main'''

for every git commit:
'''git add .
git commit -m "context of the commit"
git push -u origin main'''

# 2. THE VIRTUAL ENVIRONMENT
/Users/hoangphucvu.v2.0.m5pro/Documents/ism3232/ism3232-midterm/.venv/bin/python3

The private environment is a private "room". which python3 shows the system paths, in this case shows that venv is still activated.

# 3. THE PROJECT STRUCTURE
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

# 4. EVERY FUNCTION AND TEST

business_rules.py defines 8 functions and tests/test_business_rules.py defines 24 functions.

# 5. WHICH FILES PRINT
main.py is in the list, business_rules.py is not in the list because it does not have any print commands

# 6. THE COMMIT HISTORY
b85c13f (HEAD -> main, origin/main) ninth commit: commands.md last section is finished with 8 prior commits, comments are made in business_rules.py and tests/test_business_rules.py to provide context for other reader,so that the coder is easier to read, understand, and modify by other people
63ded09 eighth commit: after ruff format . && ruff check . && pytest -v: errors were found but fixed with ruff check --fix. Code runs smoothly with no bugs
f793f88 seventh commit: README.md done
0b73d45 sixth commit: first 5/6 sections of commands.md done
dda7868 fifth commit: test_business_rules.py: 24/24 tests passed; business_rules.py modified to reflect the correct discount percentage
5e41842 fourth commit: business_rules.py and main.py works well; output matched assignment
38cd515 third commit: all files set up
aef6fc8 second commit: requirements.txt and .gitignore set up
963f4ce first commit




