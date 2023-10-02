# Name: Orayda Shagifa
# Description: Air Travel, Loads text files representing airports and flights and analyzes the flights
# Date: 12.07.2022

class Airport:
    def __init__(self, code, city, country):
        # initializes variables
        self._code = code
        self._city = city
        self._country = country

    def __repr__(self):
        # returns representation of Airport
        return self._code + " (" + self._city + ", " + self._country + ")"

    def getCode(self):
        # gets Airport code
        return self._code

    def getCity(self):
        # gets Airport city
        return self._city

    def getCountry(self):
        # gets Airport country
        return self._country

    def setCity(self, city):
        # sets Airport city
        self._city = city

    def setCountry(self, country):
        # sets Airport country
        self._country = country


