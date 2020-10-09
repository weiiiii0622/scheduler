{
	function prompt_test() {
		var csrf_token = $('input[name="csrfmiddlewaretoken"]').val()
		var test = prompt("考試類型：");

		$.ajax({
			
			type: 'POST',
			url: '/grades_ajax/',
			data: {
				'test_type': test,
				'csrfmiddlewaretoken': csrf_token,
			},
			success: function(response){
				console.log("Success");
				var select = document.getElementById('id_create_option');
				var option = document.createElement('option');

				// create text node to add to option element (opt)
				option.appendChild(document.createTextNode(test));

				// set value property of opt
				option.value = (test);

				// add opt to end of select box (sel)
				select.appendChild(option); 
				console.log("success");
				
			},
			error: function(response){
				console.log("Failed");
			}
		});
	}
}