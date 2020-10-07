// Popup Modal

  $(".year_href").on('click',function (e) {
    var x = $(this);
    e.preventDefault();
    $('#exam_setting_modal').modal('show');
    $("form#exam_setting_form").submit(function(e){
      e.preventDefault();
  
      number = $('input[name="number"]:checked').val();
      console.log(number);
      
      $.ajax({
        type: 'GET',
        url: $("form#exam_setting_form").data('url'),
        data: {
          'number': number,
        },
        success: function(response){
          console.log("Success");
          $('#exam_setting_modal').modal('hide');
          console.log(x.attr('href'));
          window.location.href = x.attr('href');
        },
        error: function(response){
          console.log("Failed");
        },
      });
    });
  });




// Initialize Swiper
{
  var swiper = new Swiper('.swiper-container', {
    pagination: {
      el: '.swiper-pagination',
      type: 'progressbar',
    },
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
  });
}


// Check answer AJAX
{
  $("#answer_submit_button").on('click', function(){
    $("input[type='radio']").submit(function (e) { 
      e.preventDefault();
      
    });
  });





}