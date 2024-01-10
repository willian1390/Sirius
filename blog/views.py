from django.shortcuts import render
from blog.models import Post, Categoria
from django.core.paginator import Paginator
# Create your views here.

def blog(request):
	posts=Post.objects.all()
	paginator = Paginator(posts, 2)
	page = request.GET.get('page')
	posts = paginator.get_page(page)

	return render(request, "blog/blog.html", {"posts": posts})


def blogleer(request):
	return render(request, "blog/blogleer.html")

def categoria(request, categoria_id):
	categoria=Categoria.objects.get(id=categoria_id)
	posts=Post.objects.filter(categorias=categoria)
	
	return render (request, "blog/categorias.html", {'categoria':categoria, "posts": posts})

