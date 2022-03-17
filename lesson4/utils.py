import requests
def currency_rates(currency_code=""):
    if not (currency_code):
        return None
    link = 'http://www.cbr.ru/scripts/XML_daily.asp'
    r = requests.get(link).text.split(currency_code)
    value = r[1].split("</Value>")[0].split("<Value>")[1]
    value = float(value.replace(",", "."))
    date = requests.get(link).headers["Date"]
    return (value, date)