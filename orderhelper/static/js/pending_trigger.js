var urlExtract;
	
$(".actionCloseSubcomanda").click(function () {
    console.log('OrderHelper-Pending: Close suborder.')
    urlExtract = $(this).attr("href");
});

$(".actionCancelSubcomanda").click(function () {
    console.log('OrderHelper-Pending: Cancel suborder.')
    urlExtract = $(this).attr("href");
});

$(".actionViewSubcomanda").click(function () {
    console.log('OrderHelper-Pending: Details suborder.')
    urlExtract = $(this).attr("href");
    });

$(".actionCloseComanda").click(function () {

	if ($(this).hasClass('disabled')) {
  		event.stopImmediatePropagation();
        return(false);
  	}

	  console.log('OrderHelper-Pending: Close order.') 
		urlExtract = $(this).attr("href");
 });

$(".actionCancelComanda").click(function () {

	if ($(this).hasClass('disabled')) {
  		event.stopImmediatePropagation();
        return(false);
  	}

	console.log('OrderHelper-Pending: Cancel order.') 
	urlExtract = $(this).attr("href");
});

$(".actionViewComanda").click(function () {
    console.log('OrderHelper-Pending: Details order.') 
    urlExtract = $(this).attr("href");
});