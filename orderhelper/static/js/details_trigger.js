 var urlExtract;
 
$(".actionViewSubcomanda").click(function () {
	console.log('OrderHelper-History: Launch suborder details.')
    urlExtract = $(this).attr("href");
});

$(".actionViewComanda").click(function () {
	console.log('OrderHelper-History: Launch order details.')
    urlExtract = $(this).attr("href");
});
