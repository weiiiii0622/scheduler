$('#grades_modal').on('show.bs.modal', function (event) {
	// $('#create_button').button('toggle')
});
{
	function prompt_test() {
		var csrf_token = $('input[name="csrfmiddlewaretoken"]').val()
		let test = prompt("考試類型：");
		
		if(test){
			$.ajax({
				
				type: 'POST',
				url: '/grades/choices_ajax/',
				data: {
				'test_type': test,
				'csrfmiddlewaretoken': csrf_token,
				},
				success: function(response){
				console.log("Success prompt");
				var select = document.getElementById('id_create_option');
				var option = document.createElement('option');
		
				// create text node to add to option element (opt)
				option.appendChild(document.createTextNode(test));
		
				// set value property of opt
				option.value = (test);
		
				// add opt to end of select box (sel)
				select.appendChild(option); 
				
				},
				error: function(response){
				console.log("Failed prompt");
				}
			});
		}
	}
}


{
	$('#create_grade_button').on('click', function(){

		
		console.log("HIII");
		let subject = $('#id_grades_subject')[0].value
		let test = $('#id_create_option')[0].value
		let date = $('#id_date')[0].value
		let scope = $('#id_scope')[0].value
		let grade = $('#id_grade')[0].value
		var csrf_token = $('input[name="csrfmiddlewaretoken"]').val()

		$.ajax({
		
			type: 'POST',
			url: '/grades/creategradeAJAX',
			data: {
				'subject': subject,
				'test': test,
				'date': date,
				'scope': scope,
				'grade': grade,
				'csrfmiddlewaretoken': csrf_token,
			},
			success: function(response){
				$('#id_date').val("");
				$('#id_scope').val("");
				$('#id_grade').val("");
        $('#grades_modal').modal('hide');
				console.log("Success submit");
			},
			error: function(response){
				console.log("Failed submit");
			}
			});

	});





}
{
	// events.forEach(element => {
	// 	$('#grades_table').append(`
	// 	<tr id="${element.pk}">
	// 	  <th>${element.fields.start_time.slice(11,19)}<br>~<br>${element.fields.end_time.slice(11,19)}</th>
	// 	  <th>${element.fields.subject}<br>${element.fields.description}</th> 
	// 	  <th>
	// 		${element.fields.status} 
	// 		<button id="${element.pk}" type="button" class="close event-delete-button" >
	// 		<span aria-hidden="true">&times;</span>
	// 		</button> 
	// 	  </th>
	// 	</tr>
	//   `);
	//   });

	  // Event Delete
	  $('.close').on('click',function(){
		// var id = ${element.pk};
		var ondeleteEvent = $(this).attr('id');
		$('#event-delete-modal').modal('show');
		$("#confirm-delete-button").on('click', function(){
	  
		  $.ajax({
			type: 'POST',
			url: $("div#event-delete-modal").data('url'),
			data: {
			  'id': ondeleteEvent,
			  'csrfmiddlewaretoken': csrf_token,
			},
			success: function(response){
			  console.log("Success");
			  $('tr#'+ondeleteEvent).remove();
			  if($('#grades_table').children().length == 1){
				$('#grades_table').children().remove();
			  };
			  $('#event-delete-modal').modal('hide');
			},
			error: function(response){
			  console.log("Failed");
			  }
		  });
		});
	  });
}