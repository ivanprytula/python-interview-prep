## Use flake8
The error code of flake8 are E***, W*** used in pep8 and F*** and C9**.

E***/W***: Error and warning of pep8
F***: Detection of PyFlakes
C9**: Detection of circulate complexity by McCabe


```shell
flake8 <file_name.py>
```

```python
# flake8: noqa
```

## Use black
```shell
black <file_name.py> --check

# -S, --skip-string-normalization: Don't normalize string quotes or prefixes.
black <file_name.py> -S

#  --diff Don't write the files back, just output a
#                                  diff for each file on stdout.
# --color / --no-color            Show colored diff. Only applies when
#                                  `--diff` is given.
black --diff --color main.py
# Format all files in dir
black .
```
https://naereen.github.io/badges/


## Use bandit

```shell
bandit -c pyproject.toml -r quiz/
```

## Use pytest
```shell
# run all tests
$ python -m pytest tests

# run tests in `chat` directory
$ python -m pytest tests/chat

# run only the quiz tests
$ python -m pytest tests/quiz/test_question_models.py

# run 2 tests concurrently
python -m pytest tests -n 2
```
