$(function(){

  // code clears search bar when user clicks off
  $(".search").click(function(){
    $(this).removeClass("remove-input")
    $(this).addClass("search-active");

  });
});


$( function() {

    // code for autocomplete on search bar
    $( "#tags" ).autocomplete({
    source: availableTags
    });
} );