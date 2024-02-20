import hashlib


def obtener_hash(texto):
    h = hashlib.new("sha256")
    h.update(bytes(texto, "utf-8"))
    return h.hexdigest()

    # bdatos = bytes(datos, "utf-8")
    # texto = hashlib.new("sha256", bdatos)
