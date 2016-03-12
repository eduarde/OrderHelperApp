 var urlExtract;
 
$(".actionViewSubcomanda").click(function () {
	console.log('OrderHelper: Launch suborder details.')
    urlExtract = $(this).attr("href");
});

$(".actionViewComanda").click(function () {
	console.log('OrderHelper: Launch order details.')
    urlExtract = $(this).attr("href");
});
