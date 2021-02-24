import ast
import os
from flake8_inflammatory_jargon.checker import InflammatoryJargonChecker
from typing import Set

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
TRIVAL_CASE_FILE_PATH = 'test files/clean_jargon_case.py'
INFLAMMATORY_CASE_FILE_PATH = 'test files/Inflammatory_jargon_case.py'

def _results(file_path:str) -> Set[str]:
    tree = ast.parse("")
    plugin = InflammatoryJargonChecker(tree=tree, filename=f'{ROOT_DIR}\\{file_path}')
    return {f'{line}:{col} {msg}' for line, col, msg, _ in plugin.run()}

def test_clean_jargon_case():
    assert _results(TRIVAL_CASE_FILE_PATH) == set()

def test_inflammatory_jargon_case():
    ret = _results(INFLAMMATORY_CASE_FILE_PATH)
    assert ret == {"3:0 IJU100 inflammatory jargon detected,consider switching blacklist with blocklist"}
