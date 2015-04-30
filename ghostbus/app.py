#currently this app.py file runs the URL to find the location
#of the bus_num specified (hardcoded)

#this is the main function of the Ghost bus API
#uses the urllib2 from python for opening the url
import urllib2
import json


num_bus = 9383;

#this is the URL for the general request to b54
url = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=9030507a-62c2-4168-825d-ddf477ec1b22&OperatorRef=MTA+NYCT&LineRef=B54'
#this adds the specific bus # to the url
url = url + '&VehicleRef' + str(num_bus);

# print 'url' + str(url); #test printing the URL

#handling the http get request
response = urllib2.urlopen(url)
data = response.read()
json_data = json.loads(data)

print "===================================================" #testing
print "This route gives you the latitude and longitude" #testing
print "===================================================" #testing
print "B54 Bus #: " + str(num_bus); #testing


#we need only the lat-long values
#using the python hash:
latitude =json_data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][0]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']

print 'Latitude: ' + str(latitude) #testing

longitude = json_data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][0]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']

print 'Longitude ' + str(longitude) #testing
