# Countries
import re
import requests
from bs4 import BeautifulSoup


def get_response(service_url: str, xml_info: str, headers: dict):
    response = requests.request("POST", service_url, headers=headers, data=xml_info)
    return response


def get_country_xml_with_attribute_replace(attribute: str, main_xml: str):
    return main_xml.replace("ATTRIBUTE", attribute)


countries_list_url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"
countries_list_main_xml = """<?xml version="1.0" encoding="utf-8"?>
                        <soap12:Envelope xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
                          <soap12:Body>
                            <ListOfCountryNamesByName xmlns="http://www.oorsprong.org/websamples.countryinfo">
                            </ListOfCountryNamesByName>
                          </soap12:Body>
                        </soap12:Envelope>"""

capital_city_country_url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"
capital_city_main_xml = """<?xml version="1.0" encoding="utf-8"?>
                        <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
                          <soap:Body>
                            <CapitalCity xmlns="http://www.oorsprong.org/websamples.countryinfo">
                              <sCountryISOCode>ATTRIBUTE</sCountryISOCode>
                            </CapitalCity>
                          </soap:Body>
                        </soap:Envelope>"""

country_currency_url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"
country_currency_main_xml = """<?xml version="1.0" encoding="utf-8"?>
                        <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
                          <soap:Body>
                            <CountryCurrency xmlns="http://www.oorsprong.org/websamples.countryinfo">
                              <sCountryISOCode>ATTRIBUTE</sCountryISOCode>
                            </CountryCurrency>
                          </soap:Body>
                        </soap:Envelope>"""

country_flag_url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"
country_flag_main_xml = """<?xml version="1.0" encoding="utf-8"?>
                    <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
                      <soap:Body>
                        <CountryFlag xmlns="http://www.oorsprong.org/websamples.countryinfo">
                          <sCountryISOCode>ATTRIBUTE</sCountryISOCode>
                        </CountryFlag>
                      </soap:Body>
                    </soap:Envelope>"""

international_phone_code_url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"
international_phone_code_main_xml = """<?xml version="1.0" encoding="utf-8"?>
                                <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
                                  <soap:Body>
                                    <CountryIntPhoneCode xmlns="http://www.oorsprong.org/websamples.countryinfo">
                                      <sCountryISOCode>ATTRIBUTE</sCountryISOCode>
                                    </CountryIntPhoneCode>
                                  </soap:Body>
                                </soap:Envelope>"""

headers = {
    'Content-type': "text/xml; charset=utf-8"
}
