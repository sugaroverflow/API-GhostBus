#this is the main function of the Ghost bus API
#uses the urllib2 from python for opening the url
import urllib2
import json


"""Grab ALL data from the MTA Siri API for the B54
Returns the data as a JSON string"""
def _get_all_data():
    #this is the URL for the general request to b54
    url =  'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=9030507a-62c2-4168-825d-ddf477ec1b22&OperatorRef=MTA+NYCT&LineRef=B54'
    response = urllib2.urlopen(url)
    return response.read()

"""Grab specific bus# from the MTA Siri API for the B54
using the SIRI parameter &VehicleRef and returns the data as a JSON string"""
def _get_specific_data(busnum):
    url =  'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=9030507a-62c2-4168-825d-ddf477ec1b22&OperatorRef=MTA+NYCT&LineRef=B54'
    url = url + '&VehicleRef=' + str(busnum)
    response = urllib2.urlopen(url)
    return response.read()

def _closest_bus():
    #find the gps location of the user
    #cross check with the gps locations of all the buses
    #find the closest bus and return the bus#
    return 0000; #meaning not found

"""_get_Lat takes a specific busnum and runs _get_specific_data(busnum)
to find and return the latitude"""
def _get_Lat(busnum):
    _get_specific_data(busnum)
    latitude=json_data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][0]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    return latitude

"""_get_Long takes a specific busnum and runs _get_specific_data(busnum)
to find and return the longitude"""
def _get_Long(busnum):
    _get_specific_data(busnum)
    latitude=json_data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][0]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    return longitude
