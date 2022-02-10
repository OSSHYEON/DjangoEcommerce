function findAddr(){
    new daum.Postcode({
        oncomplete: function(data) {

            var roadAddr = data.roadAddress;
            var extraRoadAddr = '';

            if(data.bname !== '' && /[동|로|가]$/g.test(data.bname)){
                extraRoadAddr += data.bname;
            }

            if(data.buildingName !== '' && data.apartment === 'Y'){
               extraRoadAddr += (extraRoadAddr !== '' ? ', ' + data.buildingName : data.buildingName);
            }

            if(extraRoadAddr !== ''){
                extraRoadAddr = ' (' + extraRoadAddr + ')';
            }

            document.getElementById('post_address').value = data.zonecode;
            document.getElementById("road_name").value = roadAddr;
            document.getElementById("number_addr").value = data.jibunAddress;

            if(roadAddr !== ''){
                document.getElementById("detail_addr").value = extraRoadAddr;
            } else {
                document.getElementById("detail_addr").value = '';
            }
        }
    }).open();
}


var getMail = RegExp(/^[A-Za-z0-9_\.\-]+@[A-Za-z0-9\-]+\.[A-Za-z0-9\-]+/);

function check_email(){
    if(!getMail.test($("#email").val())){
        alert("이메일을 형식에 맞게 입력해주세요!")
        $("#email").val("");
        $("#email").focus();
    }
}

function kakako(){

    var product = '상품'
    var quantity = $('#quantity').val();
    var total_amount = $('#total').val();

    console.log("결제요청중")
    fetch("/kakaopay/",{
        method : "POST",
        headers : {
                    "Content-Type":"application/json",
                    'X-CSRFToken': csrftoken,
                },
        body : JSON.stringify({
            'item_name' : product,
            'quantity': quantity,
            'total_amount' : total_amount,
            'phone': $('#phone').val(),
            'road_addr': $('#road_name').val(),
            'post_address' : $('#post_address').val(),
            'email' : $('#email').val(),
            'detail_addr' : $('#detail_addr').val()
        })
    })
    .then((response)=>{
        return response.json()
    })
    .then((data)=>{
        console.log('data:', data)

    })
}





function Payment11111111111() {
    var IMP = window.IMP;
    IMP.init('imp97760430');
    IMP.request_pay({
        pg : 'html5_inicis',
        pay_method : "card",
        merchant_uid : 'merchant_' + new Date().getTime(),
        name : form.product_name.value,
        amount : '{{ order.get_cart_total }}',
        buyer_email : $('#email').val(),
        buyer_name : form.name.value,
        buyer_tel : $('#phone').val(),
        buyer_addr : $('#road_name').val(),
        buyer_postcode : $('post_address').val(),
    }, function (rsp) {
        alert("aa");
        if (rsp.success) {
            $ajax({
                url : "{% url 'payment' %}",
                method : "POST",
                headers : {
                    "Content-Type":"application/json",
                    'X-CSRFToken': csrftoken,
                },
                data:{
                        imp_uid: rsp.imp_uid,
                        merchant_uid: rsp.merchant_uid
                    }
                }).done(function(data){
                    var msg = '결제가 완료되었습니다.';
                    console.log(msg);
                    msg += '고유ID : ' + rsp.imp_uid;
                    msg += '상점 거래ID : ' + rsp.merchant_uid;
                    msg += '결제 금액 : ' + rsp.paid_amount;
                    msg += '카드 승인번호 : ' + rsp.apply_num;
                })

        }else{
            alert("결제에 실패했어요 ㅠㅠ 에러 : " + rsp.error_msg);
        }
    }
    );
}



