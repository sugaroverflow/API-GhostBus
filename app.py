
import urllib2
import json
response = urllib2.urlopen('http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=9030507a-62c2-4168-825d-ddf477ec1b22&OperatorRef=MTA+NYCT&LineRef=B54&VehicleRef=4105')
html = response.read()
h = json.loads(html)
print h['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']['MonitoredVehicleJourney'][0]['VehicleLocation']
