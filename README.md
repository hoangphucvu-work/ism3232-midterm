# ISM3232 Midterm: Copper Kettle Coffee Roaster

- **Name:** Hoang Phuc Vu
- **Version:** 1.1
- **Date:** 10/25/2026

## What This Program Does
This program reports and calculates based on the input and the rules provided by the company. The calculations are: wholesale costs, discounts based on each customer's different situation, shipping fees; it reports orders requiring prepayments or freight pallets as well. At the end, the output of this program is a clear individual shipment report alongside statistics such as amount of events, total income, average shipment, largest shipment, number of prepayments required, and number of pallets needed.

## Business Rules
There are 6 business rules:
1. The bean cost is price per bag times number of bags. Each shipment is different.
2. There are discount available based on number of bags for each shipment: no discount for fewer than 20 bags, small discount of 9% for shipments of 20 to 79 bags, and big discount of 14% for shipments from 80 bags or more. 
3. Partner cafes get 13% for small discount and 18% for big discount with the same requirements of quantity. No discount for less than 20 bags though.
4. If the discounted cost is less than $250, a $35 shipping fee is added. Otherwise, the shipment gets free shipping.
5. A shipment whose total exceeds $1499.99, after discount and shipping fee applied, will requires prepayment.
6. A shipment will need a fright pallet if BOTH requirements are met: more than 60 bags and  shipment total is over $700.

## How to Run
'''cd ~Documents/ism3232/ism3232-midterm
python3 -m venv .venv 
source .venv/bin/activate
pip install pytest ruff 
pip freeze > requirements.txt
echo '.venv/' > .gitignore
echo '__pycache__/' >> .gitignore
touch main.py 
touch business_rules.py
mkdir -p tests && touch tests/__init__.py tests/test_business_rules.py
python3 main.py'''

## How to Test
'''ruff format .
ruff check .
pytest -v'''
24 tests written, all passed

## Files in This Repository
1. requirements.txt: The virtual environment is created and all the tools are installed

2. .gitignore: a text file telling Git what to ignore, prevents files from being accidentally leaked

3. README.md: information of the project

4. commands.md: lists of commands of the project

5. main.py: the main Python3 file, including 8 shipments and their details. Running this file will display the report and other statistics that have been mentioned prior.

6. business_rules.py: rules of the business, which are then applied to other files (main.py and tests/test_business_rules.py)

7. tests/test_business_rules.py: define tests to test back the business_rules.py, making sure that there is no error in the code

## AI Use Statement
I did not use AI for any part of the whole project. Everything is written, checked, debugged, and commited to GitHub by me and only me, with the help of the course site and my past labs. 

