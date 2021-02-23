# flake8-Inflammatory-jargon


A flake8 plugin that checks your code for inflammable words like blacklist, whitelist,master, etc.. and suggests to replace them with more appropriate words

## What Inflammatory language is?
Inflammatory language is a form of speech that is used with the intent to stir up emotions, elicit anger, or invoke a physical reaction. Name calling is one form, but the use is generally wider in scope, in the sense that it is used to attack, oppress, or denigrate groups of people, or focus hate or anger on a public figure. (rationalwiki)

## Warnings
This package adds 1 new flake8 warning

-  ``IJU100``: inflammatory jargon detected, consider switching %inflammatory word% with %appropriate word%

Installation
------------

If you don't already have it, install ``flake8``::

    $ pip install flake8

Then, install the extension::

    $ pip install flake8-Inflammatory-jargon

Usage
-----

Run the following to verify that the plugin has been installed correctly::

    $ flake8 --version
    2.0 (pep8: 1.4.6, flake8-Inflammatory-jargon: 1.0.0, pyflakes: 0.7.3)

Now, when you run ``flake8``, the plugin will automatically be used.
## Extending the inflammatory jargon
flake8-Inflammatory-jargon is highly extensible and built to easily allow the addition of more inflammable words and matching replacements suggestions. All you need to do is to open data/inflammatory_words.json and add inflammatory words together with their appropriate replacement suggestions

## Contributing
1. Clone
2. Add more inflammatory words & replacement suggestions the data/inflammatory_words.json file
3. Type `pip install -e .` in order to test your changes (I am using pytest)
3. Submit a PR
