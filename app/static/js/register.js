function bindCaptchaBtnClick(){
    $("#captcha-btn").on("click", function(event){
        var $this = $(this);
        var email = $("input[name='email']").val();
        if(!email){
            alert("请输入邮箱");
            return;
        }

        // 发送验证码
        $.ajax({
            method: "POST",
            dataType:"json",
            url: "/user/captcha",
            data: {
                email: email
            },
            success: function( result ) {
              if(result.code == 200){
                // 取消点击事件
                $this.off("click")
                // 开始倒计时
                var countDown = 60;
                var timer = setInterval(function(){
                    countDown -= 1;
                    if(countDown > 0){
                        $this.text(countDown+"秒后重新发送");
                    }else{
                        $this.text("获取验证码");
                        // 重新执行绑定click方法
                        bindCaptchaBtnClick();
                        // 删除倒计时
                        clearInterval(timer);
                    }
                }, 1000);
                alert("验证码发送成功");
              }else{
                alert(result.message);
              }
            }
          });
    })
}

$(function(){
    bindCaptchaBtnClick();
})