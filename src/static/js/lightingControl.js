function getLightingStatus() {
  var lightingStatus = $('#lightingStatus');
  var request = new XMLHttpRequest();
  request.onreadystatechange = function() {
    if (request.readyState == 4 && request.status == 200) {
      lightingStatus.text("Lighting status: " + request.responseText)
    }
  }
  //var url = lightingStatus.data('url');
  request.open("GET", LIGHTING_STATUS_URI, true);
  request.send();
}

function setLightingStatus() {
  var inputField = $('#syncInput');
  var state = inputField.val();
  inputField.val("");

  var request = new XMLHttpRequest();
  request.onreadystatechange = function() {
    if (request.readyState == 4 && request.status == 200) {
      getLightingStatus();
    }
  }
  request.open("GET", LIGHTING_SYNC_URI + state, true);
  request.send();

}

function onLightingClick(state) {
  var request = new XMLHttpRequest();
  request.onreadystatechange = function() {
    if (request.readyState == 4 && request.status == 200) {
      $("button[type=submit]").button('reset');
      alert('done');
      getLightingStatus();
    }
  }
  request.open("GET", LIGHTING_SET_URI + state, true);
  request.send();
}


var LIGHTING_STATUS_URI = "/lighting";
var LIGHTING_SET_URI = "/lighting/";
var LIGHTING_SYNC_URI = "/lighting/sync/";

// Get and show lighting status on page load
getLightingStatus();
