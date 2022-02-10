# DjangoEcommerce

## Main Page
![image](https://user-images.githubusercontent.com/94279314/153344989-800343fb-5839-486e-ac1e-ac4ff530a7e1.png)

## Test
![Test](https://user-images.githubusercontent.com/94279314/153346712-a1fb78bb-0901-4bef-afe9-78c8a9a30bcd.gif)


## Requirements
  + ```django 4.0.1 ```
  ```pip install django```
  + ```easy_thumbnails 2.8.1```
  ```pip install easy_thumbnails```
  + ```allauth 0.48.0```
  ```pip install django-allauth```
  + ```rest_framework 3.13.1```
  ```pip install djangorestframework```
  + ```debug_toolbar 3.2.4```
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
  + RESTful api: 상품 정보, 질문 작성자 유저 정보 전달 시 활용 ```예시 ) http://127.0.0.1:8010/shop/1/```
  + javascript/jquery
