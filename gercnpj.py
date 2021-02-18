from requests import get

def GeradorCNPJ(message):

    cnpj = get('http://geradorapp.com/api/v1/cnpj/generate?token=f01e0024a26baef3cc53a2ac208dd141').json()['data']['number_formatted']
    return f'*CNPJ: *`{cnpj}`'
