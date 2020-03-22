$(document).ready(function(){
  $('#goRight').on('click', function(){
    $('#slideBox').animate({
      'marginLeft' : '0'
    });
    $('.topLayer').animate({
      'marginLeft' : '100%'
    });
  });
  $('#goLeft').on('click', function(){
    $('#slideBox').animate({
      'marginLeft' : '50%'
    });
    $('.topLayer').animate({
      'marginLeft': '0'
    });
  });

  if(window.location.pathname.indexOf('users/register') > -1) $("#goRight").click()
  else $("#goLeft").click()
});

//window.onload = something();
//
//function something() {
//
//   if ( window.location.pathname.indexOf('users/register')){
//        console.log("retst");
//       document.getElementById('goRight').click();
//   }
//}