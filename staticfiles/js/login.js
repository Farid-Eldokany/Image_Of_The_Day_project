$(function(){
	$("#signup").click(function(){
  		if ($('#on-signup').hasClass("show")) {
        // Sign the user in
  		} else {
  			$('.on-signup').addClass("show");
      	$('#login').hide();
  		}
  	})
});