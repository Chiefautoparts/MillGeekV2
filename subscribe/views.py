from django.shortcuts import render
from .forms import EmailPostForm

def newsLetter(request, post_id):
	post = get_object_or_404(Post, id=post_id, status='publised')

	if request.method == 'POST':
		form = EmailPostForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
	else:
		form = EmailPostForm()
	return render(request, 'subscribe/email.html', {'post': post, 'form': form})