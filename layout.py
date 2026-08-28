BENTO_PATTERNS = [
    [2, 1, 1],
    [1, 2, 1],
    [1, 1, 2],
]


def bento_rows(n: int) -> list[list[int]]:
    """Split n items into row width-patterns for a bento-style grid.

    Cycles through asymmetric 3-column patterns so the "featured" (wide)
    slot moves around, giving the grid a mosaic feel instead of uniform rows.
    """
    rows: list[list[int]] = []
    i = 0
    row_idx = 0
    while i < n:
        pattern = BENTO_PATTERNS[row_idx % len(BENTO_PATTERNS)]
        remaining = n - i
        if remaining < len(pattern):
            pattern = [1] * remaining
        rows.append(pattern)
        i += len(pattern)
        row_idx += 1
    return rows
