import sumas


@pytest.mark.parametrize(
    [
        ("hola", "b221d9dbb083a7f33428d7c2a3c3198ae925614d70210e28716ccaa7cd4ddb79"),
        ("dori", "447f75a8ebdbdb79a57f0b8cebbfba183820cf54a8119ac01449b30499e5ef0e"),
        ("java", "38a0963a6364b09ad867aa9a66c6d009673c21e182015461da236ec361877f77"),
    ]
)
def test_sumas(texto, resultado):
    assert sumas.obtener_hash(texto) == resultado
