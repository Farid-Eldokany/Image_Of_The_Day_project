$(document).ready(function() {

	// code for showing the image in more detail
	// when clicked on

	$(".image-preview").hide();
	$(".showcaseImage").click(function(){
		$(".image-preview").show();
	})

	$(document).click(function(){
    	var $target = $(event.target);
    	if(!$target.closest(".showcaseImage").length){
			$(".image-preview").hide();
		}
    });
  });

