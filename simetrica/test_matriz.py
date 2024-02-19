import matriz
import pytest


@pytest.mark.parametrize(
    "matris,resultado",
    [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], False),
        ([[3, 2, 8], [2, 4, 0], [8, 0, 6]], True),
        ([[1, 1, 1], [2, 2, 2], [3, 3, 3]], False),
    ],
)
def test_matriz(matris, resultado):
    assert matriz.es_simetrica(matris) == resultado
