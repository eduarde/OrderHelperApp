
// Used to launch the modal dialog via ajax
$('#modalEdit').on('show.bs.modal', function (event) {

  console.log('OrderHelper: Launching modal dialog.')

  var modal = $(this);  
  $.ajax({
    url: urlView,
    context: document.body
  }).done(function(response) {
    modal.html(response);
  });
})

$('body').on('hidden.bs.modal', '.modal', function () {
  $(this).removeData('bs.modal');
});