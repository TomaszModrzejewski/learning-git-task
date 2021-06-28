# import biblioteki zewnętrznej

from faker import Faker
fake = Faker()

# deklaracja klasy BaseContact


class BaseContact:
    def __init__(self, first_name, second_name, email, phone):
        self.first_name = first_name
        self.second_name = second_name
        self.email = email
        self.phone = phone

    @property
    def label_length(self):
        return len(self.first_name), len(self.second_name)

    def __str__(self):
        return f"{self.first_name} {self.second_name}, email: {self.email}, phone: {self.phone}"

    def contact(self):
        return f"Wybieram numer {self.phone} i dzwonię do {self.first_name} {self.second_name}"


# deklaracja klasy BusinessContact


class BusinessContact(BaseContact):
    def __init__(self, position, company, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position
        self.company = company

    def __str__(self):
        return f"{self.first_name} {self.second_name}, company: {self.company}, position: {self.position}, email: {self.email}, phone: {self.phone}"


def create_contacts(card_type, amount):
    cards = []
    for i in range(amount):
        if card_type == "base":
            cards.append(
                BaseContact(
                    first_name=fake.first_name(),
                    second_name=fake.last_name(),
                    phone=fake.phone_number(),
                    email=fake.email(),
                )
            )
        elif card_type == "business":
            cards.append(
                BusinessContact(
                    first_name=fake.first_name(),
                    second_name=fake.last_name(),
                    email=fake.email(),
                    phone=fake.phone_number(),
                    position=fake.job(),
                    company=fake.company(),
                )
            )

    return cards


if __name__ == "__main__":

    print("Generuję zwykłe kontakty")
    base_cards = create_contacts("base", 4)
    for card in base_cards:
        print(card.first_name,
              card.second_name,
              card.email,
              card.phone,
              card.label_length)
        print()
    print(card.contact())

    print("Generuję kontakty biznesowe")
    business_cards = create_contacts("business", 6)
    for card in business_cards:
        print(card.first_name,
              card.second_name,
              card.email,
              card.phone,
              card.position,
              card.company,
              card.label_length)
        print()
    print(card.contact())
