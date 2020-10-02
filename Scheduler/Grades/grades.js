
    $.ajax({
      type: 'POST',
      url: $("form#prompt_input").data('url'),
      data: {
        'csrfmiddlewaretoken': csrf_token,

      },
       //success: function(response){
    //     console.log("Success");
    //     $("form#event_create_form")[0].reset();
    //     $('#create_event_modal').modal('hide')
    //   },
    //   error: function(response){
    //     console.log("Failed");
    //   }
    });

  