#!/usr/bin/env bash
echo "Hello! You are lunching SWAPI api tests"
echo "Will test Films suite ONY"
echo "Report file will be generating after testrun completes"
echo "Starting ..."

# Delete old report file

if [ -f "Films_test_report.html" ]
then
    rm Films_test_report.html
fi
pip3 install virtualenv
python3 -m virtualenv env
source env/bin/activate

pip install -r requirements.txt
pytest tests/test_films.py -s -v --html=Films_test_report.html