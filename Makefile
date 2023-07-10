VENV_NAME?=venv
PYTHON=${VENV_NAME}/bin/python3

venv:
	python3.11 -m venv ${VENV_NAME}

# activate venv manually in terminal, for some reason it doesn't work in makefile
# activate:
	# . ${VENV_NAME}/bin/activate

install:
	${PYTHON} -m pip install --upgrade pip
	${PYTHON} -m pip install -r requirements.txt

clean:
	rm -rf ${VENV_NAME}

.PHONY: venv install clean
