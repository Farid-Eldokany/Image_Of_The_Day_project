$(function(){
    $(".displayed-image").mouseover(function(){
        $(".name").fadeOut();
       
	});
    $(".displayed-image").mouseout(function(){
        $(".name").fadeIn();
	});
})