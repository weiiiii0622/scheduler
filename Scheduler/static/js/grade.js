$('#grades_modal').on('show.bs.modal', function (event) {
	// $('#create_button').button('toggle')
});

// 	function prompt_test() {
// 		var csrf_token = $('input[name="csrfmiddlewaretoken"]').val()
// 		var test = prompt("考試類型：");
	
// 		$.ajax({
		  
// 		  type: 'POST',
// 		  url: '/grades_ajax/',
// 		  data: {
// 			'test_type': test,
// 			'csrfmiddlewaretoken': csrf_token,
// 		  },
// 		  success: function(response){
// 			console.log("Success");
// 			var select = document.getElementById('id_create_option');
// 			var option = document.createElement('option');
  
// 			// create text node to add to option element (opt)
// 			option.appendChild(document.createTextNode(test));
  
// 			// set value property of opt
// 			option.value = (test);
  
// 			// add opt to end of select box (sel)
// 			select.appendChild(option); 
// 			console.log("success");
			
// 		  },
// 		  error: function(response){
// 			console.log("Failed");
// 		  }
// 		});
// 	  }
// }


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
        		$('#grades_modal').modal('hide')
				console.log("Success");
			},
			error: function(response){
				console.log("Failed");
			}
			});

	});





}