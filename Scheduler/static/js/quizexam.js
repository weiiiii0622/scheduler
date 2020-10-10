// Popup Modal

  $(".year_href").on('click',function (e) {
    let x = $(this);
    e.preventDefault();
    $('#exam_setting_modal').modal('show');
    $("form#exam_setting_form").submit(function(e){
      e.preventDefault();
  
      number = $('input[name="number"]:checked').val();
      
      $.ajax({
        type: 'GET',
        url: $("form#exam_setting_form").data('url'),
        data: {
          'number': number,
        },
        success: function(response){
          console.log("Success");
          $('#exam_setting_modal').modal('hide');
          window.location.href = x.attr('href') ;
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
    $("form#answer_form").submit(function(e){ 
      e.preventDefault();
      var id_list = [];
      $('.answer').each(function(){
        id_list.push($(this).attr('id'));
      })
      console.log(id_list);
      $.ajax({
        type: 'GET',
        url: $("#answer_submit_button").data('url'),
        traditional: true,
        data: {
          'id': id_list,
        },
        success: function(response){
          console.log("Success");
          
          $('input[name="option"]:checked').each(function(){
            if (response.answer.includes($(this).attr('id'))){
              console.log("Right!");
              $('label[for="'+$(this).attr('id')+'"]').css('color','lime',);
              response.answer.splice(response.answer.indexOf($(this).attr('id')), 1);
            }
            else{
              console.log("Wrong!");
              $('label[for="'+$(this).attr('id')+'"]').css('color','#F40009',);
            }
          });
          response.answer.forEach(element => {
            $('label[for="'+element+'"]').css('color','lime',);
          });
          
          swiper.slideTo(0);
          $("#answer_submit_button").off('click');
          $('#answer_submit_button').text('Quit')
          $('#answer_submit_button').on('click', function(){
            window.location.href = '/QuizBank/';
            return false;
          });
        },
        error: function(response){
          console.log("Failed");
        },
      });


    });
  });





}