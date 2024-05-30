const $char = $('#character');
$.get({
	type: 'GET',
	url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
	success: (data) => {
		const name = data.name;
		$char.text(name);
	},
})
