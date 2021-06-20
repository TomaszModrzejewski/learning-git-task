class BaseContact:
    def __init__(self, name, surname, private_mail):
       self.name = name
       self.surname = surname
       self.private_mail = private_mail  
    def __str__(self):
        return f"{self.name} {self.surname}: {self.private_mail}"
    
    # @property
    # def label_lenght(self):
    #     return self.label_lenght    
    # @label_lenght.setter
    def fullname(self):
        return len(self.name + ' ' + self.surname)

def fake_data():
    from faker import Faker
    fake = Faker()
    name, surname = fake.name().split()
    return BaseContact(name=name, surname=surname, private_mail=fake.email())

p1 = BaseContact("Alicja", "Walczak", "aa@o2.pl")
p2 = BaseContact("Olga", "Lipińska", "oo@o2.pl")
p3 = BaseContact("Roman","Bratny", "rr@o2.pl")
p4 = BaseContact("Marek","Waszczuk", "mm@o2.pl")
p5 = BaseContact("Bjork", "Johansson", "bb@o2.pl")
people_list = [p1, p2, p3, p4, p5]
people_list.append(fake_data())

class BusinessContact(BaseContact):
    def __init__(self, company, job_title, company_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.company = company
        self.job_title = job_title
        self.company_phone = company_phone
    def contact(self):
        return f"Dzwonię do {self.name} {self.surname} z firmy {self.company} pod numer telefonu: {self.company_phone}"
def fake_data2():
    from faker import Faker
    fake = Faker()
    name, surname = fake.name().split()
    return BusinessContact(name=name, surname=surname, private_mail=fake.email(), company=fake.company(), job_title=fake.job(), company_phone=fake.ssn())
p1 = BusinessContact(name="Alicja", surname="Walczak", private_mail="aa@o2.pl", company="Budimex", job_title="Dyrektor Finansowy", company_phone="+48221231212")
p2 = BusinessContact(name="Olga", surname="Lipińska", private_mail="oo@o2.pl", company="TVP", job_title="Reżyser", company_phone="+48226424242")
p3 = BusinessContact(name="Roman",surname="Bratny", private_mail="rr@o2.pl", company="PGE",job_title="Główny Księgowy", company_phone="+48228832211")
p4 = BusinessContact(name="Marek",surname="Waszczuk", private_mail="mm@o2.pl", company="SztormGrupa",job_title="CEO", company_phone="+48606332211")
p5 = BusinessContact(name="Bjork", surname="Johansson", private_mail="bb@o2.pl", company="IKEA", job_title="Account Manager", company_phone="+4672323456")
people_list = [p1, p2, p3, p4, p5]
people_list.append(fake_data2())
for i in people_list:
    print(i.contact())
print(p3.fullname())
def create_contacts(rodzaj, ilosc):
    if rodzaj == BusinessContact:
        return [fake_data2() for _ in range(ilosc)]
    elif rodzaj == BaseContact:
        return [fake_data() for _ in range(ilosc)]
for contact in create_contacts(BusinessContact, 15):
    print(contact)