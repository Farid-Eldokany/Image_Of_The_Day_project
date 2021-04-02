$(function(){

  $(".search-results").hide();

  // .click works on every browser besides safari change this //



  $(".search").click(function(){
    $(this).removeClass("remove-input")
    $(this).addClass("search-active");

    $(".search-results").slideDown();
  });

  $(document).click(function(){
    var $target = $(event.target);

    if(!$target.closest(".search").length && $(".search").hasClass("search-active")){
        
      if(!$target.closest(".search-results").length) {
        $(".search-results").slideUp();
        $(".search").removeClass("search-active");
        $(".search").addClass("remove-input");

      }
      

    }
  });
});

$( function() {
    $( "#tags" ).autocomplete({
    source: availableTags
    });
} );