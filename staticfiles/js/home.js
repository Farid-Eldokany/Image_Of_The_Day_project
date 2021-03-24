$(function(){
	$(".loved-it-text").hide();
	$(".loved-it-counter").hide();
	$(".hated-it-text").hide();
	$(".hated-it-counter").hide();

	$(".loved-it").mouseover(function(){
		$(".loved-it-text").show();
		$(".loved-it-counter").show();
		$(".hated-it-text").show();
		$(".hated-it-counter").show();
	});

	$(".loved-it").mouseout(function(){
		$(".loved-it-text").hide();
		$(".loved-it-counter").hide();
		$(".hated-it-text").hide();
		$(".hated-it-counter").hide();
	})

	$(".hated-it").mouseover(function(){
		$(".hated-it-text").show();
		$(".hated-it-counter").show();
		$(".loved-it-text").show();
		$(".loved-it-counter").show();
	});

	$(".hated-it").mouseout(function(){
		$(".hated-it-text").hide();
		$(".hated-it-counter").hide();
		$(".loved-it-text").hide();
		$(".loved-it-counter").hide();
	})
})