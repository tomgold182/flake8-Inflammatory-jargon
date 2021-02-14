import ast
import os
from flake8_Inflammatory_jargon_checker import InflammatoryJargonPlugin
from typing import Set

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def _results(s: str) -> Set[str]:
    tree = ast.parse(s)
    plugin = InflammatoryJargonPlugin(tree=tree, filename=f'{ROOT_DIR}\\flake8_Inflammatory_jargon_checker_test.py')
    return {f'{line}:{col} {msg}' for line, col, msg, _ in plugin.run()}

def test_trivial_case():
    assert _results('') == set()

def test_inflammatory_jargon():
    ret = _results('blacklist = {}')
    assert ret == {f'1:1 IJU100 inflammatory jargon detected'}

def test_allowed_jargon():
    assert _results('blocklist={}') == set()
