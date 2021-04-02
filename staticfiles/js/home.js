$(function(){
    $(".name-text").hide();
    $(".report-text").hide();
	$(".loved-it-text").hide();
	$(".loved-it-counter").hide();
	$(".hated-it-text").hide();
	$(".hated-it-counter").hide();
    $(".name").mouseover(function(){
        $(".name-text").show();
        $(".report-text").show();
		$(".loved-it-text").show();
		$(".loved-it-counter").show();
		$(".hated-it-text").show();
		$(".hated-it-counter").show();
       
	});
    $(".name").mouseout(function(){
        $(".name-text").hide();
        $(".report-text").hide();
		$(".loved-it-text").hide();
		$(".loved-it-counter").hide();
		$(".hated-it-text").hide();
		$(".hated-it-counter").hide();
       
	});
	$(".report").mouseover(function(){
        $(".name-text").show();
        $(".report-text").show();
		$(".loved-it-text").show();
		$(".loved-it-counter").show();
		$(".hated-it-text").show();
		$(".hated-it-counter").show();
       
	});
    $(".report").mouseout(function(){
        $(".name-text").hide();
        $(".report-text").hide();
		$(".loved-it-text").hide();
		$(".loved-it-counter").hide();
		$(".hated-it-text").hide();
		$(".hated-it-counter").hide();
       
	});
	$(".loved-it").mouseover(function(){
        $(".name-text").show();
        $(".report-text").show();
		$(".loved-it-text").show();
		$(".loved-it-counter").show();
		$(".hated-it-text").show();
		$(".hated-it-counter").show();
       
	});
	$(".loved-it").mouseout(function(){
        $(".name-text").hide();
        $(".report-text").hide();
		$(".loved-it-text").hide();
		$(".loved-it-counter").hide();
		$(".hated-it-text").hide();
		$(".hated-it-counter").hide();
       
	})

	$(".hated-it").mouseover(function(){
        $(".name-text").show();
        $(".report-text").show();
		$(".hated-it-text").show();
		$(".hated-it-counter").show();
		$(".loved-it-text").show();
		$(".loved-it-counter").show();
      
	});

	$(".hated-it").mouseout(function(){
        $(".name-text").hide();
        $(".report-text").hide();
		$(".hated-it-text").hide();
		$(".hated-it-counter").hide();
		$(".loved-it-text").hide();
		$(".loved-it-counter").hide();
    
	})
})