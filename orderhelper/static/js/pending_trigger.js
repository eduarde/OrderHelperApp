var urlExtract;
	
$(".actionCloseSubcomanda").click(function () {
    urlExtract = $(this).attr("href");
});

$(".actionCancelSubcomanda").click(function () {
    urlExtract = $(this).attr("href");
});

$(".actionViewSubcomanda").click(function () {
    urlExtract = $(this).attr("href");
    });

$(".actionCloseComanda").click(function () {

	if ($(this).hasClass('disabled')) {
  		event.stopImmediatePropagation();
        return(false);
  	}

	
		 urlExtract = $(this).attr("href");
 });

$(".actionCancelComanda").click(function () {

	if ($(this).hasClass('disabled')) {
  		event.stopImmediatePropagation();
        return(false);
  	}
	
	urlExtract = $(this).attr("href");
});

$(".actionViewComanda").click(function () {
    urlExtract = $(this).attr("href");
});