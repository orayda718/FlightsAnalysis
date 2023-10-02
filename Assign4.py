# Name: Orayda Shagifa
# CS1026A Assignment 4: Air Travel
# Description: Loads text files representing airports and flights and analyzes the flights
# Due Date: 12.07.2022

from Flight import *
from Airport import *

# list to store Airport objects
allAirports = []
# dictionary to store Flight objects
allFlights = {}


def loadData(airportFile, flightFile):
    # loads data from airport and flight files
    try:
        try:
            # open airports and flights files
            airportsF = open(airportFile, "r", encoding='utf8')
            flightsF = open(flightFile, "r", encoding='utf8')

        except FileNotFoundError:
            # returns false and quits the program if files are not found
            return False, quit()

        for line in airportsF:
            # split line
            airports = line.split(",")
            for x in range(len(airports)):
                # remove whitespace
                airports[x] = airports[x].strip()

            # retrieve variables
            code = airports[0]
            country = airports[1]
            city = airports[2]

            # create airport object
            airport = Airport(code, city, country)

            # add airport object to allAirports list
            allAirports.append(airport)

        for x in allAirports:
            # uses airport code to create keys for allFlights dictionary
            if x.getCode() not in allFlights:
                allFlights[x.getCode()] = []

        for line in flightsF:
            # split line
            flights = line.split(",")
            for x in range(len(flights)):
                # remove whitespace
                flights[x] = flights[x].strip()

            # retrieve variables
            flightNo = flights[0]
            origin = flights[1]
            destination = flights[2]

            # finds corresponding origin airport code to create Airport object
            originObj = ""
            for x in allAirports:
                if x.getCode() == origin:
                    originObj = x

            # finds corresponding destination airport code to create Airport object
            destinationObj = ""
            for x in allAirports:
                if x.getCode() == destination:
                    destinationObj = x

            # create flight object
            flight = Flight(flightNo, originObj, destinationObj)

            for x in allAirports:
                # adds Flight objects to dictionary as values
                if x.getCode() == flight.getOrigin().getCode():
                    allFlights[x.getCode()].append(flight)

        # close airports and flights files
        airportsF.close()
        flightsF.close()

        # True is returned if there are no errors
        return True

    except:
        # False is returned if there is any error
        return False


def getAirportByCode(code):
    # returns Airport object that has the given code
    for x in allAirports:
        if code == x.getCode():
            return x
    # -1 is returned if no Airport is found
    return -1


def findAllCityFlights(city):
    # finds all flights involving given city

    # list to store the flight within given city
    flightsInCity = []
    # variable to store Airport code of given city
    cityCode = ""

    # finds airport code for the given city
    for x in allAirports:
        if city == x.getCity():
            cityCode = x.getCode()

    for x in allFlights:
        # finds flights that have the origin as the given city
        if x == cityCode:
            for i in allFlights[x]:
                flightsInCity.append(i)

        # finds flights that have the destination as the given city
        for i in allFlights[x]:
            if i.getDestination().getCode() == cityCode:
                flightsInCity.append(i)

    # returns list of Flight objects
    return flightsInCity


def findAllCountryFlights(country):
    # finds all flights involving given country

    # list to store flights in given country
    flightsInCountry = []
    # list to store airport codes in given country
    countryCodes = []

    # adds all airport codes in given country to list
    for x in allAirports:
        if country == x.getCountry():
            countryCodes.append(x.getCode())

    for x in allFlights:
        # finds flights that have the origin as the given country
        if x in countryCodes:
            for i in allFlights[x]:
                flightsInCountry.append(i)

        # finds flights that have the destination as the given country
        for i in allFlights[x]:
            if i.getDestination().getCode() in countryCodes:
                flightsInCountry.append(i)

    # returns list of Flight objects
    return flightsInCountry


def findFlightBetween(origAirport, destAirport):
    # finds direct flight from origAirport to destAirport
    # if there is no direct flight, tries to find single-hop flight

    # set to store Airport codes of single-hop flights
    singleHop = set()

    for x in allFlights:
        # finds flights with the same origin airport codes
        if x == origAirport.getCode():
            for i in allFlights[x]:

                # finds flight with the same destination airport code
                if i.getDestination().getCode() == destAirport.getCode():
                    # return statement with airport codes if a direct flight is found
                    return "Direct Flight: " + x + " to " + i.getDestination().getCode()

    for x in allFlights:
        # finds flights with the same origin airport codes
        if x == origAirport.getCode():
            for i in allFlights[x]:
                for y in allFlights:
                    if i.getDestination().getCode() == y:
                        for z in allFlights[y]:
                            # checks if the destination of the single-hop airport is the same as the destination airport
                            if z.getDestination() == destAirport:
                                singleHop.add(z.getOrigin().getCode())

    if len(singleHop) == 0:
        # -1 is return if set is empty
        return -1
    else:
        # set containing single-hop airport codes
        return singleHop


def findReturnFlight(firstFlight):
    # finds a return flight for the given flight object
    for x in allFlights:
        # finds flights that have the same origin airport as the given flight's destination airport
        if x == firstFlight.getDestination().getCode():
            for i in allFlights[x]:
                # finds flights that have the same destination airport as given flight's origin airport
                if i.getDestination() == firstFlight.getOrigin():
                    # returns the flight object
                    return i

    # -1 is returned if no return flight is found
    return -1





