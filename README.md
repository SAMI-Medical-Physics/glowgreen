[![DOI](https://zenodo.org/badge/546642261.svg)](https://zenodo.org/badge/latestdoi/546642261)

# glowgreen
A small Python package for calculating radiation dose from close contact patterns with radioactive patients. 

## Requires
- Python >= 3.9

## Installation
Install the package from the [Python Package Index](https://pypi.org/) (PyPI) using `pip`:

    python -m pip install --upgrade glowgreen

Alternatively, if you have a clone of the repository on your local computer, you can install it via the *pyproject.toml* file.
First update your pip:

    python -m pip install --upgrade pip

Then enter e.g.:

    python -m pip install -e \path\to\glowgreen-master\

These are the preferred methods as they handle the dependencies for you. 
Another way is to add the **glowgreen-master\src** directory to the PYTHONPATH environment variable. For example, for Windows:

    set PYTHONPATH=%PYTHONPATH%;\path\to\glowgreen-master\src\

## Dependencies
Python packages:
- `numpy` >= 1.21.4
- `scipy` >= 1.7.3
- `matplotlib` >= 3.5.0
- `pandas` >= 1.3.4

It has not been tested with earlier versions of these packages.

## Testing
You can run some tests if there is a clone of the repository on your local computer. Install `pytest`:

    python -m pip install --upgrade pytest

Then in the **glowgreen-master** directory run:

    python -m pytest

## Documentation
Documentation including API reference can be found here: https://glowgreen.readthedocs.io

### Build documentation locally

Documentation is generated using `sphinx`.
See this [tutorial](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/read-the-docs.html). 

If the **docs/source/** directory does not exist, see *howto_documentation.md* to generate the documentation from scratch.
Otherwise, do the following:

Check the project information is up-to-date in *docs/source/conf.py*.

Install sphinx:

    python -m pip install sphinx

Github does not have empty directories **docs/source/_static** and **docs/source/_templates**.
Optionally create these empty directories to avoid a warning in the next step.

In **docs** directory, run:

    make html


## Source 
https://github.com/SAMI-Medical-Physics/glowgreen

## Bug tracker
https://github.com/SAMI-Medical-Physics/glowgreen/issues

## Authors
- Jake Forster (Jake.Forster@sa.gov.au)
- Erin Lukas (Erin.Lukas@sa.gov.au)

## Copyright
`glowgreen` is Copyright (C) 2022, 2023 South Australia Medical Imaging.

## License
MIT license. See LICENSE file.

## Publishing
`glowgreen` is published on PyPI:

https://pypi.org/project/glowgreen/

See this [tutorial](https://packaging.python.org/en/latest/tutorials/packaging-projects/).

## Publications
Papers that use `glowgreen`:
- Close contact restriction periods for patients who received radioactive iodine-131 therapy for differentiated thyroid cancer, J. C. Forster et al., In preparation.
