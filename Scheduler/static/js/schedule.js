

// add event AJAX
$("form#event_create_form").submit(function(e){
  e.preventDefault();

  var subject = $(this)[0][1].value
  var description = $(this)[0][2].value
  var start_time = $(this)[0][3].value
  var clock = Number($(this)[0][4].value)
  
  var csrf_token = $('input[name="csrfmiddlewaretoken"]').val()
  
  console.log("Start");

  $.ajax({
    type: 'POST',
    url: $("form#event_create_form").data('url'),
    data: {
      'subject': subject,
      'description': description,
      'start_time': start_time,
      'clock': clock,
      'csrfmiddlewaretoken': csrf_token,
    },
    success: function(response){
      console.log("Success");
      $("form#event_create_form")[0].reset();
      $('#create_event_modal').modal('hide')
    },
    error: function(response){
      console.log("Failed");
    }
  });
});


// calendar slide
{
  var current_slide = $('.flex-container.active');
  let slide_list = $('.flex-container');
  let index = 0;


  $(current_slide).on('swipeleft', swipeleftHandler);
  $(current_slide).on('swiperight', swiperightHandler)

  function swipeleftHandler( event ){
    console.log("left")
    let next_slide = current_slide.next();
    console.log(next_slide);
    next_slide.addClass('active');
    current_slide.removeClass('active');
    $(current_slide).off('swipeleft', swipeleftHandler);
    $(current_slide).off('swiperight', swiperightHandler);
    current_slide = next_slide;
    $(current_slide).on('swipeleft', swipeleftHandler);
    $(current_slide).on('swiperight', swiperightHandler);
  }

  function swiperightHandler( event ){
    console.log("right")
    let prev_slide = current_slide.prev();
    console.log(prev_slide);
    prev_slide.addClass('active');
    current_slide.removeClass('active');
    $(current_slide).off('swipeleft', swipeleftHandler);
    $(current_slide).off('swiperight', swiperightHandler);
    current_slide = prev_slide;
    $(current_slide).on('swipeleft', swipeleftHandler);
    $(current_slide).on('swiperight', swiperightHandler);
  }

}


