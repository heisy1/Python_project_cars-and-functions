from dataclasses import dataclass

@dataclass
class Masina:
    marca: str
    model: str
    tokenMasina: str
    pretAchizitie: int
    pretVanzare: int

    @property
    def id(self):
        return self.tokenMasina

    def __str__(self):
        return f"Marca: {self.marca}, modelul: {self.model}, tokenMasina: {self.tokenMasina}, pret achizitie: {self.pretAchizitie}, pret vanzare: {self.pretVanzare}"
    