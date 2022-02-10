var getMail = RegExp(/^[A-Za-z0-9_\.\-]+@[A-Za-z0-9\-]+\.[A-Za-z0-9\-]+/);


function check_email(){
    if(!getMail.test($("#email").val())){
        alert("이메일을 형식에 맞게 입력해주세요!")
        $("#email").val("")
        $("#email").focus()
    }

    if(){
        alert("아이디를 입력하세요")
        $().val("")
        $().focus()
    }

    if($('#password1').val()!=$('#password2').val(){
        alert("비밀번호가 일치하지 않습니다!");
        $('#password1').val("");
        $('#password2').val("");
    })
}