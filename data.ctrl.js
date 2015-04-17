angular.module('app').controller("MainController", function($scope, $http, $httpProvider){

  //GET request:
  $http.get('http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=9030507a-62c2-4168-825d-ddf477ec1b22&OperatorRef=MTA%20NYCT&LineRef=B54&VehicleRef=9531').
    success(function(data) {
      $scope.VehicleRef = data;
    });

});
