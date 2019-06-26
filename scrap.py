import requests
from bs4 import BeautifulSoup as BS

f = open('/home/marcelo/Dropbox/alfabeta/Mayo/test-name.txt', 'r')
for line in f:
    print (repr(line))
   
    URL = ""+line
    #url="http://www.alfabeta.net/precio/tamoxis.html"
    print URL 
    req = requests.get(URL)
    status_code = req.status_code
    print status_code
    if status_code == 200:
        print("OK")
        soup = BS(req.text, 'html.parser')
        entradas = soup.find_all('table', {'class': 'presentacion'})
        for i, entrada in enumerate(entradas):
            presentacion = entrada.find('td', 'tddesc').getText()
            print (presentacion)
    else:
        print "Status Code %d" % status_code
# price = soup.find_all(class_="tdprecio")
#forecast_items = seven_day.find_all(class_="tombstone-container")
#tonight = seven_day[0]
#print(price)
