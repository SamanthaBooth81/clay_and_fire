// Country Drop Down Box colour styling
let countrySelected = $('#id_default_country').val();
if(!countrySelected) {
    $('#id_default_country').css('color', '#8e9ba8');
}
$('#id_default_country').change(function() {
    countrySelected = $(this).val();
    if(!countrySelected) {
        $(this).css('color', '#8e9ba8');
    } else {
        $(this).css('color', '#495057');
    }
});
