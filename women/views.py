from django.shortcuts import render
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
    cats = Category.objects.all()
    context =  {
        'title':'Главная страница',
        'posts': posts,
        'cats': cats,
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

def show_post(request,post_id):
    return HttpResponse(f"Статья с айди = {post_id}")

def show_category(request,cat_id):
    posts = Women.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()
    context =  {
        'title':'Ототброжение по рубрикам ',
        'posts': posts,
        'cats': cats,
        'menu' : menu,
        'cat_selected': 0,
        
    }
    return render(request,'women/index.html',context=context)