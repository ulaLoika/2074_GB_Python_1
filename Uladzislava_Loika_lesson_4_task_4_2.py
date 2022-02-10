
import requests as req
from re import finditer, findall


def currency_rates(code):
    result_value = 0.0000
    response = (req.get('http://www.cbr.ru/scripts/XML_daily.asp')).text
    currency_dict = {}
    currency_list = response.split('ID=')
    del currency_list[0]
    for element in currency_list:
        exchange_element = element[(element.find('<Value>') + 7):element.find('</Value>')]
        if exchange_element:
            exchange_element = float(exchange_element.replace(',', '.'))
            amendment = int(element[(element.find('<Nominal>') + 9):element.find('</Nominal>')])
            currency_dict[(element[(element.find('<CharCode>') + 10):element.find('</CharCode>')])] = exchange_element / amendment
            result_value = currency_dict.get(code.upper(), None)
    return result_value


print(currency_rates('USD'))
