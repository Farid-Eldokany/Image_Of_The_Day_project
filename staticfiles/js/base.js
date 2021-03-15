$(function(){

  // .click works on every browser besides safari change this //

  $(".search").click(function(){
    $(this).addClass("search-active");
  });

  $(document).click(function(){
    var $target = $(event.target);
    if(!$target.closest(".search").length && $(".search").hasClass("search-active")){
      $(".search").removeClass("search-active");
    }
  });
});