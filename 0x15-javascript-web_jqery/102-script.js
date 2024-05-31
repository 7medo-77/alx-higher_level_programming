$(document).ready(() => {
    $('#language_code').on("focus keydown", (event) => {
        if (event.keyCode === 13) {
            fetch(1);
        }
    });
    $('#btn_translate').on("click", () => {
        fetch(1);
    });

    function fetch(embedded = False) {
        const lang = $('#language_code').val();
        const request = "https://hellosalut.stefanbohacek.dev/?lang=" + lang;
        if (embedded) {
            $.get({
                type: 'GET',
                url: request,
                success: (response) => {
                    const result = response.hello;
                    $('#hello').text(result);
                },
            })
        }
    }

});
