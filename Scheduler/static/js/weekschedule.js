
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

// calendar



// calendar slide initialize
{
  Date.prototype.addDays = function(days) {
    this.setDate(this.getDate() + days);
    return this;
  }

  const today = new Date();
  var today_forward = new Date();
  var today_backward = new Date();
  
  var current_sunday = new Date(today.setDate(today.getDate() - today.getDay()));
  var prev_sunday = new Date(today.setDate(current_sunday.getDate() - 7));
  var next_sunday = new Date(today.setDate(current_sunday.getDate() + 7));
  var next_next_sunday = new Date(today.setDate(current_sunday.getDate() + 14));
  var prev_prev_sunday = new Date(today.setDate(today.getDate() - today.getDay() - 28));

  var swiper = new Swiper('.swiper-container', {
    initialSlide: 1,
  });

  swiper.on('reachEnd', function(){
    swiper.appendSlide(
      `<div class="swiper-slide">

        <div class="flex-container">
        <div class="round-button 0">${next_next_sunday.getMonth()+1}/${next_next_sunday.getDate()}</div>
        <div class="round-button 1">${next_next_sunday.getMonth()+1}/${next_next_sunday.getDate()+1}</div>
        <div class="round-button 2">${next_next_sunday.getMonth()+1}/${next_next_sunday.getDate()+2}</div>
        <div class="round-button 3">${next_next_sunday.getMonth()+1}/${next_next_sunday.getDate()+3}</div>
        <div class="round-button 4">${next_next_sunday.getMonth()+1}/${next_next_sunday.getDate()+4}</div>
        <div class="round-button 5">${next_next_sunday.getMonth()+1}/${next_next_sunday.getDate()+5}</div>
        <div class="round-button 6">${next_next_sunday.getMonth()+1}/${next_next_sunday.getDate()+6}</div>
        </div>

  </div>`);
    next_next_sunday.setDate(next_next_sunday.getDate() + 7);
  });

  swiper.on('reachBeginning', function(){
    swiper.prependSlide(
      `<div class="swiper-slide">

        <div class="flex-container">
          <div class="round-button 0">${prev_prev_sunday.getMonth()+1}/${prev_prev_sunday.getDate()}</div>
          <div class="round-button 1">${prev_prev_sunday.getMonth()+1}/${prev_prev_sunday.getDate()+1}</div>
          <div class="round-button 2">${prev_prev_sunday.getMonth()+1}/${prev_prev_sunday.getDate()+2}</div>
          <div class="round-button 3">${prev_prev_sunday.getMonth()+1}/${prev_prev_sunday.getDate()+3}</div>
          <div class="round-button 4">${prev_prev_sunday.getMonth()+1}/${prev_prev_sunday.getDate()+4}</div>
          <div class="round-button 5">${prev_prev_sunday.getMonth()+1}/${prev_prev_sunday.getDate()+5}</div>
          <div class="round-button 6">${prev_prev_sunday.getMonth()+1}/${prev_prev_sunday.getDate()+6}</div>
        </div>

  </div>`);
  prev_prev_sunday.setDate(prev_prev_sunday.getDate() - 7);
  swiper.slideTo(1, 0, false);
  myswiper.slidePrev();
  });

  for (let i = 0; i < 7; i++) {
    $(`div.flex-container.0 > div.round-button.${prev_sunday.getDay()}`).text(`${prev_sunday.getMonth()+1}/${prev_sunday.getDate()}`);
    prev_sunday.setDate(prev_sunday.getDate() + 1);
    $(`div.flex-container.1 > div.round-button.${current_sunday.getDay()}`).text(`${current_sunday.getMonth()+1}/${current_sunday.getDate()}`);
    current_sunday.setDate(current_sunday.getDate() + 1);
    $(`div.flex-container.2 > div.round-button.${next_sunday.getDay()}`).text(`${next_sunday.getMonth()+1}/${next_sunday.getDate()}`);
    next_sunday.setDate(next_sunday.getDate() + 1);
  }

  

}




