import os

countries = {}
with open(os.path.join(os.path.dirname(__file__), "country_info.txt"), "r", encoding="utf-8") as countries_file:
    for line in countries_file:
        Country, Capital, CC, CC3, IAC, Timezone, Currency = line.strip().split("|")
        if Country == "Country":
            continue            
        country_dictionnary = {
            "Name": Country,
            "Capital": Capital,
            "CC": CC,
            "CC3": CC3,
            "IAC": IAC,
            "Timezone": Timezone,
            "Currency": Currency
        }
        countries[Country.casefold()] = country_dictionnary
def get_country_capital(country_name):
    country_name = country_name.casefold()
    if country_name in countries:
        return countries[country_name]["Capital"]
    else:
        return "Country not found"
def get_country_currency(country_name):
    country_name = country_name.casefold()
    if country_name in countries:
        return countries[country_name]["Currency"]
    else:
        return "Country not found"
    
def get_country_timezone(country_name):
    country_name = country_name.casefold()
    if country_name in countries:
        return countries[country_name]["Timezone"]
    else:
        return "Country not found"

def get_country_info(country_name):
    country_name = country_name.casefold()
    if country_name in countries:
        return countries[country_name]
    else:
        return "Country not found"
    
if __name__ == "__main__":
    country_name = input("Enter a country name: ")
    print(get_country_capital(country_name))
