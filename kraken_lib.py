import requests

def precio_crypto(pair):
    url = f'https://api.kraken.com/0/public/Ticker?pair={pair}'
    try:
        response = requests.get(url)
        data = response.json()

        if 'result' in data and pair in data['result']:
            pair_info = data['result'][pair]
            price = pair_info['c'][0]
            return float(price)
        else:
            return None

    except Exception as e:
        return None

def lista_crypto():
    url = 'https://api.kraken.com/0/public/Assets'
    try:
        response = requests.get(url)
        data = response.json()
        cryptos = [asset_info['altname'] for asset_info in data['result'].values()]
        return cryptos
    except Exception as e:
        return f'Error al obtener la lista de criptomonedas: {str(e)}'
    


def intercambios(cripto):
    url = f'https://api.kraken.com/0/public/Trades?pair={cripto}'
    try:
        response = requests.get(url)
        data = response.json()

        if 'result' in data and cripto in data['result']:
            info = data['result'][cripto][0][0:2]
            return info
        else:
            return None
    except Exception as e:
        return None
    