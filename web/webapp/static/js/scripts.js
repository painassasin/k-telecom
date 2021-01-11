function changeMask() {
    let mask = $('#equipment_type option:selected').attr('name');
    $('#equipmentMask').text('Маска: ' + mask);
}

$( function() {
    changeMask();
});

$('#equipmentHint').tooltip({
    title:  'N – цифра от 0 до 9' + '<br>' +
            'A – прописная буква латинского алфавита' + '<br>' +
            'a – строчная буква латинского алфавита' + '<br>' +
            'X – \'A\' или \'N\'' + '<br>' +
            'Z –символ из списка: \'-\', \'_\', \'@\'',
    placement: 'right',
    delay: { show: 300, hide: 100 },
    html: true,
});
