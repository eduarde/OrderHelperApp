
var urlExtract;

$(".actionAdd").click(function () {
	urlExtract = $(this).attr("href");
});

$(document).ready(function(){

	// Make call to edit 
	$("#edit").click(function(){
		$(location).attr('href', urlExtract );
	});

	// Get the checkboxes
	$( "input" ).on( "click", function() {
		urlExtract = $( "input:checked" ).attr('url');

		$("#edit").removeClass('disabled')
	    if ( $( "input:checked" ).length > 1 || $( "input:checked" ).length == 0 ) {
	    	$("#edit").addClass('disabled')	
	    }	
	});
});