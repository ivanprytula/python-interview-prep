# Collection of handy commands, refs, examples
# https://ftp.gnu.org/old-gnu/Manuals/make-3.79.1/html_node/make_34.html
.PHONY: run clean

VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

#The variables can be overridden by providing the values when running the make command:
#make VENV=my_venv run

run: $(VENV)/bin/activate
	$(PYTHON) app.py

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

clean:
	rm -rf __pycache__
	rm -rf $(VENV)
