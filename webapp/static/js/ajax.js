// Переопределение поведение кнопки "Добавить"
$(document).ready(function() {
    $('#main_form').on('submit', function(event) {
        event.preventDefault();
        sendAjaxForm('main_form');
    })
});


// Отправка формы через ajax
function sendAjaxForm(ajax_form){
    var form = $('#' + ajax_form);
    $.ajax({
        type: form.attr('method'),
        url: form.attr('action'),
        data: form.serialize(),
        success: function(response) {
            var json = $.parseJSON(response);
            if (json.success == true) {
                alert(json.msg)
                form.trigger('reset');
                $('#msg').html('');
            }
            else {
                $('#msg').html(json.msg)
            }
        },
        error: function(error) {
            console.log(error);
        }
    })
}