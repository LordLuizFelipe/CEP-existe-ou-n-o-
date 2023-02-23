import requests

def validar_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'erro' not in data:
            return True
    return False

# Exemplo de uso
cep = input('Digite o CEP: ')
if validar_cep(cep):
    print(f'O CEP {cep} é válido!')
else:
    print(f'O CEP {cep} é inválido!')
