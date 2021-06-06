from typing import Iterator, Tuple


def read(f) -> Iterator[Tuple[str, int]]:
    """Reads a text file an produces a stream of tuples representing the page number(s) and frame count(s)"""
    page = 1
    frame = 0
    combo = False
    for line_number, line in enumerate(f.readlines()):
        for line_position, c in enumerate(line):
            if c.isspace():
                pass
            elif c == "-":
                yield f"{page}-{page+1}", frame
                page += 1
                frame = 0
            elif c == "*":
                combo = not combo
            elif c.isdigit():
                if frame and not combo:
                    yield str(page), frame
                    page += 1
                    frame = 0
                frame = frame * 10 + int(c)
            else:
                raise RuntimeError(
                    f"Unexpected {c}, line {line_number}, position {line_position}"
                )
    if frame:
        yield str(page), frame
