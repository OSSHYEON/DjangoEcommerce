$(document).ready(function(){
    var Rating = 0
    $('.stars .fas').click(function(){
        $(this).addClass('active')
        $(this).prevAll().addClass('active')
        $(this).nextAll().removeClass('active')

        var num = $(this).index()
        var starRate = num + 1

        if(starRate==1){
            $('.print').html('<img src="/static/images/angry.png" style="width:20px;">' + '별로에요')
        }
        else if(starRate==2){
            $('.print').html('<img src="/static/images/sad.png" style="width:20px;">' + '그저그래요')
        }
        else if(starRate==3){
            $('.print').html('<img src="/static/images/smile (1).png" style="width:20px;">' + '보통이에요')
        }
        else if(starRate==4){
            $('.print').html('<img src="/static/images/smiling.png" style="width:20px;">' + '맘에들어요')
        }
        else if(starRate==5){
            $('.print').html('<img src="/static/images/smile.png" style="width:20px;">' + '최고에요')
        }
        Rating = starRate
        console.log(Rating)
    })

    $('.starBtn').click(function(){
        console.log(productId)
        fetch("/star/",{
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken' : csrftoken,
        },
        body:JSON.stringify({'Rating':Rating, 'productId':productId})
    })
    .then((response)=>{
        return response.json()
    })
    .then((data)=>{
        console.log('별점을 매겼습니다.')
    })
    location.reload();
    })
})







$(document).ready(function(){
    $('.tab_menu li').click(function(){
        $(this).addClass('active')
        $(this).siblings().removeClass('active')

        var result = $(this).attr('data-alt')
        $('.tabs div').removeClass('active')
        $('#'+result).addClass('active')

        $('.tabs').last().addClass('active')
    })
})
