from repository.repository_masina import RepositoryMasina
from service.service_masina import ServiceMasina
from ui.console import Console

if __name__ == "__main__":
    repository = RepositoryMasina()
    service = ServiceMasina(repository)
    consola = Console(service)
    consola.run_console()