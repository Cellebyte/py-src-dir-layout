# py-src-dir-layout

I found that there is to less documentation around the src-dir layout for python packages.
So I started a small repository which just shows how to do it properly.

```txt
.
├── poetry.lock
├── pyproject.toml
├── README.md
├── src
│   └── py_src_dir_layout
│       ├── hello.py
│       └── __init__.py
├── test_include.txt
├── tests
│   └── test_py_src_dir_layout
│       ├── __init__.py
│       └── test_hello.py
└── tox.ini
```

## Creating a VENV

Python supports venvs from its standard lib.

* [Venv](https://docs.python.org/3/library/venv.html)

if you don't want to use something like `poetry` you can go with a simple venv


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

[Poetry Documentation](https://python-poetry.org/docs/)
[Tox Documentation](https://tox.readthedocs.io/en/latest/)
[PyTest Documentation](https://docs.pytest.org/en/stable/contents.html)

```console
$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -
> Installed poetry version x.y.z
$ pip install tox # optional if you want to test with tox
> Installed tox version x.y.z
$ pip install pytest # optional if you want to run pytest from hand
> Installed pytest version x.y.z
```

## Running Pytest from hand

### With developer installation

```console
$ poetry install
> Installing dependencies from lock file
> 
> No dependencies to install or update
> 
>   - Installing py-src-dir-layout (0.1.0)
$ poetry run pytest
=============================================== test session starts ================================================
platform linux -- Python 3.9.1, pytest-6.2.1, py-1.10.0, pluggy-0.13.1
rootdir: /home/cellebyte/git/py-src-dir-layout
collected 1 item                                                                                                   

tests/test_py_src_dir_layout/test_hello.py .                                                                 [100%]

================================================ 1 passed in 0.05s =================================================
```

### With just the repository

```console
$ PYTHONPATH=src pytest
=============================================== test session starts ================================================
platform linux -- Python 3.9.1, pytest-6.2.1, py-1.10.0, pluggy-0.13.1
rootdir: /home/cellebyte/git/py-src-dir-layout
collected 1 item                                                                                                   

tests/test_py_src_dir_layout/test_hello.py .                                                                 [100%]

================================================ 1 passed in 0.05s =================================================
```

## Running it with tox

```console
$ tox # poetry run tox also works
> test inst-nodeps: /home/cellebyte/git/py-src-dir-layout/.tox/.tmp/package/1/py-src-dir-layout-0.1.0.tar.gz
> test installed: appdirs==1.4.4,attrs==20.3.0,black==20.8b1,click==7.1.2,distlib==0.3.1,filelock==3.0.12,flake8==3.8.4,iniconfig==1.1.1,mccabe==0.6.1,mypy==0.790,mypy-extensions==0.4.3,packaging==20.8,pathspec==0.8.1,pluggy==0.13.1,py==1.10.0,py-src-dir-layout @ file:///home/cellebyte/git/py-src-dir-layout/.tox/.tmp/package/1/py-src-dir-layout-0.1.0.tar.gz,pycodestyle==2.6.0,pyflakes==2.2.0,pyparsing==2.4.7,pytest==6.2.1,regex==2020.11.13,six==1.15.0,toml==0.10.2,tox==3.21.1,typed-ast==1.4.2,typing-extensions==3.7.4.3,virtualenv==20.3.1
> test run-test-pre: PYTHONHASHSEED='288829196'
> test run-test: commands[0] | pytest -v
> ============================================== test session starts ==============================================
> platform linux -- Python 3.9.1, pytest-6.2.1, py-1.10.0, pluggy-0.13.1 -- /home/cellebyte/git/py-src-dir-layout/.tox/test/bin/python
> cachedir: .tox/test/.pytest_cache
> rootdir: /home/cellebyte/git/py-src-dir-layout
> collected 1 item                                                                                                
> 
> tests/test_py_src_dir_layout/test_hello.py::test_say PASSED                                               [100%]
> 
> =============================================== 1 passed in 0.04s ===============================================
> pre-commit installed: appdirs==1.4.4,cfgv==3.2.0,distlib==0.3.1,filelock==3.0.12,identify==1.5.12,nodeenv==1.5.0,pre-commit==2.9.3,PyYAML==5.3.1,six==1.15.0,toml==0.10.2,virtualenv==20.3.1
> pre-commit run-test-pre: PYTHONHASHSEED='288829196'
> pre-commit run-test: commands[0] | pre-commit run --all-files --show-diff-on-failure
> black....................................................................Passed
> mypy.....................................................................Passed
> ____________________________________________________ summary ____________________________________________________
>   test: commands succeeded
>   pre-commit: commands succeeded
>   congratulations :)
```

## Linting and Formatting

For linting and formatting the packages `flake8`, `black` and `mypy` are installed.
To use them with VSCode use the following config in your project



```jsonc
{
  // "python.venvFolders": [
  // "~/.cache/pypoetry/virtualenvs"
  // ],
  "python.linting.enabled": true,
  "python.linting.flake8Enabled": true,
  "python.formatting.provider": "black",
  "python.linting.mypyEnabled": true,
  "python.linting.pylintEnabled": false,
}
```
