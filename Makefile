PYTHON = python
PIP = pip

run:
	$(PYTHON) src/__main__.py

install:
	$(PIP) install -r requirements.txt

# clean up Python bytecode files and __pycache__ directories
ifeq ($(OS),Windows_NT)
    RM = del /s /q
    RMDIR = for /d /r . %%d in (__pycache__) do if exist "%%d" rd /s /q "%%d"
else
    RM = rm -f
    RMDIR = find . -type d -name '__pycache__' -exec rm -r {} +
endif

clean:
	$(RM) *.pyc
	$(RMDIR)
###

.PHONY: run clean install