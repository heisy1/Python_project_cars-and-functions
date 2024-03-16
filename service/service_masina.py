import time
from domain.masina import Masina


class ServiceMasina:
    def __init__(self, Repository):
        self.__repository = Repository

    def adauga(self, marca, model, tokenMasina, pretAchizitie, pretVanzare):
        masina = Masina(marca, model, tokenMasina, pretAchizitie, pretVanzare)
        self.__repository.adauga(masina)

    def get_all(self):
        return self.__repository.find_all()

    def get_by_id(self, id):
        return self.__repository.find_by_id(id)

    def cautare_secv(self, id):
        for i in self.__repository.find_all():
            if i.id == id:
                return i

    def cautare_binara(self, id):
        left = 0
        right = len(self.__repository.find_all())-1
        lista = self.__repository.find_all()
        self.mergeSort(lista)
        start_time = time.time()
        while left<=right:
            mid = (left+right)//2
            if lista[mid].id == id:
                print("the function ends in ", time.time() - start_time, "secs")
                return lista[mid]
            if lista[mid].id > id:
                right = mid - 1
            if lista[mid].id < id:
                left = mid + 1

    def sortare_selectie(self):
        lista = self.__repository.find_all()
        for i in range(0,len(lista)-1):
            for j in range(i+1, len(lista)):
                if lista[i].tokenMasina > lista[j].tokenMasina:
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux

        return lista

    def sortare_selectie_model(self):
        lista = self.__repository.find_all()
        for i in range(0,len(lista)-1):
            p=i
            for j in range(i+1, len(lista)):
                if lista[i].marca > lista[j].marca:
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
                elif lista[i].marca == lista[j].marca:
                    if lista[i].model > lista[j].model:
                        aux = lista[i]
                        lista[i] = lista[j]
                        lista[j] = aux


        return lista

    def sortare_selectie_marca_model(self):
        lista = self.__repository.find_all()
        for i in range(0,len(lista)-1):
            p=i
            for j in range(i+1, len(lista)):
                if lista[i].marca > lista[j].marca:
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
                elif lista[i].marca == lista[j].marca:
                    if lista[i].model > lista[j].model:
                        aux = lista[i]
                        lista[i] = lista[j]
                        lista[j] = aux
                    elif lista[i].model == lista[j].model:
                        if lista[i].tokenMasina > lista[j].tokenMasina:
                            aux = lista[i]
                            lista[i] = lista[j]
                            lista[j] = aux

        return lista

    def sortare_selectie_profit(self):
        lista = self.__repository.find_all()
        for i in range(0,len(lista)-1):
            p=i
            for j in range(i+1, len(lista)):
                if lista[i].pretVanzare-lista[i].pretAchizitie > lista[j].pretVanzare-lista[j].pretAchizitie:
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux

        return lista

    def sortare(self):
        st = 0
        dr = len(self.__repository.find_all())-1
        lista = self.__repository.find_all()
        self.mergeSort(lista)
        return lista

    def mergeSort(self, myList):
        if len(myList) > 1:
            mid = len(myList) // 2
            left = myList[:mid]
            right = myList[mid:]

            self.mergeSort(left)
            self.mergeSort(right)

            i = 0
            j = 0

            k = 0

            while i < len(left) and j < len(right):
                if left[i].tokenMasina <= right[j].tokenMasina:
                    myList[k] = left[i]
                    i += 1
                else:
                    myList[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                myList[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                myList[k] = right[j]
                j += 1
                k += 1


    def sortare_marca(self):
        st = 0
        dr = len(self.__repository.find_all())-1

        lista = self.__repository.find_all()
        self.mergeSort_marca(lista)
        return lista

    def mergeSort_marca(self, myList):
        if len(myList) > 1:
            mid = len(myList) // 2
            left = myList[:mid]
            right = myList[mid:]

            self.mergeSort_marca(left)
            self.mergeSort_marca(right)

            i = 0
            j = 0
            k = 0

            while i < len(left) and j < len(right):
                if left[i].marca < right[j].marca:
                    myList[k] = left[i]
                    i += 1
                elif left[i].marca > right[j].marca:
                    myList[k] = right[j]
                    j += 1
                else:
                    if left[i].model <= right[j].model:
                        myList[k] = left[i]
                        i += 1
                    else:
                        myList[k] = right[j]
                        j += 1

                k += 1

            while i < len(left):
                myList[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                myList[k] = right[j]
                j += 1
                k += 1

    def sortare_marca_model(self):
        st = 0
        dr = len(self.__repository.find_all())-1

        lista = self.__repository.find_all()
        self.mergeSort_marca_model(lista)
        return lista

    def mergeSort_marca_model(self, myList):
        if len(myList) > 1:
            mid = len(myList) // 2
            left = myList[:mid]
            right = myList[mid:]

            self.mergeSort_marca_model(left)
            self.mergeSort_marca_model(right)

            i = 0
            j = 0
            k = 0

            while i < len(left) and j < len(right):
                if left[i].marca < right[j].marca:
                    myList[k] = left[i]
                    i += 1
                elif left[i].marca > right[j].marca:
                    myList[k] = right[j]
                    j += 1
                else:
                    if left[i].model < right[j].model:
                        myList[k] = left[i]
                        i += 1
                    elif left[i].model > right[j].model:
                        myList[k] = right[j]
                        j += 1
                    else:
                        if left[i].tokenMasina < right[j].tokenMasina:
                            myList[k] = left[i]
                            i += 1
                        else:
                            myList[k] = right[j]
                            j += 1

                k += 1

            while i < len(left):
                myList[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                myList[k] = right[j]
                j += 1
                k += 1

    def sortare_profit(self):
        st = 0
        dr = len(self.__repository.find_all())-1
        lista = self.__repository.find_all()
        self.mergeSort_profit(lista)
        return lista

    def mergeSort_profit(self, myList):
        if len(myList) > 1:
            mid = len(myList) // 2
            left = myList[:mid]
            right = myList[mid:]

            self.mergeSort_profit(left)
            self.mergeSort_profit(right)

            i = 0
            j = 0

            k = 0

            while i < len(left) and j < len(right):
                if left[i].pretVanzare-left[i].pretAchizitie < right[j].pretVanzare-right[j].pretAchizitie:
                    myList[k] = left[i]
                    i += 1
                elif left[i].pretVanzare-left[i].pretAchizitie > right[j].pretVanzare-right[j].pretAchizitie:
                    myList[k] = right[j]
                    j += 1
                else:
                    if left[i].marca < right[j].marca:
                        myList[k] = left[i]
                        i += 1
                    elif left[i].marca > right[j].marca:
                        myList[k] = right[j]
                        j += 1
                    else:
                        if left[i].tokenMasina <= right[j].tokenMasina:
                            myList[k] = left[i]
                            i += 1
                        else:
                            myList[k] = right[j]
                            j += 1
                k += 1

            while i < len(left):
                myList[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                myList[k] = right[j]
                j += 1
                k += 1