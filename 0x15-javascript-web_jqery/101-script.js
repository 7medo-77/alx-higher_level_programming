$(document).ready(() => {
	$('#add_item').on('click', $('<li>Item</li>'), () => {
		$('<li>Item</li>').appendTo(uList);
	});

	$('#clear_list').on('click', () => {
		uList.empty()
	});

	$("#remove_item").click(function () {
		$("ul.my_list li").last().remove();
	});

});