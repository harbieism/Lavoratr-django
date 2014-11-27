$(document).ready(function () {
	$('.alert').hide();

	$( "#target" ).submit(function( event ) {
		alert( "Handler for .submit() called." );
		event.preventDefault();
	});
})