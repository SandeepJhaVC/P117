//Create date variable
var date = new Date()
let display_date = "Date:"+date.toLocaleDateString()

//Load HTML DOM
$(document).ready(function(){
    $("#display_date").html(display_date)



//Define variable to store predicted emotion
let predicted_emotion

$(function () {
    $("#predict_button").click(function () {
        let input_data = {
            "text":$("#text").val()
        }
        console.log(input_data)
        //AJAX call

        $.ajax({
            type:'POST',
            url:'/predict-emotion',
            data:JSON.stringify(input_data),
            dataType:"json",
            contentType:'application/json',
            success:function(result){
                $('#sentiment').html(result.data.predicted_emotion)
                $('#emoji').attr('src', result.data.predicted_emotion_img_url);
                $("#sentiment").css('display','');
                $("#emoji").css("display",'')
                predicted_emotion=result.data.predicted_emotion
                $('#save_button').prop('disabled', false)
            },

            error : function(result){
                alert(result.responseJSON.message)
            }
            
              
        });
    });
})

})