$(function(){

	// code checks if device is a mobile and changes
	// the footer formatting accordingly

	function checkForMobile() {
		var ua = navigator.userAgent
		var checker = {
			iPhone: ua.match(/(iPhone|iPad)/),
			Android: ua.match(/(Android)/)
		};

		if (checker.android|checker.iPhone) {
			$('.f-resize').css("display","block");
		}
	}

	checkForMobile();

  // code clears search bar when user clicks off
  $(".search").click(function(){
    $(this).removeClass("remove-input")
    $(this).addClass("search-active");

  });
});


$( function() {

    // code for autocomplete on search bar
    $( "#tags" ).autocomplete({
    source: availableTags
    });
} );

