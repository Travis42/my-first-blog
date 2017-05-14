from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
    # organize by published, then by date
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
                # user request, template file, things to populate the template:
    return render(request, 'blog/post_list.html', {'posts': posts})

