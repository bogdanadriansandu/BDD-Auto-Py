py -m ...
pip install -U selenium
pip install behave
pip install behave-html-formatter

run test
behave -f html -o smoke.html --tags=smoke
behave -f html -o regression.html --tags=regression
behave -f html -o behave-report.html --tags=temp
