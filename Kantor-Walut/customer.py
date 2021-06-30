import error_codes
import connection


class Customer(object):
    __currencies_dictionary: object
    list_of_currencies = connection.ReadTableOfCurrencies()

    def __init__(self, name, currencies_dictionary):
        self.name = name
        self.__currencies_dictionary = currencies_dictionary

    def payment(self, currency, amount):
        if currency not in self.list_of_currencies:
            return error_codes.CURRENCY_DOES_NOT_EXIST
        if amount < 0:
            return error_codes.NEGATIVE_AMOUNT
        if currency in self.__currencies_dictionary.keys():
            self.__currencies_dictionary[currency] = self.__currencies_dictionary[currency] + amount
        else:
            self.__currencies_dictionary[currency] = amount

    def exchange(self, currency_from, currency_to, amount):
        if currency_from in self.list_of_currencies and currency_to in self.list_of_currencies:
            pass
        else:
            return error_codes.CURRENCY_DOES_NOT_EXIST
        if amount < 0:
            return error_codes.NEGATIVE_AMOUNT
        rate = connection.getRate(currency_from, currency_to)
        if rate == error_codes.CONNECTION_TO_NBP_PROBLEM:
            return error_codes.CONNECTION_TO_NBP_PROBLEM
        if currency_from in self.__currencies_dictionary.keys():
            amount_from = self.__currencies_dictionary[currency_from]
        else:
            amount_from = 0
        if currency_to in self.__currencies_dictionary.keys():
            amount_to = self.__currencies_dictionary[currency_to]
        else:
            amount_to = 0
        if amount_from - amount / rate < 0:
            return error_codes.NOT_ENOUGH_CURRENCY
        self.__currencies_dictionary[currency_from] = amount_from - amount / rate
        self.__currencies_dictionary[currency_to] = amount_to + amount

    def getCurrencies(self):
        str_temp = ""
        for currency in self.__currencies_dictionary.keys():
            str_temp += currency
            str_temp += ": "
            self.__currencies_dictionary[currency] = round(self.__currencies_dictionary[currency], 4)
            str_temp += str(self.__currencies_dictionary[currency])
            str_temp += "\n"
        return str_temp

    @property
    def currencies_dictionary(self):
        return self.__currencies_dictionary
