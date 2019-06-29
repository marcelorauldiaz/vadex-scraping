import requests
from bs4 import BeautifulSoup as BS
import array
#pr= []
#pc= []
registro=1
o = open('/home/roxana/Dropbox/alfabeta/Mayo/vadex-result.txt', 'w+')
f = open('/home/roxana/Dropbox/alfabeta/Mayo/name-html.txt', 'r')
for line in f:
    req = requests.get(line.strip())
    status_code = req.status_code
    print "***************************************"
    if status_code == 200:
        print "Producto:"+line.strip()
        soup = BS(req.text, 'html.parser')

        entradas = soup.find_all('table', {'class': 'estandarc'})
        for i, entrada in enumerate(entradas):
             laboratorio = entrada.find('span', 'defecto').getText()
             print "laboratorio:"+laboratorio

        entradas = soup.find_all('tr', {'class': 'lproducto'})
        for i, entrada in enumerate(entradas):
             name = entrada.find('span', 'tproducto').getText()
             print "Nombre producto:"+name


        entradas = soup.find_all('tr', {'class': 'sproducto'})
        for i, entrada in enumerate(entradas):
             droga = entrada.find('span', 'defecto').getText()
             print "droga:"+droga

        entradas = soup.find_all('td', {'class': 'textor'})
        for i, entrada in enumerate(entradas):
            if i==1:
                accion  = entrada.find('span', 'defecto').getText()
                print "accion:"+accion

        entradas = soup.find_all('table', {'class': 'presentacion'})
        for p, entrada in enumerate(entradas):
            presentacion = entrada.find('td', 'tddesc').getText()
            precio = entrada.find('td', 'tdprecio').getText()
            #pr.append(presentacion)
            #pc.append(precio)
            print "presentacion:"+presentacion
            print "precio:"+precio
            #No tenemos: tipoventa, via, preciopami
            #id@name@presentacion@laboratorio@tipoventa@droga@accion@precio@via@true@preciopami
            o.write("%s@%s@%s@%s@@%s@%s@%s@@true@\n" % (str(registro).encode('ascii', 'ignore'), name.encode('ascii', 'ignore'), presentacion.encode('ascii', 'ignore'), laboratorio.encode('latin_1', 'ignore'), droga.encode('latin_1', 'ignore'), accion.encode('latin_1', 'ignore'), precio.encode('ascii', 'ignore')) )
            registro = registro + 1
        #pc[:]=[]
        #pr[:]=[]
        #cont=cont+1
    else:
        print "Status Code %d" % status_code
o.close()
