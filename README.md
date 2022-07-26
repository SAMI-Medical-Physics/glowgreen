# glowgreen
A Python package. See the documentation.
Instructions to generate the documentation are given below. 

## Requires
- Python >= 3.9 (for return type hint tuple[])
- Python packages
    - numpy
    - scipy
    - matplotlib
    - pandas

## Installation
This package will (hopefully) be published on the Python Package Index (PyPI), then it can be installed using pip:

    pip install glowgreen

For now, download the source code and add the glowgreen-master\src\ directory to the PYTHONPATH environment variable. For example, for Windows:

    set PYTHONPATH=%PYTHONPATH%;\path\to\glowgreen-master\src\

For Linux:

    export PYTHONPATH="${PYTHONPATH}:/path/to/glowgreen-master/src/"

## Testing

Some tests can be ran using pytest.

    pip install pytest

In the glowgreen-master directory run:

    python -m pytest

## Documentation

Documentation including API reference can be generated using sphinx. 
If the docs/source/ directory does not exist, see howto_documentation.md to generate the documentation from scratch.
Otherwise, do the following:

Check the Projection information is up-to-date in docs/source/conf.py (e.g. version).

Install sphinx:

    pip install sphinx

Github does not have empty directories docs/source/_static and docs/source/_templates.
Optionally create these empty directories to avoid a warning in the next step.

In docs directory, run:

    make html

When this repository is made public, this documentation should be hosted on ReadTheDocs.
See https://sphinx-rtd-tutorial.readthedocs.io/en/latest/read-the-docs.html.

## Author

Jake Forster (jake.forster@sa.gov.au)

## Source 

https://github.com/JakeForster/glowgreen

## Copyright

Glowgreen is Copyright (C) 2022 Jake Forster and South Australia Medical Imaging.

## Licence

**No public licence.**

## Publishing

Once a licence is arranged, I intend to publish glowgreen on the Python Package Index (PyPI). 
See https://pypi.org/ and https://packaging.python.org/en/latest/tutorials/packaging-projects/.