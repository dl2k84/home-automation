function deactivateCarousel() {
  var items = $('#navCarousel .item');
  for (var i = 0; i < items.length; i++) {
    $('#' + items[i].id).removeClass('active');
  }
}

function getNavCarousel() {
  return $('#navCarousel');
}

$('#lighting').click(function() {
  // Only switch carousel if clicked is not the currently active item
  var active = $('.item.active');
  var lightingCarousel = $('#lightingCarousel');
  if (active.length == 0
    || active[0].id != lightingCarousel[0].id) {
    // Remove all displayed carousel items
    deactivateCarousel();
    var index = lightingCarousel.index();

    // Load carousel item
    lightingCarousel.load(lightingCarousel.data('url'), function(result) {
      getNavCarousel().carousel(index);
      getNavCarousel().carousel('pause');
      lightingCarousel.addClass('active');
    });
  }
});
