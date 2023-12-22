from data import *


def get_country_info(country_code: str, xml: str):
    country_info_xml = get_country_xml_with_attribute_replace(country_code, xml)
    response_capital_info = get_response(capital_city_country_url, country_info_xml, headers)
    country_info_souped = BeautifulSoup(response_capital_info.text, "lxml")

    return country_info_souped.text.strip()


response_countries_list = get_response(countries_list_url, countries_list_main_xml, headers)
countries_list_souped = BeautifulSoup(response_countries_list.text, "lxml")

codes_list = countries_list_souped.find_all("m:sisocode")
country_list = countries_list_souped.find_all("m:sname")

assert len(codes_list) == len(country_list)

country_dictionary = {}

for key, value in zip(codes_list, country_list):
    country_dictionary.setdefault(key.text, []).append(f"Name: {value.text}")

for key in country_dictionary.keys():
    country_dictionary[key].append(f'Capital: {get_country_info(key, capital_city_main_xml)}')
    country_dictionary[key].append(f'Currency: {get_country_info(key, country_currency_main_xml)}')
    country_dictionary[key].append(f'Flag: {get_country_info(key, country_flag_main_xml)}')
    country_dictionary[key].append(f'Phone code: {get_country_info(key, international_phone_code_main_xml)}')

    print(key, country_dictionary[key])
