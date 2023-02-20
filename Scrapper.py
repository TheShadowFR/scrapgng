import requests 
from bs4 import BeautifulSoup 
from Toolkit import Toolkit

class Scrapper:

    def __init__(self, ScrapInstance, linkFile, finalFile, errorFile):
        self.ScrapInstance = ScrapInstance
        self.linkFile = linkFile
        self.finalFile = finalFile
        self.errorFile = errorFile
        self.linkFileNameFields = ['id', 'category', 'link']
        self.finalFileNameFields = ["title","name","adress", "realAdress", "departement", "country", "tel","email"]
        self.errorFileNameFields = ["id", "link"]



    def exec(self):
        # self.swoupMultiple()
        self.swoupMultiple(self.ScrapInstance.getLinks(), self.ScrapInstance.setEndpoints)
        rows = []
        i = 0
        for url in self.ScrapInstance.getEndpoints():
            print("Writing : " + str(i))
            row = {}
            row['id'] = i
            row['category'] = ""
            row['link'] = url
            rows.append(row)
            i += 1
        
        Toolkit.fileWriter(self.linkFile,self.linkFileNameFields, rows)
        self.swoupMultiple(self.ScrapInstance.getEndpoints(), self.ScrapInstance.getInfoByPage)
        Toolkit.fileWriter(self.finalFile,self.finalFileNameFields, self.ScrapInstance.getParsedResult())
        
        return

    def swoup(self,url, process):
        # Instanciation de mon proxy
        response = requests.get(url)
        # #si mon site renvoie un code HTTP 200 (OK)
        if response.ok:
            #je passe le contenue html de ma page dans un "parser"
            soup = BeautifulSoup(response.text, 'html.parser')
            try:
                #Je retourne l'execution de ma fonction process prenan ma SWOUP SWOUP en parametre
                return process(soup)
            except Exception:
                print("ERROR: Impossible to process ! On :" + str(url))
                return False

        else:
            print("ERROR: Failed Connect on :" + str(url))
            return False
        return 

    def swoupMultiple(self, urls, process):
        result = []
        for url in urls:
            # print(url, process)
            soup = self.swoup(url, process)
            if hasattr(soup, "__len__"):
                result.extend(soup)
            else: 
                result.append(soup)

        return result