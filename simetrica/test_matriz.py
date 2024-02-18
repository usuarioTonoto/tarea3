import matriz
import pytest


@pytest.mark.parametrize(
    "matriz,resultado",
    [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], False),
        ([[3, 2, 8], [2, 4, 0], [8, 0, 6]], True),
        ([[1, 1, 1], [2, 2, 2], [3, 3, 3]], False),
    ],
)
def test_matriz(matriz, resultado):
    assert matriz.es_simetrica(matriz) == resultado
