from django import forms

class PostForm(forms.Form):
    class Meta:
    	title = forms.CharField(max_length=100)
    	body = forms.CharField(widget="forms.TextArea")
    	image = forms.ImageField()
    	published = forms.DateTimeField()
    	created = forms.DateTimeField(auto_now_add=True)
    	updated = forms.DateTimeField(auto_now=True)