# 2, 3 и 5 задание
import requests

response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
text = response.text.split('ID')
date = text[0].split()


def currency_rates(code):
    for i in text:
        if code in i:
            return float(i[i.find('<Value>') + 7:i.find('</Value>')].replace(',','.')), date[3][date[3].find('"')+1:date[3].rfind('"')]
print(currency_rates(input()))