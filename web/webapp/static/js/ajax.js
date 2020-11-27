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
            if (response['success'] == true) {
                alert(response['msg']);
                form.trigger('reset');
                $('#msg').html('');
            }
           else {
                $('#msg').html(response['msg']);
           }
        },
        error: function(error) {
            console.log(error);
        }
    })
}