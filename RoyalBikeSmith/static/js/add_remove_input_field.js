// Add multiple input field for extra attributes and value
$(document).ready(function(){
	var max_fields = 100; // maximum input boxes allowed
	var wrapper = $(".input_fields_wrap");//Fields wrapper
	var add_button = $(".add_field_button"); // Add button Id
   
	
	var counter = 1; //initlal text box count
	$(add_button).click(function(e){ //on add input button click
		e.preventDefault();

		if(counter < max_fields){
			counter++;
			$(wrapper).append('<tr><td class="col-md-2"><input type="text" class="form-control" name="part_number"></td><td class="col-md-2"><input type="text" class="form-control" name="part_name"></td><td class="col-md-2"><input type="number"  class="form-control" name="quantity"></td><td class="col-md-2"><input type="number" pattern="^\d*(\.\d{0,2})?$" class="form-control" name="price"></td><td class="col-md-2"><input type="number" class="form-control" pattern="^\d*(\.\d{0,2})?$" name="total"></td><td class="col-sm-1 text-center"><button class="remove btn btn-danger remove" type="button">Remove</button></td></tr>');
		}

	});

	// jquery button click event to remove a row
	$(document).on('click', 'button.remove', function(){
		$(this).closest('tr').remove();
		counter--;
		return false;
	});
});

