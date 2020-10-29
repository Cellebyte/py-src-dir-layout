# py-src-dir-layout

I found out that there is to less documentation around the src-dir Layout for python packages.
So I started a small repository which just shows how to do it properly.

```txt
.
├── MANIFEST.in
├── README.md
├── setup.py
├── src
│   └── rocket_science
│       ├── __init__.py
│       └── hello.py
└── tests
    ├── __init__.py   # this is not needed if you use a tooling like pytest
    └── test_hello.py
```

## Running Pytest

### With developer installation

```console
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