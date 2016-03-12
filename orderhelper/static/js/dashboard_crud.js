var urlExtract;

// Get the url for Add action
$(".actionAdd").click(function () {
	console.log('OrderHelper-Dashboard: Add object.')
	urlExtract = $(this).attr("href");
});

// Get the url for checked to EDIT
$(document).ready(function(){
	
	console.log('OrderHelper-Dashboard: Edit object.')
	// Get the checkboxes
	$( "input" ).on( "click", function() {

		urlExtract = $( "input:checked" ).attr('url');
	    $("#edit").removeClass('disabled')
	       
	    if ( $( "input:checked" ).length > 1 || $( "input:checked" ).length == 0 ) {
	    	$("#edit").addClass('disabled')	
	    }	
	});
});