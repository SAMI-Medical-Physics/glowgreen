# Instructions for generating documentation

Follow these instructions to generate the documentation from scratch (e.g. if the docs/source/ directory does not exist).

## Setting up

Install sphinx:

    pip install sphinx

In the docs directory run

    sphinx-quickstart

and follow the prompts.

Copy overview.rst into docs/source/.

Run src/glowgreen_sample.py and save the figures in docs/source with filenames docs_cpat.png and docs_cpat_dose.png.

## Editing conf.py
Add the following to docs/source/conf.py.
At the top:

    import os
    import sys
    sys.path.insert(0, os.path.abspath('../..'))
    sys.path.insert(0, os.path.abspath('../../src/'))
    sys.path.insert(0, os.path.abspath('../../src/glowgreen/'))

And further down:

    extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon']

To document `__init__`:

    autoclass_content = 'both'

Choose this style:

    html_theme = 'classic'

## API reference

In the docs directory run:

    sphinx-apidoc -o ./source ../src/glowgreen/ -e -M

In index.rst, write 'overview', 'modules' under toctree

Change heading in modules.rst to 'API reference'
and add '.. _API reference:' before the heading

in glowgreen.close_contact.rst, write ':private-members: _ContactPattern' under automodule

## Finish

In docs directory run:

    make html
