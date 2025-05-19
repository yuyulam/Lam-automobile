
class Client:
    def __init__(self, nom: str, id: int):
        self.nom = nom
        self.id = id

    def infos(self) -> str:
        return f"Client {self.id} : {self.nom}"
