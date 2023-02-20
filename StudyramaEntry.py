class StudyramaEntry: 
    def __init__(self,title,name,cleanArrAdress,realAdress,realCC,realCountry,tel,email,):
        self.title = title
        self.name = name
        self.cleanArrAdress = cleanArrAdress
        self.realAdress = realAdress
        self.realCC = realCC
        self.realCountry = realCountry
        self.tel = tel
        self.email = email  
          
    def get(self):
        return  {
                "title": self.title,
                "name": self.name,
                "adress": self.cleanArrAdress,
                "realAdress": self.realAdress,
                "departement": self.realCC,
                "country": self.realCountry,
                "tel": self.tel,
                "email": self.email
            }

   