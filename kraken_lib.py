import requests

def precio_crypto(pair):
    url = f'https://api.kraken.com/0/public/Ticker?pair={pair}'
    try:
        response = requests.get(url)
        data = response.json()

        if 'result' in data and pair in data['result']:
            pair_info = data['result'][pair]
            price = pair_info['c'][0]
            return float(price)  # Convert the price to float
        else:
            return None  # Return None if there is an issue with the response

    except Exception as e:
        return None  # Return None if there is an exception

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
    
"""
def obtener_10_menores_valores():
    url = 'https://api.kraken.com/0/public/Assets'
    try:
        response = requests.get(url)
        data = response.json()
        cryptos = [asset_info['altname'] for asset_info in data['result'].values()]
        
        # Obtener los precios de todas las criptomonedas
        precios = {}
        for crypto in cryptos:
            pair = f'{crypto}USD'
            precio = precio_crypto(pair)
            
            if precio is not None:
                precios[crypto] = precio
        
        # Ordenar las criptomonedas por valor
        sorted_cryptos = sorted(cryptos, key=lambda x: precios[x])
        
        # Obtener las 10 criptomonedas con menor valor
        menor_valor_10 = list()
        for precio in range(10):
            if precios[sorted_cryptos[precio]] is not None:
                menor_valor_10.append(sorted_cryptos[precio])
        
        return menor_valor_10
    except Exception as e:
        return f'Error al obtener las 10 criptomonedas con menor valor: {str(e)}'
"""