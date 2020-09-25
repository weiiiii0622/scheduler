

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
  Date.prototype.addDays = function(days) {
    this.setDate(this.getDate() + days);
    return this;
  }

  var today = new Date();

  var swiper = new Swiper('.swiper-container', {
    initialSlide: 1,
  });

  swiper.on('reachEnd', function(){
    swiper.appendSlide(`<div class="swiper-slide"><div class="flex-container"><div class="round-button">${today.getMonth()+1}/${today.getDate()}</div><div class="round-button">${today.addDays(+1).getMonth()+1}/${today.getDate()}</div><div class="round-button">${today.addDays(+1).getMonth()+1}/${today.getDate()}</div><div class="round-button">${today.addDays(+1).getMonth()+1}/${today.getDate()}</div><div class="round-button">${today.addDays(+1).getMonth()+1}/${today.getDate()}</div><div class="round-button">${today.addDays(+1).getMonth()+1}/${today.getDate()}</div><div class="round-button">${today.addDays(+1).getMonth()+1}/${today.getDate()}</div></div></div>`);
  });
  swiper.on('reachBeginning', function(){
    swiper.prependSlide(`<div class="swiper-slide"><div class="flex-container"><div class="round-button">${today.addDays(-7).getMonth()+1}/${today.getDate()}</div><div class="round-button">${today.addDays(-6).getMonth()+1}/${today.getDate()}</div><div class="round-button">${today.getMonth(-5)+1}/${today.getDate()}</div><div class="round-button">${today.getMonth(-4)+1}/${today.getDate()}</div><div class="round-button">${today.getMonth(-3)+1}/${today.getDate()}</div><div class="round-button">${today.getMonth(-2)+1}/${today.getDate()}</div><div class="round-button">${today.getMonth(-1)+1}/${today.getDate()}</div></div></div>`);
  });
}

// {
//   var current_slide = $('.flex-container.active');
//   let slide_list = $('.flex-container');
//   let index = 0;


//   $(current_slide).on('swipeleft', swipeleftHandler);
//   $(current_slide).on('swiperight', swiperightHandler)

//   function swipeleftHandler( event ){
//     console.log("left")
//     let next_slide = current_slide.next();
//     console.log(next_slide);
//     next_slide.addClass('active');
//     current_slide.removeClass('active');
//     $(current_slide).off('swipeleft', swipeleftHandler);
//     $(current_slide).off('swiperight', swiperightHandler);
//     current_slide = next_slide;
//     $(current_slide).on('swipeleft', swipeleftHandler);
//     $(current_slide).on('swiperight', swiperightHandler);
//   }

//   function swiperightHandler( event ){
//     console.log("right")
//     let prev_slide = current_slide.prev();
//     console.log(prev_slide);
//     prev_slide.addClass('active');
//     current_slide.removeClass('active');
//     $(current_slide).off('swipeleft', swipeleftHandler);
//     $(current_slide).off('swiperight', swiperightHandler);
//     current_slide = prev_slide;
//     $(current_slide).on('swipeleft', swipeleftHandler);
//     $(current_slide).on('swiperight', swiperightHandler);
//   }

// }


