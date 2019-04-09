#!/usr/bin/env bash

echo "Hello! You are lunching SWAPI api tests"
echo "Will test People suite ONY"
echo "Report file will be generating after testrun completes"
echo "Starting ..."

# Delete old report file
if [ -f "People_test_report.html" ]
then
    rm People_test_report.html
fi
pip3 install virtualenv
python3 -m virtualenv env
source env/bin/activate

pip install -r requirements.txt
pytest tests/test_people.py -s -v --html=People_test_report.html