console.log("abc")

$("form#event_event_form").submit(function(e){
  e.preventDefault();

  var subject = $(this)[0][1].value
  var description = $(this)[0][2].value
  var start_time = $(this)[0][3].value
  var clock = Number($(this)[0][4].value)
  
  var csrf_token = $('input[name="csrfmiddlewaretoken"]').val()
  
  console.log("Start");
  console.log(subject);
  
  $.ajax({
    type: 'POST',
    url: $("form#event_event_form").data('url'),
    data: {
      'subject': subject,
      'description': description,
      'start_time': start_time,
      'clock': clock,
      'csrfmiddlewaretoken': csrf_token,
    },
    datatype: 'json',
    success: function(response){
      console.log("Success");
      $("#event_create_form")[0].trigger('reset');
    },
    error: function(response){
      console.log("Failed");
    }
  });
});
