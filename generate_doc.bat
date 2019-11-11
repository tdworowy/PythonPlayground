set PYTHONPATH=%PYTHONPATH%;%cd%
sphinx-apidoc -o docs Playground
cd docs
xcopy *.rst source /i /y
make clean && make html