# Name: Orayda Shagifa
# CS1026A Assignment 4: Air Travel
# Description: Loads text files representing airports and flights and analyzes the flights
# Due Date: 12.07.2022

from Airport import *


class Flight:
    def __init__(self, flightNo, origin, destination):
        if isinstance(origin, Airport) and isinstance(destination, Airport):
            # checks if origin and destination are Airport objects
            self._flightNo = flightNo
            self._origin = origin
            self._destination = destination
        else:
            # Error if origin and destination are not Airport objects
            raise TypeError("The origin and destination must be Airport objects")

    def __repr__(self):
        if self.isDomesticFlight():
            # domestic if isDomesticFlight is True
            isDom = "domestic"
        else:
            # international if isDomesticFlight is False
            isDom = "international"
        # returns representation of Flight
        return "Flight: " + self._flightNo + " from " + self._origin.getCity() + " to " + self._destination.getCity() + " {" + isDom + "}"

    def __eq__(self, other):
        if not isinstance(other, Flight):
            # checks if other is a flight object
            return False

        if (self._origin.getCity() == other._origin.getCity()) and (self._origin.getCountry() == other._origin.getCountry()) \
                and (self._destination.getCity() == other._destination.getCity()) and (self._destination.getCountry() == other._destination.getCountry()):
            # checks if they are the same flight and returns True if they are
            return True
        else:
            # returns False if they are not the same flight
            return False

    def getFlightNumber(self):
        # gets Flight number
        return self._flightNo

    def getOrigin(self):
        # gets Flight origin
        return self._origin

    def getDestination(self):
        # gets Flight destination
        return self._destination

    def isDomesticFlight(self):
        # checks if Flights are within the same country
        if self._origin.getCountry() == self._destination.getCountry():
            # returns True if domestic
            return True
        else:
            # returns False if international
            return False

    def setOrigin(self, origin):
        # sets the Flight origin
        self._origin = origin

    def setDestination(self, destination):
        # sets the Flight destination
        self._destination = destination


