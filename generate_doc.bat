set PYTHONPATH=%PYTHONPATH%;%cd%/Playground
sphinx-apidoc -o docs Playground
cd docs
xcopy *.rst source /i /y
make clean && make html