function getPresence() {
  var presenceList = $('#presenceList'); 
  var request = new XMLHttpRequest();
  request.onreadystatechange = function() {
    if (request.readyState == 4 && request.status == 200) {
      present = JSON.parse(request.responseText);
      if (present.length == 0) {
        presenceList.text("No one is home, or has their registered devices turned on.");
      } else {
        for (i = 0; i < present.length; i++) {
          presenceList.text(presenceList.text() + present[i]);
          if (i < present.length - 1) {
            presenceList.text(presenceList.text() + ", ");
          }
        }
      }
    }
  }
  request.open("GET", PRESENCE_URI, true);
  request.send();
}

var PRESENCE_URI = "/presence";

// Get presence on page load
getPresence();
