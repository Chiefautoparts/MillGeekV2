$('#btn-wrap').click(function(){
	if($('#mid-blue').hasClass('asctive')){
		$('#mid-blue, #icon, .nav-btn, #bg-disc').removeClass('active');
	} else {
		$('#mid-blue, #icon, .nav-btn, #bg-disc').addClass('activeopening').removeClass('opening');
	}
});