var urlExtract;

// Get the url for Add action
$(".actionAdd").click(function () {
	urlExtract = $(this).attr("href");
});

// Get the url for checked to EDIT
$(document).ready(function(){
	
	// Get the checkboxes
	$( "input" ).on( "click", function() {
		urlExtract = $( "input:checked" ).attr('url');
	    $("#edit").removeClass('disabled')
	       
	    if ( $( "input:checked" ).length > 1 || $( "input:checked" ).length == 0 ) {
	    	$("#edit").addClass('disabled')	
	    }	
	});
});