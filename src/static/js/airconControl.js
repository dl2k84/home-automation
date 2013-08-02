function getStatusOnOffDiv() {
  return $('#statusOnOff');
}

function getStatusTemperatureDiv() {
  return $('#statusTemperature')
}

function getStatusModeDiv() {
  return $('#statusMode')
}

function updateAirconStatus(status) {
  IS_ON = status["turnOn"];
  MODE = status["mode"];
  TEMPERATURE = status["temperature"]
}

function getOnOffSwitch() {
  return $('#onOffSwitch');
}

function getAirconStatus() {
  var request = new XMLHttpRequest();
  request.onreadystatechange = function() {
    if (request.readyState == 4 && request.status == 200) {
      response = JSON.parse(request.responseText);
      updateAirconStatus(response);
      getStatusOnOffDiv().text(IS_ON);
      getStatusModeDiv().text(MODE);
      getStatusTemperatureDiv().text(TEMPERATURE);

      getOnOffSwitch().bootstrapSwitch('setState', IS_ON);
      $('input[name="modeOptions"][data-mode=' + MODE +']', '#modeRadio').click();
      $('input[name="temperatureOptions"][data-temperature=' + TEMPERATURE +']', '#temperatureRadio').click();
    }
  }
  //var url = lightingStatus.data('url');
  request.open("GET", AIRCON_URI, true);
  request.send();
}

function setAircon() {
  var request = new XMLHttpRequest();
  request.onreadystatechange = function() {
    if (request.readyState == 4 && request.status == 200) {
      // TODO hacky way to get new aircon value: unload and reload carousel
      // for some reason, the click() commands above does not work upon
      // request to set aircon. Until I have some time to find out why,
      // will use this hack.
      //getAirconStatus();
      deactivateCarousel();
      loadAirconCarousel();
    }
  }

  json = {}
  json.turnOn = getOnOffSwitch().bootstrapSwitch('status');
  json.mode = $('input[name="modeOptions"]:checked', '#modeRadio').data('mode');
  json.temperature = $('input[name="temperatureOptions"]:checked', '#temperatureRadio').data('temperature');
  request.open("POST", AIRCON_URI, true);
  request.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
  request.send(JSON.stringify(json));
}

var AIRCON_URI = "/aircon";
var IS_ON;
var MODE;
var TEMPERATURE;
// Get and show lighting status on page load
getAirconStatus();
