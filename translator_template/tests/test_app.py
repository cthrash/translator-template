import os
from tempfile import TemporaryDirectory

from translator_template.app import generate

TEST_DIR = os.path.dirname(os.path.abspath(__file__))


def test_generate():
    with TemporaryDirectory() as dir:
        in_file = os.path.join(TEST_DIR, "data", "test.txt")
        out_file = os.path.join(dir, "test.docx")
        generate(in_file, out_file)
