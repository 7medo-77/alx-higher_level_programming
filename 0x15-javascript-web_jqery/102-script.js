$(document).ready(() => {

    $('#language_code').on("focus keydown", (event) => {
        const lang = $('#language_code').val();
        const request = "https://hellosalut.stefanbohacek.dev/?lang=" + lang;

        if (event.keyCode === 13)
            $.get({
                type: 'GET',
                url: request,
                success: (response) => {
                    const result = response.hello;
                    $('#hello').text(result);
                },
            })
    })

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