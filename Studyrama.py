from Toolkit import Toolkit
from StudyramaEntry import StudyramaEntry

class Studyrama:
    def __init__(self, baseUrl,uri, pageUrl, nbPage):
        self.baseUrl = baseUrl 
        self.uri = uri
        self.urls = []
        self.pageUrl = pageUrl
        self.nbPage = nbPage
        self.result = [] 
    def __str__(self):
        return self
        return f"Scraping on : {self.uri}"  




    def setEndpoints(self, soup):
        ul = soup.find('ul', { "class": "trackingContainer"})
        lis = ul.findAll('li')
        links = []
        for li in lis:
            a = li.find('a')
            try: 
                links.append(a['href'])
            except:
                pass
        self.endpoints = links
        self.endpoints =Toolkit.addBaseUrl(self.baseUrl, self.endpoints)

        return self.endpoints


    def getLinks(self):
        for i in range(self.nbPage):
            self.urls.append(self.pageUrl + str(i))
        self.urls =Toolkit.addBaseUrl(self.baseUrl, self.urls)
        return self.urls

    def getInfoByPage(self,soup):
        fiches = []
        contacts = soup.find("div",{"class": "coordonnees"})
        if contacts is not None:
            tabs = contacts.findAll('li', {"class":"accordeon-item"})
            if tabs is not None:
                for contact in tabs:
                    name = Toolkit.tryToCleanOrReturnBlank(contact.find("div", {"class": "accordeon-header"}))
                    coord = contact.find("div", {"class": "accordeon-body"})
                    adress = coord.find("p")
                    tel = Toolkit.tryToCleanOrReturnBlank(coord.find("a", {"class": "tel"}))
                    email = Toolkit.tryToCleanOrReturnBlank(coord.find("a", {"class": "email"}))
                    title = Toolkit.tryToCleanOrReturnBlank(soup.find("title"))

                    try:
                        adress = adress.getText()
                        cleanArrAdress = []
                        for ele in str(adress).split("\n"):
                            # cleanAdress.push(ele)
                            if ele.strip() != "":
                                cleanArrAdress.append(ele.strip())
                        
                        realAdress = cleanArrAdress[0]
                        realCC = cleanArrAdress[1]
                        realCountry = cleanArrAdress[2]
                    except:
                        adress= ""
                        realAdress= ""
                        realCC= ""
                        realCountry= ""
                        cleanArrAdress = []
            
                
                    # adress = [item.strip() for item in adress if str(item)]
                    # fiche = {
                    #     "title": title.replace('- Studyrama', ""),
                    #     "name": name,
                    #     "adress": " ".join(cleanArrAdress),
                    #     "realAdress": realAdress,
                    #     "departement": realCC,
                    #     "country": realCountry,
                    #     "tel": tel,
                    #     "email": email
                    # }
                    fiche = StudyramaEntry(title.replace('- Studyrama', ""), name, " ".join(cleanArrAdress), realAdress, realCC, realCountry, tel, email)
                    fiches.append(fiche)
        self.result.extend(fiches)
        return fiches

    def getResult(self):
        return self.result

    def getParsedResult(self):
        parsedResult = []
        for res in self.result:
            parsedResult.append(res.get())

        print(parsedResult)
        return parsedResult    
    def getEndpoints(self):
        return self.endpoints