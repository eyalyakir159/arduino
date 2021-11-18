

class client:
    def __init__(self,id,name,email,phone,age,symtoms,syndrom_type) -> None:
        #user enter
        self.id=id
        self.name= name
        self.email=email
        self.phone = phone
        self.age = age
        self.symtoms = symtoms
        self.symtoms=symtoms
        self.syndrom_type=syndrom_type

        #user data
        self.reports = []
        self.schedule =None

        
    def add_reports(self,report):
        self.reports.append(report)

