# ensure you have Python (3  or latest)
# ensure you have pip installer
import requests 
from bs4 import BeautifulSoup 

import csv




# L'url du site que je souhaite Scraper
baseUrl = 'https://www.studyrama.com'
uri = "/formations/annuaire-des-formations?btnRechercherFormations=rechercher&page="

#Genere des liens avec l'argument "page" qui s'incrémente
def getLinks(url, nbPg):
    # initialisation du resultat (vide pour l'instant)
    urls = []
    # Pour chaque page
    for i in range(nbPg):
        # Ajoutes la concatenation de l'url avec l'index au tableau d'urls
        urls.append(url + str(i))
    return urls


#fonction qui permet de "crawler" sur mon site et recuperer tous les liens sur la page visée
def getEndpoints(soup):
    #ATTENTION, la suite de cette fonction ne marche que pour mon site, c'est un exemple
    #l'exercice etant de refaire une fonction pour VOTRE site a scraper
    ul = soup.find('ul', { "class": "trackingContainer"})
    lis = ul.findAll('li')
    links = []
    for li in lis:
        a = li.find('a')
        try: 
            links.append(a['href'])
        except:
            pass
            # print(li)
            # print('ERROR: No link')
    return links

def swoup(url, process):
    #Instanciation de mon proxy
    response = requests.get(url)
    #si mon site renvoie un code HTTP 200 (OK)
    if response.ok:
        #je passe le contenue html de ma page dans un "parser"
        soup = BeautifulSoup(response.text, 'html.parser')
        try:
            #Je retourne l'execution de ma fonction process prenan ma SWOUP SWOUP en parametre
            return process(soup)
        except Exception:
            print("ERROR: Impossible to process ! " )
    else:
        print("ERROR: Failed Connect")
    return 

#concatene mes liens a l'url
def addBaseUrl(baseUrl, urls):
    res = []
    for url in urls:
        res.append(baseUrl + url)
    return res


#Execution
urls = []
for link in getLinks(baseUrl + uri, 1674):
# for link in getLinks(baseUrl + uri, 1):
    print("Checking " + link)
    urls.extend(addBaseUrl(baseUrl, swoup(link, getEndpoints)))
    print("You'got actually :"+ str(len(urls)) + " links !")
        
print(urls, "Pshatek got : " + str(len(urls)) + " links !")


#Lire le fichier
# with open("links.csv", 'r') as file:
#     csvreader = csv.reader(file)
#     for row in csvreader:
#         print(row)


rows = []
i = 0
for url in urls:
    print("Writing : " + str(i))
    row = {}
    row['id'] = i
    row['category'] = ""
    row['link'] = url
    rows.append(row)
    i += 1


fieldnames = ['id', 'category', 'link']
with open('links.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)


print("Done")