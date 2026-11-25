d = {"nom": "Maria", "edat": 21}
d["edat"]              # 21 (KeyError si la clau no hi és)
d.get("curs", "?")     # "?" (valor per defecte, sense error)
d["nota"] = 9.5        # afegeix la clau o en modifica el valor
d.pop("nota")          # elimina i retorna 9.5
"nom" in d             # True (mira les claus)
d.keys(), d.values(), d.items()
d.update({"edat": 22}) # fusiona un altre diccionari