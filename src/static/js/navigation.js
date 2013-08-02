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
  // Only switch carousel if clicked is not the currently active item
  var active = getActiveCarousel();
  var lightingCarousel = $('#lightingCarousel');
  if (active.length == 0 || active[0].id != lightingCarousel[0].id) {
    // Remove all displayed carousel items
    deactivateCarousel();
    loadCarousel(lightingCarousel);
//    var index = lightingCarousel.index();

    // Load carousel item
//    lightingCarousel.load(lightingCarousel.data('url'), function(result) {
//      getNavCarousel().carousel(index);
//      getNavCarousel().carousel('pause');
//      lightingCarousel.addClass('active');
//    });
  }
});

$('#aircon').click(function() {
  // Only switch carousel if clicked is not the currently active item
  var active = getActiveCarousel();
  var airconCarousel = $('#airconCarousel');
  if (active.length == 0 || active[0].id != airconCarousel[0].id) {
    // Remove all displayed carousel items
    deactivateCarousel();
    loadCarousel(airconCarousel);
  }
});
