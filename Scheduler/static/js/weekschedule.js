// tomato clock
{
$('#tomato_clock_button').on('click', function(){
  $(this).css('visibility', 'hidden');
  TodayEventswiper.slideTo(0);
  let tomato_clock = setInterval(TomatoClock,1000);
  let timeleft = 20+1+1;
  let clocktime = 10  //sec
  let resttime = 10;  //sec
  function TomatoClock() {
  
    let min = Math.floor(clocktime / 60);
    let sec = clocktime % 60;
    let percent = Math.floor(((10-clocktime)/10)*100);
    let rest_min = Math.floor(resttime / 60);
    let rest_sec = resttime % 60;

    if(clocktime >= 0){
      $('#time').text(percent+'%'+'/'+('0'+min).slice(-2)+':'+('0'+sec).slice(-2));
      clocktime--;
      timeleft--;
    }
    else{
      $('#time').text(('0'+rest_min).slice(-2)+':'+('0'+rest_sec).slice(-2));
      resttime--;
      timeleft--;
    }

    if(percent == 20){
      document.getElementById("tomato_clock_image").src = "/static/image/today/20%.png";
    }
    else if(percent == 40){
      document.getElementById("tomato_clock_image").src = "/static/image/today/40%.png";
    }
    else if(percent == 60){
      document.getElementById("tomato_clock_image").src = "/static/image/today/60%.png";
    }
    else if(percent == 80){
      document.getElementById("tomato_clock_image").src = "/static/image/today/80%.png";
    }
    else if(percent == 100){
      document.getElementById("tomato_clock_image").src = "/static/image/today/100%.png";
    }
    else if (timeleft < 0) {
      clearInterval(tomato_clock);
      $('#tomato_clock_button').css('visibility', 'visible');
      $('#time').empty();
      // window.confirm("Take A Break!");

      // clock completed AJAX
      let target_event= document.getElementsByClassName("swiper-slide-active")[0].id;

      $.ajax({
        type: 'GET',
        url: $("div#tomato_clock").data('url'),
        data: {
          'target_event_id': target_event,
          'status': 'Done',
        },
        success: function(response){
          TodayEventswiper.slideNext();
          TodayEventswiper.removeSlide(0);
          console.log("Success");
        },
        error: function(response){
          console.log("Failed");
        }
      });



    }
  }
});
}


// add event AJAX
{
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
        $(".error").empty();
        $('#create_event_modal').modal('hide')
      },
      error: function(response){
        $('#create_event_modal').modal('show');

        let error_array = Object.keys(response.responseJSON.errors);

        error_array.forEach(error => {
          $(`#${error}_error`).text(response.responseJSON.errors[`${error}`]);
        });
        
        console.log("Failed");
      },
    });
  });
}

// calendar event AJAX
{
  $('.swiper-container').on('click', 'div.round-button', function (e) {
    e.preventDefault();

    let year = new Date().getFullYear();
    let month = $(this).text().split('/')[0];
    let date = $(this).text().split('/')[1];
    
    console.log(year, month, date);

    $.ajax({
      type: 'GET',
      url: $("div#weekschedule-swiper").data('url'),
      data: {
        'year': year,
        'month': month,
        'date': date,
      },
      success: function(response){
        console.log("Success");
        console.log(JSON.parse(response.targets)[0].fields);
        var events = JSON.parse(response.targets);
        $('#event_table').empty();
        $('#event_table').append(`
          <tr>
            <th>Time</th>
            <th>Subject</th> 
            <th>Status</th>
          </tr>
        `);
          
        events.forEach(element => {
          $('#event_table').append(`
          <tr id="${element.pk}">
            <th>${element.fields.start_time.slice(11,19)}<br>~<br>${element.fields.end_time.slice(11,19)}</th>
            <th>${element.fields.subject}<br>${element.fields.description}</th> 
            <th>
              ${element.fields.status} 
              <button id="${element.pk}" type="button" class="close event-delete-button" >
              <span aria-hidden="true">&times;</span>
              </button> 
            </th>
          </tr>
        `);
        });

        // Event Delete
        $('.close').on('click',function(){
          var ondeleteEvent = $(this).attr('id');
          $('#event-delete-modal').modal('show');
          $("#confirm-delete-button").on('click', function(){
        
            $.ajax({
              type: 'GET',
              url: $("div#event-delete-modal").data('url'),
              data: {
                'id': ondeleteEvent,
              },
              success: function(response){
                console.log("Success");
                $('tr#'+ondeleteEvent).remove();
                if($('#event_table').children().length == 1){
                  $('#event_table').children().remove();
                };
                $('#event-delete-modal').modal('hide');
              },
              error: function(response){
                console.log("Failed");
                }
            });
          });
        });
      },

      error: function(response){
        $('#event_table').empty();
        console.log("Failed");
      }

    });
  });
}






// calendar slider
{
  Date.prototype.addDays = function(days) {
    this.setDate(this.getDate() + days);
    return this;
  }

  let today = new Date();

  var current_sunday = new Date(today.setDate(today.getDate() - today.getDay()));


  var prev_sunday = new Date(current_sunday.addDays(-7));
  current_sunday = new Date(today.setDate(today.getDate() - today.getDay()));

  var next_sunday = new Date(current_sunday.addDays(+7));
  current_sunday = new Date(today.setDate(today.getDate() - today.getDay()));
  console.log(next_sunday, current_sunday, prev_sunday);

  var WeekScheduleswiper = new Swiper('#weekschedule-swiper', {
    initialSlide: 1,
  });

  WeekScheduleswiper.on('reachEnd', function(){
    let sun = new Date(next_sunday.setDate(next_sunday.getDate()));
    let mon = new Date(next_sunday.setDate(next_sunday.getDate()+1));
    let tue = new Date(next_sunday.setDate(next_sunday.getDate()+1));
    let wed = new Date(next_sunday.setDate(next_sunday.getDate()+1));
    let thu = new Date(next_sunday.setDate(next_sunday.getDate()+1));
    let fri = new Date(next_sunday.setDate(next_sunday.getDate()+1));
    let sat = new Date(next_sunday.setDate(next_sunday.getDate()+1));

    WeekScheduleswiper.appendSlide(
      `<div class="swiper-slide" id="weekschedule-slide">

        <div class="flex-container">
          <div class="round-button 0">${sun.getMonth()+1}/${sun.getDate()}</div>
          <div class="round-button 1">${mon.getMonth()+1}/${mon.getDate()}</div>
          <div class="round-button 2">${tue.getMonth()+1}/${tue.getDate()}</div>
          <div class="round-button 3">${wed.getMonth()+1}/${wed.getDate()}</div>
          <div class="round-button 4">${thu.getMonth()+1}/${thu.getDate()}</div>
          <div class="round-button 5">${fri.getMonth()+1}/${fri.getDate()}</div>
          <div class="round-button 6">${sat.getMonth()+1}/${sat.getDate()}</div>
        </div>
  </div>`);
    // next_sunday.setDate(next_sunday.getDate() + 1);
  });

  WeekScheduleswiper.on('reachBeginning', function(){
    prev_sunday = new Date(today.setDate(today.getDate() - today.getDay() - 7));

    let sat = new Date(prev_sunday.setDate(prev_sunday.getDate()-1));
    let fri = new Date(prev_sunday.setDate(prev_sunday.getDate()-1));
    let thu = new Date(prev_sunday.setDate(prev_sunday.getDate()-1));
    let wed = new Date(prev_sunday.setDate(prev_sunday.getDate()-1));
    let tue = new Date(prev_sunday.setDate(prev_sunday.getDate()-1));
    let mon = new Date(prev_sunday.setDate(prev_sunday.getDate()-1));
    let sun = new Date(prev_sunday.setDate(prev_sunday.getDate()-1));
    
    WeekScheduleswiper.prependSlide(
      `<div class="swiper-slide" id="weekschedule-slide">

        <div class="flex-container">
          <div class="round-button 0">${sun.getMonth()+1}/${sun.getDate()}</div>
          <div class="round-button 1">${mon.getMonth()+1}/${mon.getDate()}</div>
          <div class="round-button 2">${tue.getMonth()+1}/${tue.getDate()}</div>
          <div class="round-button 3">${wed.getMonth()+1}/${wed.getDate()}</div>
          <div class="round-button 4">${thu.getMonth()+1}/${thu.getDate()}</div>
          <div class="round-button 5">${fri.getMonth()+1}/${fri.getDate()}</div>
          <div class="round-button 6">${sat.getMonth()+1}/${sat.getDate()}</div>
        </div>
  </div>`);
  
  WeekScheduleswiper.slideTo(1, 0, false);
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


// todaypage event swiper
{
var TodayEventswiper = new Swiper('#today-swiper', {
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
});
}










