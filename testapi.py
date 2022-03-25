from requests import request

def api_catfact():

    protocolo = 'https://'
    servidor = 'catfact.ninja'
    recurso = '/fact'

    url = protocolo + servidor + recurso
    print(f'Conectando a: {url}')
    
    respuesta = request('GET', url)

    print('Respuesta: ')
    print(respuesta.text)
    print('\n')

    return respuesta


def api_catfacts(n=5,lon=30):

    protocolo = 'https://'
    servidor = 'catfact.ninja'
    recurso = '/facts'
    param1 = f'?limit={n}'
    param2 = f'&max_length={lon}'

    url = protocolo + servidor + recurso + param1 + param2
    print(f'Conectando a: {url}')
    
    respuesta = request('GET', url)

    print('Respuesta: ')
    x = [print(f'{i+1}.- {hecho["fact"]}') for i,hecho in enumerate(respuesta.json()['data'])]
    print('\n')

    return respuesta


def api_shortcode():

    url_larga = input('Escribe la URL a acortar: ')
    url =  f'https://api.shrtco.de/v2/shorten?url={url_larga}'
    print(f'Conectando a: {url}')
    
    respuesta = request("POST", url)

    print('Respuesta: ',respuesta.json()['result']['short_link3']) if respuesta.ok else print('Error:',respuesta.reason)

    return respuesta


def api_shortcode_v2():

    protocolo = 'https://'
    servidor = 'api.shrtco.de'
    recurso = '/v2/shorten'
    parametro = f'?url=https://colab.research.google.com/drive/14DIPx5Q2-PuuorvtaRQK-98obAAKJhsk?usp=sharing'

    url = protocolo + servidor + recurso + parametro
    
    print(f'Conectando a: {url}')
    
    respuesta = request("POST", url)

    print('Respuesta: ',respuesta.json()['result']['short_link3']) if respuesta.ok else print('Error:',respuesta.reason)

    return respuesta


if __name__ == '__main__':

    # Funcion 1
    api_catfact()

    # Funcion 2
    api_catfacts()

    # Funcion 3
    api_shortcode()
