import requests
from bs4 import BeautifulSoup as BS
page = requests.get("http://www.alfabeta.net/precio/lanseka.html")
soup = BS(page.content, 'html.parser')
seven_day = soup.find(id="tdprecio")
#forecast_items = seven_day.find_all(class_="tombstone-container")
#tonight = seven_day[0]
print(seven_day)
