from io import StringIO

from translator_template.parse import read


def test_read():
    def read_from(s):
        with StringIO(s) as f:
            return [p for p in read(f)]

    assert [("1", 2)] == read_from("2")
    assert [("1", 2), ("2", 3)] == read_from("23")
    assert [("1", 2), ("2-3", 3)] == read_from("23-")
    assert [("1", 56)] == read_from("*56*")
    assert [("1-2", 56)] == read_from("*56*-")
