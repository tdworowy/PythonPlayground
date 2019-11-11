set PYTHONPATH=%PYTHONPATH%;%cd%/Playground
sphinx-apidoc -o Doc Playground
cd Doc
xcopy *.rst source /i /y
make clean && make html