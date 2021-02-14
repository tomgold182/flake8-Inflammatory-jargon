import ast
import sys
import re
import json
from flake8.utils import stdin_get_value
from pycodestyle import readlines
from typing import Generator
from typing import List
from typing import Tuple

if sys.version_info < (3, 8):
    import importlib_metadata
else:
    import importlib.metadata as importlib_metadata

WORDS_FILE = 'data/words.json'


class InflammatoryJargonPlugin:
    name = __name__
    version = importlib_metadata.version(__name__)

    def __init__(self, tree: ast.Module, filename: str) -> None:
        self.filename = filename
        with open(WORDS_FILE) as f:
            self.Inflammatory_words = json.load(f)
        self._pattern = self._get_pattern()
        self._regex = re.compile(f'(?=({self._pattern}))', flags=re.IGNORECASE)
        self.violation_code = "IJU100"
        self.base_violation_msg = f'{self.violation_code} inflammatory jargon detected'

    def run(self) -> Generator[Tuple[int, int, str, type], None, None]:
        """Run the linter and return a generator of errors."""
        lines = self._get_file_content()
        yield from self._get_content_errors(lines)

    def _get_pattern(self) -> str:
        """Get a set of bad words."""
        return '|'.join(self.Inflammatory_words.keys())

    def _get_file_content(self) -> List[str]:
        """Return file content as a list of lines."""
        if self.filename in ('stdin', '-', None):
            return stdin_get_value().splitlines(True)
        else:
            return readlines(self.filename)

    def _get_content_errors(self, content) -> Generator[Tuple[int, int, str, type], None, None]:
        """Get file content errors if any exist."""
        if self._pattern == '':
            yield from ()
            return
        for row_number, row in enumerate(content, 1):
            errors = self._check_row(row)
            yield from (
                (
                    row_number,
                    column,
                    f'{self.base_violation_msg},consider switching {Inflammatory_word} with {self.Inflammatory_words[Inflammatory_word]}',
                    type(self),
                )
                for column, Inflammatory_word in errors
            )

    def _check_row(self, line: str) -> Generator[Tuple[int, str], None, None]:
        """Return a list containing bad words and their positions."""

        yield from (
            (match.start(), match.group(1)) for match in self._regex.finditer(line)
        )

