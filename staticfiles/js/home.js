$(function(){

	// code for text over displayed image fading out
	// and back in on users mouse over and out
    $(".displayed-image").mouseover(function(){
        $(".name").fadeOut();

	});
    $(".displayed-image").mouseout(function(){
        $(".name").fadeIn();
	});
})