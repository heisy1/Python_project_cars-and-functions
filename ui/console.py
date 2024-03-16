import time
import timeit


class Console:
    def __init__(self, Service):
        self.__service = Service

    def adauga(self):
        marca = input("Scrieti marca: ")
        model = input("Screti modelul: ")
        tokenMasina = input("Scrieti token-ul: ")
        pretAchizitie = int(input("Scrieti pretul de achizitie: "))
        pretVanzare = int(input("Scrieti pretul de vanzare: "))
        self.__service.adauga(marca, model, tokenMasina, pretAchizitie, pretVanzare)

    def afisare(self):
        print(*self.__service.get_all(), sep= "\n")

    def search(self):
        id = input("Screti token-ul masini: ")
        start_time = timeit.default_timer()
        print(self.__service.cautare_secv(id))
        print("the function ends in ", timeit.default_timer() - start_time, "secs")

    def search_binar(self):
        id = input("Screti token-ul masini: ")
        print(self.__service.cautare_binara(id))

    def sortare(self):
        start_time = timeit.default_timer()
        print(*self.__service.sortare(), sep= "\n")
        print("the function ends in ", timeit.default_timer()-start_time, "secs")

    def sortare_marca(self):
        start_time = timeit.default_timer()
        print(*self.__service.sortare_marca(), sep= "\n")
        print("the function ends in ", timeit.default_timer()-start_time, "secs")

    def sortare_marca_model(self):
        start_time = timeit.default_timer()
        print(*self.__service.sortare_marca_model(), sep="\n")
        print("the function ends in ", timeit.default_timer()-start_time, "secs")

    def sortare_profit(self):
        start_time = timeit.default_timer()
        print(*self.__service.sortare_profit(), sep="\n")
        print("the function ends in ", timeit.default_timer() - start_time, "secs")

    def sortare_selectie(self):
        start_time = timeit.default_timer()
        print(*self.__service.sortare_selectie(), sep="\n")
        print("the function ends in ", timeit.default_timer() - start_time, "secs")

    def sortare_selectie_model(self):
        start_time = timeit.default_timer()
        print(*self.__service.sortare_selectie_model(), sep="\n")
        print("the function ends in ", timeit.default_timer()-start_time, "secs")

    def sortare_selectie_marca_model(self):
        start_time = timeit.default_timer()
        print(*self.__service.sortare_selectie_marca_model(), sep="\n")
        print("the function ends in ", timeit.default_timer() - start_time, "secs")

    def sortare_selectie_profit(self):
        start_time = timeit.default_timer()
        print(*self.__service.sortare_selectie_profit(), sep="\n")
        print("the function ends in ", timeit.default_timer() - start_time, "secs")


    def printMenu(self):
        print("1.Adauga masina")
        print("2.Cauta masina")
        print("2.0.Cautare masina binar")
        print("3.Sortare dupa token")
        print("4.Sortare dupa marca,model")
        print("5.Sortare dupa marca,model,token")
        print("6.Sortare dupa profit")
        print("7.Sortare selectie")
        print("8.Sortare selectie, marca, model")
        print("9.Sortare selectie, marca, model, token")
        print("10.Sortare selectie, profit")
        print("a.Afisare")
        print("x.Iesire")

    def adaugaMasini(self):
        self.__service.adauga("Chevrolet", "Malibu", "fuvjx4hgj4", 4236, 4199)
        self.__service.adauga("Chevrolet", "Silverado", "wjckx944uj", 7693, 7494)
        self.__service.adauga("Ford", "Transit", "iumj7qirqq", 3214, 9045)
        self.__service.adauga("Volvo", "850", "bv55fq9ewq", 2640, 13400)
        self.__service.adauga("Toyota", "LandCruiser", "fdm98gbg9j", 3358, 8395)
        self.__service.adauga("Chevrolet", "Silverado3500HD", "98kskdu1cr", 1570, 11285)
        self.__service.adauga("Toyota", "T100", "0yi1ocmlxn", 4156, 8313)
        self.__service.adauga("Toyota", "Avalon", "x8fu5lo3m9", 8920, 3916)
        self.__service.adauga("Audi", "A8", "340fvt339e", 4720, 7764)
        self.__service.adauga("Ford", "Taurus", "sqaybhpqj4", 3013, 13071)
        self.__service.adauga("Audi", "S7", "2qyapt359a", 5705, 3122)
        self.__service.adauga("Audi", "RS5", "nj3l315y1x", 3254, 11875)
        self.__service.adauga("Chevrolet", "Cavalier", "h2uwk5jfev", 8632, 10334)
        self.__service.adauga("Suzuki", "SX4", "ikn8ntwin4", 2036, 6299)
        self.__service.adauga("Ford", "Econoline", "d71a92ggfp", 6788, 12876)
        self.__service.adauga("Mercedes-Benz", "Mercedes-AMG", "yx6196wdcm", 5032, 3670)
        self.__service.adauga("Mercedes-Benz", "E-Class", "k6xeulilfw", 5390, 3272)
        self.__service.adauga("BMW", "M5", "lce7r3xqpr", 6919, 8237)
        self.__service.adauga("BMW", "1Series", "c36jtvjrcu", 9557, 11029)
        self.__service.adauga("Toyota", "Tundra", "xx4e32mtje", 4739, 7576)
        self.__service.adauga("Audi", "A6", "amsbl4aixl", 5463, 8885)
        self.__service.adauga("Chevrolet", "Express2500", "etxita8lic", 3976, 11103)
        self.__service.adauga("Chevrolet", "Malibu", "q2dip9g0uy", 7012, 5473)
        self.__service.adauga("Toyota", "Highlander", "wll61s7abu", 1278, 7862)
        self.__service.adauga("BMW", "X5", "ndizj7lng2", 2168, 14999)
        self.__service.adauga("Ford", "Taurus", "1yklhcll8a", 3515, 9764)
        self.__service.adauga("BMW", "3Series", "61lxnbay0c", 6692, 13222)
        self.__service.adauga("Subaru", "Outback", "z3bohgt66y", 5152, 14411)
        self.__service.adauga("Toyota", "RAV4", "3n6wpwsbqk", 6415, 7899)
        self.__service.adauga("Chevrolet", "3500RegularCab", "ynyb4usatm", 8344, 10074)
        self.__service.adauga("Suzuki", "Esteem", "qqdl4gg4r3", 6926, 10475)
        self.__service.adauga("Ford", "Fiesta", "dwhod1a3w5", 9995, 8986)
        self.__service.adauga("Toyota", "Mirai", "zn7jpf4dgp", 5806, 8925)
        self.__service.adauga("Subaru", "BRZ", "0ibdu3n47t", 2987, 3046)
        self.__service.adauga("Chevrolet", "Silverado3500RegularCab", "di5qz4ctha", 6154, 9158)
        self.__service.adauga("Ford", "F150SuperCrewCab", "btvw4mv2sp", 2881, 133440)
        self.__service.adauga("Suzuki", "Sidekick", "7s0t39eqv4", 6138, 9737)
        self.__service.adauga("Audi", "A3", "wt98fnpsku", 3816, 8993)
        self.__service.adauga("Volvo", "V40", "foi01znl24", 6604, 12283)
        self.__service.adauga("Chevrolet", "Suburban", "ke07khg1wn", 4121, 4704)
        self.__service.adauga("BMW", "3Series", "8gwhddclcg", 2940, 14865)
        self.__service.adauga("BMW", "5Series", "8fpkfs7s9d", 6058, 13860)
        self.__service.adauga("Chevrolet", "S10RegularCab", "ej39lnz1yx", 1959, 4909)
        self.__service.adauga("Mercedes-Benz", "SLK-Class", "4mq9w00wct", 9604, 4864)
        self.__service.adauga("Mercedes-Benz", "CLK-Class", "paau62q56q", 1477, 2391)
        self.__service.adauga("BMW", "3Series", "b9cjvyigx8", 2537, 8550)
        self.__service.adauga("Audi", "S4", "er37lnz1yx", 1959, 4969)
        self.__service.adauga("Mercedes-Benz", "SLS-Class", "4mq9p00wct", 9604, 4394)
        self.__service.adauga("Mercedes-Benz", "CLS-Class", "paeu62q56q", 1477, 2171)
        self.__service.adauga("BMW", "8Series", "b9cjvwigx8", 2537, 8890)

    def run_console(self):
        self.adaugaMasini()
        while True:
            self.printMenu()
            optiune = input("Scrieti optiunea: ")
            if optiune == "1":
                self.adauga()
            elif optiune == "2":
                self.search()
            elif optiune == "2.0":
                self.search_binar()
            elif optiune == "3":
                self.sortare()
            elif optiune == "4":
                self.sortare_marca()
            elif optiune == "5":
                self.sortare_marca_model()
            elif optiune == "6":
                self.sortare_profit()
            elif optiune == "7":
                self.sortare_selectie()
            elif optiune == "8":
                self.sortare_selectie_model()
            elif optiune == "9":
                self.sortare_selectie_marca_model()
            elif optiune == "10":
                self.sortare_profit()
            elif optiune == "a":
                self.afisare()
            elif optiune == "x":
                break
            else:
                print("Optiune gresita reincarcati!")