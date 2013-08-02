function getStatusOnOffDiv() {
  return $('#statusOnOff');
}

function getStatusTemperatureDiv() {
  return $('#statusTemperature')
}

function getStatusModeDiv() {
  return $('#statusMode')
}

function getAirconStatus() {
  var request = new XMLHttpRequest();
  request.onreadystatechange = function() {
    if (request.readyState == 4 && request.status == 200) {
      response = JSON.parse(request.responseText);
      getStatusOnOffDiv().text(getStatusOnOffDiv().text() + response["turnOn"]);
      getStatusModeDiv().text(getStatusModeDiv().text() + response["mode"]);
      getStatusTemperatureDiv().text(getStatusTemperatureDiv().text() + response["temperature"]);
    }
  }
  //var url = lightingStatus.data('url');
  request.open("GET", AIRCON_URI, true);
  request.send();
}


var AIRCON_URI = "/aircon";

// Get and show lighting status on page load
getAirconStatus();
