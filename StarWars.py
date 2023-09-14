import requests

class StarWars:
    
    def __init__(self):
        self.base_url = "https://swapi.dev/api/"

    def transformar_json(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            if response.status_code == 404:
                print("Erro 404: Recurso não encontrado.")
            else:
                print(f"Erro {response.status_code}: Falha na solicitação da API.")
            return None

    def obter_personagem(self, id_personagem):
        url = f"{self.base_url}people/{id_personagem}/"
        return self.transformar_json(url)

    def obter_filme(self, id_filme):
        url = f"{self.base_url}films/{id_filme}/"
        return self.transformar_json(url)

    def obter_planeta(self, id_planeta):
        url = f"{self.base_url}planets/{id_planeta}/"
        return self.transformar_json(url)
