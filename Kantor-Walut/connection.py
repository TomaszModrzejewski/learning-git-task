import requests
import json
import error_codes
import numpy as np
from xml.etree.ElementTree import parse, Element, SubElement

def getRate(currency_code_from, currency_code_to):
    url_template = "http://api.nbp.pl/api/exchangerates/rates/a/"
    if currency_code_to == "PLN":
        url_template += currency_code_from
        response = requests.get(url_template)
        if response.status_code != 200:
            return error_codes.CONNECTION_TO_NBP_PROBLEM
        else:
            rate = response.json()["rates"][0]["mid"]
            return rate
    else:
        url_template += currency_code_to
        response = requests.get(url_template)
        if response.status_code != 200:
            return error_codes.CONNECTION_TO_NBP_PROBLEM
        else:
            rate = response.json()["rates"][0]["mid"]
            if currency_code_from == "PLN":
                return 1/rate
            else:
                url_template = "http://api.nbp.pl/api/exchangerates/rates/a/"
                url_template += currency_code_from
                response= requests.get(url_template)
                if response.status_code != 200:
                    return error_codes.CONNECTION_TO_NBP_PROBLEM
                else:
                    first_rate = response.json()["rates"][0]["mid"]
                    return first_rate/rate


def generateListOfRatesAndDatesFromURL(url_template):
    rates_list = []
    date_list = []
    response = requests.get(url_template)
    if response.status_code != 200:
        return error_codes.CONNECTION_TO_NBP_PROBLEM, ""
    else:
        rates = response.json()['rates']
        for x in rates:
            rate = x['mid']
            rates_list.append(rate)
            date = x['effectiveDate']
            date_list.append(date)
        return rates_list, date_list


def rateTableFromPLN(currency_code_to, number_of_days):
    if currency_code_to == 'PLN':
        return [1]*number_of_days, 'PLN'
    if (number_of_days < 255):
        url_template = "http://api.nbp.pl/api/exchangerates/rates/a/"
        url_template = url_template + currency_code_to + "/last/" + str(number_of_days)
        return generateListOfRatesAndDatesFromURL(url_template)
    else:
        return error_codes.TO_MANY_DAYS, ""


def getRateTable(currency_code_from, currency_code_to, number_days):
    currency_from_table, dates_table_from = rateTableFromPLN(currency_code_from, number_days)
    currency_to_table, dates_table_to = rateTableFromPLN(currency_code_to, number_days)
    if dates_table_to == 'PLN':
        dates_table_to = dates_table_from
    if dates_table_from == 'PLN':
        dates_table_from = dates_table_to
    if dates_table_to != dates_table_from:
        return error_codes.DATES_DONT_MATCH, ""
    if type(currency_from_table) == int:
        return currency_from_table, ""
    if type(currency_to_table) == int:
        return currency_to_table, ""
    else:
        currency_from_table = np.array(currency_from_table)
        currency_to_table = np.array(currency_to_table)
        return currency_from_table/currency_to_table, dates_table_to


def ReadTableOfCurrencies():
    file = r"tabelaWalut.xml"
    currencies = []
    doc = parse(file)
    root = doc.getroot()
    for pozycja in root.iterfind("pozycja"):
        currency = pozycja.findtext("kod_waluty")
        currencies.append(currency)
    currencies = currencies + ["PLN"]
    return currencies

