//function BookMyShow(){
//    let select = document.getElementById("select-order")
//    let selectedValue = select.options[select.selectedIndex].value;
//    let data = {
//        'timing': ${selectedValue},
//        };
//    $.ajax({
//        url: 'http://127.0.0.1:8000/order/',
//        type: 'post',
//        data: ${data},
//        success: function(response){
//        console.log("Order successful!!")
//    }
//    });
//
//}
//
//

$('.dropdown-trigger').dropdown();

$('.modal').modal();