# ensure you have Python (3  or latest)
# ensure you have pip installer
import requests 
from bs4 import BeautifulSoup 

import csv
import re
from Studyrama import Studyrama
from Scrapper import Scrapper


instance = Studyrama(
    'https://www.studyrama.com',
    "/formations/annuaire-des-formations?btnRechercherFormations=rechercher&page=",
    "/formations/annuaire-des-formations?btnRechercherFormations=rechercher&page=",
    1
    )

scrapyCoco = Scrapper(instance, 'links.csv', 'contacts.csv','errors.csv')

scrapyCoco.exec()

print("Done")