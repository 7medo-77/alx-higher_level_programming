const $uList = $('#list_movies');
$.get({
	type: 'GET',
	url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
	success: (data) => {
		const resArray = data.results;
		$.each(resArray, (index, object) => {
			const title = object.title;
			$uList.append('<li>'+title+'</li>');
		})
	},
})
