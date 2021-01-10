function changeMask() {
    let mask = $('#equipment_type option:selected').attr('name');
    $('#equipmentMask').text('Маска: ' + mask);
}

$( function() {
    changeMask();
});

$('#equipmentMask').tooltip({
    title:  'N – цифра от 0 до 9' + '<br>' +
            'A – прописная буква латинского алфавита' + '<br>' +
            'a – строчная буква латинского алфавита' + '<br>' +
            'X – \'A\' или \'N\'' + '<br>' +
            'Z –символ из списка: \'-\', \'_\', \'@\'',
    placement: 'left',
    delay: { show: 300, hide: 100 },
    html: true,
});
