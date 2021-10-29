'''Ejercicio 1:
Modifica geojson.py o geoxml.py para imprimir en pantalla
el código de país de dos caracteres de los datos recuperados.
Añade comprobación de errores, de modo que tu programa no rastree los
datos si el código del país no está presente.
Una vez que lo tengas funcionando,
busca “Océano Atlántico” y asegúrate de que es capaz de
gestionar ubicaciones que no estén dentro de ningún país.'''
import urllib.request
import urllib.parse
import urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else:
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
# Ann Arbor, MI
while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break

    parms = dict()
    parms['address'] = address
    if api_key is not False:
        parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)
# recorro el diccionario
    for item in js['results']:
        for elemento in item['address_components']:
            if elemento['types'][0] == 'country':
                print(elemento['short_name'])
            else:
                print('No existe código de país')


# Ann Arbor, MI
