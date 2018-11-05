from django.shortcuts import render
from .models import post
# from django.http import HttpResponse
# Create your views here.
# posts =[
# 	{
# 			'author':'CoreyMS',
# 			'title':'Blog_post',
# 			'content':'First post content',
# 			'date_posted':'August 25, 2031'
# 	},
# 	{

# 			'author':'Mohammed Rizwan',
# 			'title':'Blog_post 2',
# 			'content':'Second post content',
# 			'date_posted':'November 4, 2018'
# 	}
# ]


def home(request):
	context={
		'rizwan': post.objects.all()
	}
	return render(request, 'blog/home.html' ,context)



def about(request):
	# return HttpResponse("<h1>blog About</h1>")
	return render(request, 'blog/about.html' , {'title':'django'})

