$(document).ready(() => {
    $('#btn_translate').on("click", () => {
        const lang = $('#language_code').val();
        const request = "https://hellosalut.stefanbohacek.dev/?lang=" + lang;

        $.get({
            type: 'GET',
            url: request,
            success: (response) => {
                const result = response.hello;
                $('#hello').text(result);
            },
        })
    })
});