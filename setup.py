from setuptools import setup, find_packages

setup(
    name="rocket-science",
    version="0.0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    extras_require={"test": ["pytest"], "dev": ["black", "mypy"]},
)
