// List with inputs from Filter section
var filterList = ['cod_reper_text', 'reper_text', 'furnizor_text', 'proiect_text', 'obiect_text']

var urlExtract;

// Clear button action
$("#clear").click(function(){

  console.log('OrderHelper-Search: Clear action - refresh page');

  var url = '/search/none/none/none/none/none';
  $(location).attr('href', url );
});

// Search button action
$("#search").click(function(){

  console.log('OrderHelper-Search: Search action - retrieve results');

  var filterMap = new Map();
   
  for (var filter in filterList) {
    filterMap.set(filterList[filter],'none');
  }

  $.each($("input[name='filter']:checked"), function(){  
    var ref = $(this).attr('ref');
    var refId = '#'+ref;  
    if ($(refId).val().length > 0) {
      filterMap.set(ref,$(refId).val())
    } 
  });

  var url = '/search/' + filterMap.get('cod_reper_text') + '/' + filterMap.get('reper_text') + '/' + filterMap.get('furnizor_text') + '/' + filterMap.get('proiect_text') + '/' + filterMap.get('obiect_text');
    $(location).attr('href', url );
});


// Populate inputs after retrieving the results
$(document).ready(function(){

  console.log('OrderHelper-Search: Populate inputs');

  var urlList = window.location.pathname.split( '/' );
  urlList.shift(); urlList.shift();

  var filterMap = new Map();
  for (var pos in filterList) {
    filterMap.set(filterList[pos],urlList[pos]);
  }
  
  $.each($("input[name='filter']"), function(){  
    var ref = $(this).attr('ref');
    var refId = '#'+ref;  
    if(filterMap.get(ref) != 'none') {
      $(refId).val(filterMap.get(ref)); 
      $(this).prop('checked', true);
    }
  });
});

// Get the url to trigger the modal
$(".actionViewSubcomanda").click(function () {
  console.log('OrderHelper-Search: view suborder details. ');
  urlExtract = $(this).attr("href");
});


$('.actionViewDetailComanda').click(function(){
  
  console.log('OrderHelper-Search: view parent order details. ');
  var pk = $(this).attr('pk');
    urlExtract = '/comanda/detail/' + pk;
   

});