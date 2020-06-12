$('document').ready(function(){
    $('body').on("show.bs.collapse", ".qr-collapse", function(event){
      var title = angular.element(event.target).scope().title;
      $(event.target).qrcode({text:'https://brewshop.github.io/BrewShopCTR/list0.json' + title.titleid});
    });
  
    $('body').on("hidden.bs.collapse", ".qr-collapse", function(event){
      $(event.target).empty();
    });
  });