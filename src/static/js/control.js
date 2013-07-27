function onLightingClick(state) {
  var request = new XMLHttpRequest();
  request.onreadystatechange = function() {
    if (request.readyState == 4 && request.status == 200) {
      $("button[type=submit]").button('reset');
      alert('done');
    }
  }
  request.open("GET", "/lighting/" + state, true);
  request.send();
}

