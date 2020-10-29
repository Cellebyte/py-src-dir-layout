# py-src-dir-layout

I found that there is to less documentation around the src-dir layout for python packages.
So I started a small repository which just shows how to do it properly.

```txt
.
├── MANIFEST.in
├── README.md
├── setup.py
├── test.txt
├── .gitignore
├── src
│   └── rocket_science
│       ├── __init__.py
│       └── hello.py
└── tests
    ├── __init__.py     # this is not needed if you use a tooling like pytest it can be used to structure your tests
    └── test_hello.py
```

## Creating a VENV

Python supports venvs from its standard lib.

* [Venv](https://docs.python.org/3/library/venv.html)


```console
$ python3 -m venv <path_to_venv:.venv|.project_name> # Ensure that you don't use double symlinks here for the python executable
$ 
```

Check that you can activate the environment and it only shows the following.

```console
$ source .venv/bin/activate
(.venv) $ pip list
> Package    Version
> ---------- -------
> pip        x.y.z
> setuptools x.y.z
```
### Requirements

```console
$ pip install tox
> Installed tox version x.y.z
$ pip install pytest # optional if you want to run pytest from hand
> Installed pytest version x.y.z
```

## Running Pytest from hand

### With developer installation

```console
$ pip install -e .
> Obtaining file:///.rocket-science
> Installing collected packages: rocket-science
>   Running setup.py develop for rocket-science
> Successfully installed rocket-science
$ pytest -v
> ==================================== test session starts ====================================
> platform linux -- Python 3.8.6, pytest-6.1.2, py-1.9.0, pluggy-0.13.1 -- .venv/bin/python3.8
> cachedir: .pytest_cache
> rootdir: .
> collected 1 item
>
> tests/test_hello.py::test_say > PASSED   [100%]
>
> ===================================== 1 passed in 0.01s =====================================
```

### With just the repository

```console
$ PYTHONPATH=src pytest -v 
> ==================================== test session starts ====================================
> platform linux -- Python 3.8.6, pytest-6.1.2, py-1.9.0, pluggy-0.13.1 -- .venv/bin/python3.8
> cachedir: .pytest_cache
> rootdir: .
> collected 1 item
>
> tests/test_hello.py::test_say > PASSED   [100%]
>
> ===================================== 1 passed in 0.01s =====================================
```

## Running it with tox

```console
$ tox
> GLOB sdist-make: ./rocket-science/setup.py
> test inst-nodeps: .tox/.tmp/package/1/rocket-science-0.0.1.zip
> test installed: attrs==20.2.0,iniconfig==1.1.1,packaging==20.4,pluggy==0.13.1,py==1.9.0,pyparsing==2.4.7,pytest==6.1.2,rocket-science==0.0.1,six==1.15.0,toml==0.10.1
> test run-test-pre: PYTHONHASHSEED='218703068'
> test run-test: commands[0] | pytest -v
> ==================================== test session starts ====================================
> platform linux -- Python 3.8.6, pytest-6.1.2, py-1.9.0, pluggy-0.13.1 -- .venv/bin/python3.8
> cachedir: .pytest_cache
> rootdir: .
> collected 1 item
>
> tests/test_hello.py::test_say > PASSED   [100%]
>
> ===================================== 1 passed in 0.01s =====================================
```
### With developer installation

```ini
[tox]
envlist = test

[testenv:test]
deps = pytest
commands = pytest -v
```

### With just the repository

```ini
[tox]
skipdist = True ; only if you want to run again repository without installation
envlist = test

[testenv:test]
deps = pytest
setenv = PYTHONPATH=src ; only if you want to run again repository without installation
commands = pytest -v
```