function deactivateCarousel() {
  var items = $('#navCarousel .item');
  for (var i = 0; i < items.length; i++) {
    $('#' + items[i].id).removeClass('active');
  }
}

function getNavCarousel() {
  return $('#navCarousel');
}

function getActiveCarousel() {
  return $('.item.active');
}


function loadCarousel(targetCarousel) {
  var index = targetCarousel.index();

  // Load carousel item
  targetCarousel.load(targetCarousel.data('url'), function(result) {
    getNavCarousel().carousel(index);
    getNavCarousel().carousel('pause');
    targetCarousel.addClass('active');
  });
}

$('#lighting').click(function() {
  loadLightingCarousel();
});

$('#aircon').click(function() {
  loadAirconCarousel();
});

$('#presence').click(function() {
  loadPresenceCarousel();
});

function loadLightingCarousel() {
  // Only switch carousel if clicked is not the currently active item
  var active = getActiveCarousel();
  var lightingCarousel = $('#lightingCarousel');
  if (active.length == 0 || active[0].id != lightingCarousel[0].id) {
    // Remove all displayed carousel items
    deactivateCarousel();
    loadCarousel(lightingCarousel);
  }
}

function loadAirconCarousel() {
  // Only switch carousel if clicked is not the currently active item
  var active = getActiveCarousel();
  var airconCarousel = $('#airconCarousel');
  if (active.length == 0 || active[0].id != airconCarousel[0].id) {
    // Remove all displayed carousel items
    deactivateCarousel();
    loadCarousel(airconCarousel);
  }
}

function loadPresenceCarousel() {
  // Only switch carousel if clicked is not the currently active item
  var active = getActiveCarousel();
  var presenceCarousel = $('#presenceCarousel');
  if (active.length == 0 || active[0].id != presenceCarousel[0].id) {
    // Remove all displayed carousel items
    deactivateCarousel();
    loadCarousel(presenceCarousel);
  }
}

