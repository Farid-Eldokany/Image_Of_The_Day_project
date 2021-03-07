$(function(){



  var imagename = $('.displayed-image').find('img').attr('name');

  // will fix once i have figured out how to get the image name from
  // the currently displayed image
  imagename = "placeholder text";

  $(".image-title-container").children().append(imagename);

  $(".signup").click(function(){
  	if ($('.on-signup').hasClass("show")) {
  		if($('.password-field1').val() === $('.password-field2').val()){
  			alert('you have just signed up');
  		} else {
  			alert('password fields must match');
  		}
  	} else {
  		$('.on-signup').addClass("show");
      $('.login-button').hide();
  	}
  })
});


