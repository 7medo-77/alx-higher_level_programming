$(document).ready(() => {
	const $hello = $('#hello');
	$.get({
		type: 'GET',
		url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
		success: (data) => {
			const helloText = data.hello;
			$hello.text(helloText);
		}
	})
})
