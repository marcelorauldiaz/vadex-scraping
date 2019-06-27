import requests
from bs4 import BeautifulSoup as BS
import array
pr= []
pc= []
ii=1
#o = open('/home/marcelo/Dropbox/alfabeta/Mayo/vadex-result.txt', 'w+')
f = open('/home/marcelo/Dropbox/alfabeta/Mayo/test-name.txt', 'r')
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
            pr.append(presentacion)
            pc.append(precio)
            print "presentacion:"+presentacion
            print "precio:"+precio

        if len(pr)>1:
            print "tiene mas de una presentacion"
        #No tenemos: tipoventa, via, preciopami
        #id@name@presentacion@laboratorio@tipoventa@droga@accion@precio@via@true@preciopami
       # o.write("%s@%s@%s@%s@-@%s@%s@%s@-@true@-"%(ii.str(),name,
        pc[:]=[]
        pr[:]=[]
        ii=ii+1
        if ii==5:
          exit
    else:
        print "Status Code %d" % status_code
