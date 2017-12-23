function displayAdmin() {
	if (user.role == "admin") {
		$("div.admin").show();
	}
	else if (user.role == "employee") {
		$("div.employee").show();
	}
	
}