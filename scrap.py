# ensure you have Python (3  or latest)
# ensure you have pip installer
import requests 
from bs4 import BeautifulSoup 

# L'url du site que je souhaite Scraper
baseUrl = 'https://www.studyrama.com'
uri = "/formations/annuaire-des-formations?btnRechercherFormations=rechercher&metier=20039043"

#Instanciation de mon proxy
response = requests.get(baseUrl + uri )



#fonction qui permet de "crawler" sur mon site et recuperer tous les liens sur la page visée
def process(swoup):
    #ATTENTION, la suite de cette fonction ne marche que pour mon site, c'est un exemple
    #l'exercice etant de refaire une fonction pour VOTRE site a scraper
    ul = swoup.find('ul', { "class": "trackingContainer"})
    lis = ul.findAll('li')
    for li in lis:
        a = li.find('a')
        try:
            print(baseUrl + a['href'])
            requests.get(baseUrl + a['href'])
        except:
            pass  

#si mon site renvoie un code HTTP 200 (OK)
if response.ok:
    #je passe le contenue html de ma page dans un "parser"
    swoupGang = BeautifulSoup(response.text,'html.parser')
    # execute mon parser dessus pour récuperer mes liens
  