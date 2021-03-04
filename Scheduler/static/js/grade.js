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

		
		// console.log("HIII");
		let subject = $('#id_grades_subject')[0].value
		let test = $('#id_create_option')[0].value
		let date = $('#id_date')[0].value
		let scope = $('#id_scope')[0].value
		let grade = $('#id_grade')[0].value
		var csrf_token = $('input[name="csrfmiddlewaretoken"]').val();
		// var tr = document.createElement('tr');
		// var td_grid = document.createElement('td');
		// var td_date = document.createElement('td');
		// var td_scope = document.createElement('td');
		// var td_grade = document.createElement('td');
		// var button = document.createElement('button');
		// button.setAttribute('')
		// td_date.setAttribute('date','row');
		// td_scope.setAttribute('scope','row');
		// td_grade.setAttribute('grade','row');
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
				var new_id = '3';
				var _html = `<tr id="link_${new_id}">
				<td>${date}</td>
				<td>${scope}</td>
				<td>${grade}</td>
			</tr>`.trim();
			var new_node = $(_html);
			$('tbody').first().append(new_node);
				// var grid = $('#table_grid').length+1;
				// td_grid.appendChild(document.createTextNode(grid));
				// td_date.appendChild(document.createTextNode(date));
				// td_scope.appendChild(document.createTextNode(scope));
				// td_grade.appendChild(document.createTextNode(grade));
				// td_grade.appendChild(button);
				// console.log(td_date);
				// tr.appendChild(td_grid);
				// tr.appendChild(td_date);
				// tr.appendChild(td_scope);
				// tr.appendChild(td_grade);
				// $('tbody').append(tr);

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

	  // Event Delete
	  $('.event-delete-button').on('click',function(){
		// var id = ${element.pk};
		var ondeleteEvent = $(this).attr('id');
		var csrf_token = $('input[name="csrfmiddlewaretoken"]').val()
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
			  $('#link_' + ondeleteEvent).remove();
			  console.log('link_'+ondeleteEvent);
			  $('#event-delete-modal').modal('hide');
			},
			error: function(response){
			  console.log("Failed");
			  }
		  });
		});
	  });
}