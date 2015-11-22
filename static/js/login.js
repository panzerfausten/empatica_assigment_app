function handlePatient(data){
	if(data == "None"){
		alert("Wrong Username/Passsword");
	}
	_data = JSON.parse(data);
	if(_data.type == "patient"){
		window.location = "app/user/"+_data.id+"/sessions";
	}
	if(_data.type == "support"){
		window.location = "app/support";

	}
	if(_data.type == "god"){
		window.location = "app/god";

	}
}
function login()

{

        _email =$("#email").val();
        _pwd =$("#password").val();
	$.ajax({
		url: "api/login?user="+_email+"&pwd="+_pwd,
		context: document.body,
		success:function(data){
			handlePatient(data);
		}
	}).done(function() {
	});
 
}
$( document ).ready(function() {
 
 
$("#loginbutton").click(function() {
	login();
});
});
$('#password').keypress(function (e) {
  if (e.which == 13) {
	login();
    return false;    
  }
});
