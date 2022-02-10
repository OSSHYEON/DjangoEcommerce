# DjangoEcommerce

![image](https://user-images.githubusercontent.com/94279314/153344989-800343fb-5839-486e-ac1e-ac4ff530a7e1.png)
![shop](https://user-images.githubusercontent.com/94279314/153346391-dece1b57-cd4a-47f8-83bc-112aadbb770d.gif)



## Requirements
  + easy_thumbnails
  ```pip install easy_thumbnails```
  + allauth
  ```pip install django-allauth```
  + rest_framework
  ```pip install djangorestframework```
  + debug_toolbar
  ```pip install django-debug-toolbar```
  
  
## Using
  + Fetch api : 장바구니에 상품 추가, 수량 변경, 배송지 정보를 view에 넘겨줄 때 활용
  ``` 
  $(document).ready(function(){
        $('.qt_btn').click(function(){
            var productId = this.dataset.product
            var action = this.dataset.action;
            console.log(action);
            console.log(productId);

            fetch("/update_item/",{
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken' : csrftoken,
                },
                body:JSON.stringify({'productId':productId, 'action':action})
            })
            .then((response)=>{
                return response.json()
            })
            .then((data)=>{
                console.log('상품 갯수를 변경했습니다')
            })
            location.reload();

        })

    })
  ```
  + RESTful api ```http://127.0.0.1:8010/shop/1/```
  + javascript/jquery
