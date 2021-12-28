
$( document ).ready(function() {
$('#id_sale_price, #id_purchase_price, #id_profit, #id_received, #id_pending').keyup(function(){

    var sale_value = $('#id_sale_price').val();
    var purchase_value = $('#id_purchase_price').val();
    var profit_value = sale_value - purchase_value

    var sale_value_2 = $('#id_sale_price').val();
    var received_value = $('#id_received').val();
    var pending_value = sale_value_2 - received_value

    


    $('#id_profit').val(profit_value);
    $('#id_pending').val(pending_value);
   
});

});