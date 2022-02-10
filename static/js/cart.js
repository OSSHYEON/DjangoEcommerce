var productId;
var action;
function btn_to_cart(){
    var updateBtns = $('.btn-to-cart')
    for (var i=0; i< updateBtns.length; i++){
        updateBtns[i].addEventListener('click', function(){
            productId = this.dataset.product
            action = this.dataset.action

            console.log('user:', user)

            if (user === 'AnonymousUser'){
                alert('로그인이 필요한 서비스입니다! 로그인해주세요')
            }else{
                updateUserOrder(productId, action)
            }
        })
    }
}

function updateUserOrder(productId, action){
    console.log('User is logged in, sending data ~')
    console.log(productId)

    fetch("/update_item/", {
        method: 'POST',
        headers:{
            'Content-Type' : 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'productId':productId, 'action':action})
    })
    .then((response)=>{
        return response.json()
    })
    .then((data)=>{
        alert('장바구니에 추가되었습니다', data)
    })
}




