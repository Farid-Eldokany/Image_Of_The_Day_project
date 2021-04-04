$(function(){

	// hides image information

   	$('.showcaseImage').children().children().not(":nth-child(6)").hide();

	// code for text over displayed image fading out
	// and back in on users mouse over and out
    $(".showcaseImage").on('mouseover', function(){
    	$(this).children().children().not(":nth-child(6)").show();
    })

    $(".showcaseImage").on('mouseout', function(){
    	$(this).children().children().not(":nth-child(6)").hide();
    })
})
