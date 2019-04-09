#!/usr/bin/env bash
echo "Hello! You are lunching SWAPI api tests"
echo "Will test all suites"
echo "Report file will be generating after testrun completes"
echo "Starting ..."


if [ -f "All_together_report.html" ]
then
    rm All_together_report.html
fi


pip3 install virtualenv
python3 -m virtualenv env
source env/bin/activate

pip install -r requirements.txt
pytest tests/ -s -v --html=All_together_report.html