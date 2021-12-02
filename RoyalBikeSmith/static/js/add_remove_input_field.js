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
			$(wrapper).append('<tr><td class="col-md-2"><input type="text" class="form-control" name="part_number"></td><td class="col-md-2"><input type="text" class="form-control" name="part_name"></td><td class="col-md-2"><input type="number" class="form-control input" id="qty" name="quantity"></td><td class="col-md-2"><input type="number" pattern="^\d*(\.\d{0,2})?$" class="form-control input" id="price" name="price"></td><td class="col-md-2"><input type="number" class="form-control" pattern="^\d*(\.\d{0,2})?$" id="total" name="total"></td><td class="col-sm-1"><button class="remove btn btn-danger remove" type="button">Remove</button></td></tr>');
		}
		

	});

	// jquery button click event to remove a row
	$(document).on('click', 'button.remove', function(){
		$(this).closest('tr').remove();
		counter--;
		return false;
	});
});

//limit number input decimal places to two
$(':input[type="number"]').change(function(){
	this.value = parseFloat(this.value).toFixed(2);
});

// Auto calculation
// $(".input").on('input',function(){

// 	var x = document.getElementById('qty').value;
// 	x = parseFloat(x).toFixed(2);

// 	var y = document.getElementById('price').value;
// 	y = parseFloat(y).toFixed(2);

// 	if(Number.isNaN(x)){
// 		x = 0;
// 	}
// 	else if(Number.isNaN(y)){
// 		y = 0;
// 	}

// 	document.getElementById('total').value = (x * y).toFixed(2);
// });

function getAmount(x){
    var value = $('#qty').val();
    var percent = $('#price').val();
	this.x = 1;
 
     //get the sum of each column of each row
  var sum_value = 0;
  $('.input').each(function(){
    sum_value += +$(this).val();
    $('#total'+x).val(sum_value);
	x++;
  })
  
}