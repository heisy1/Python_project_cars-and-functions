class RepositoryMasina:
    def __init__(self):
        self.__masina = {}

    def adauga(self, masina):
        if self.find_by_id(masina.id) is None:
            self.__masina[masina.id] = masina
        else:
            raise ValueError("Duplicate token masina!")

    def find_by_id(self, id):
        return self.__masina.get(id, None)

    def find_all(self):
        return list(self.__masina.values())

