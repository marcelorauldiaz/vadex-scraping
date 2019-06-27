import requests
from bs4 import BeautifulSoup as BS

f = open('/home/marcelo/Dropbox/alfabeta/Mayo/test-name.txt', 'r')
for line in f:
    req = requests.get(line.strip())
    status_code = req.status_code
    print status_code
    if status_code == 200:
        print("OK")
        soup = BS(req.text, 'html.parser')
        entradas = soup.find_all('table', {'class': 'estandarc'})
        for i, entrada in enumerate(entradas):
             laboratorio = entrada.find('span', 'defecto').getText()
             print(laboratorio)
        entradas = soup.find_all('tr', {'class': 'sproducto'})
        for i, entrada in enumerate(entradas):
             droga = entrada.find('span', 'defecto').getText()
             print(droga)
       
        entradas = soup.find_all('td', {'class': 'textor'})
        for i, entrada in enumerate(entradas):
             accion  = entrada.find('span', 'defecto').getText()
             print(accion)
 
        entradas = soup.find_all('table', {'class': 'presentacion'})
        for i, entrada in enumerate(entradas):
            presentacion = entrada.find('td', 'tddesc').getText()
            precio = entrada.find('td', 'tdprecio').getText()
            print (presentacion)
            print(precio)
    
    else:
        print "Status Code %d" % status_code
