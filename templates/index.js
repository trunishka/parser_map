/**
 * Created by user on 2/15/17.
 */
$(function(){
    $.getJSON('http://127.0.0.1:8000/info/?format=json', function(data) {
                $.each(data, function(key, val) {
                    users2[key] = val;
                   // $('#countries').append('<option value="' + val + '">' + key + '</option>');
                });
    });
    alert (users2[0].id);
});

