$(document).ready(function(){
    var getCheckPwd = RegExp(/^[a-zA-Z0-9]{4,12}$/);

    $('.btn').click(function(){
        if($('#username').val()==""){
        alert("아이디를 입력하세요")
        }

    if($('#password1').val()==""){
        alert("비밀번호 입력하세요")
        }

    if(!getCheckPwd.test($('#password1').val())){
        alert("비밀번호를 형식에 맞게 입력해주세요")
    }

    if($('#password2').val()==""){
        alert("비밀번호 확인란을 입력하세요")
        }



    if($('#email').val()==""){
        alert("이메일을 입력하세요")
        }


    if($('#password1').val()!=$('#password2').val()){
        alert('비밀번호가 일치하지 않습니다. 다시 입력해주세요')
        $('#password1').val('')
        $('#password2').val('')
        }
    })
})


