from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound

from women.models import Category, Women

menu = [{'title':'О сайте','url_name':'about'},
        {'title':'Добавить статью','url_name':'add_page'},
        {'title':'Обратная связь','url_name':'contact'},
        {'title':'Войти','url_name':'login'}
]

# Create your views here.
def about(request):
    return render(request , 'women/about.html',{'title':'О сайте', 'menu':menu}) 


def index(request):
    posts = Women.objects.all()
   
    context =  {
        'title':'Главная страница',
        'posts': posts,
        
        'menu' : menu,
        'cat_selected': 0,
        
    }
    return render(request , 'women/index.html',context=context)

def addpage(request):
    return HttpResponse("AddPage")

def contact(request):
    return HttpResponse("Contact")
    
def login(request):
    return HttpResponse("Login")


def pageNotFound(request,exeption):
    return HttpResponseNotFound('<h1> Page not found :(</h1>')

def show_post(request,post_slug):
    post = get_object_or_404(Women ,slug=post_slug)

    contex = {
        'post': post,
        'menu' : menu,
        'title' : post.title,
        'cat_selected' : post.cat
    }

    return render (request,'women/post.html',context=contex)

def show_category(request,cat_id):
    posts = Women.objects.filter(cat_id=cat_id)
    print(posts,"-------------------------------------------------")
    context =  {
        'title':'Ототброжение по рубрикам ',
        'posts': posts,
    
        'menu' : menu,
        'cat_selected': cat_id,
        
    }
    return render(request,'women/index.html',context=context)