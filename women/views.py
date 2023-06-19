from django.views.generic import ListView , DetailView , CreateView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from women.forms import AddPage
from django.shortcuts import redirect 

from women.models import Category, Women

menu = [{'title':'О сайте','url_name':'about'},
        {'title':'Добавить статью','url_name':'add_page'},
        {'title':'Обратная связь','url_name':'contact'},
        {'title':'Войти','url_name':'login'}
]

# Create your views here.
def about(request):
    return render(request , 'women/about.html',{'title':'О сайте', 'menu':menu}) 


# def index(request):
#     posts = Women.objects.all()
   
#     context =  {
#         'title':'Главная страница',
#         'posts': posts,
         
#         'menu' : menu,
#         'cat_selected': 0,
        
#     }
#     return render(request , 'women/index.html',context=context)


class WomenHome(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
 
    

    def get_context_data(self,*, object_list=None, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['cat_selected'] = 0
        context['title'] = 'Главная страница'
        return context
    
    def get_queryset(self) :
        return Women.objects.filter(is_published=True)

    
# def addpage(request):
#     if request.method == 'POST':
#         form = AddPage(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPage()
 
#     return render(request, 'women/addpage.html',{'form':form,'menu':menu,'title':'Добавдение статьи'})

class AddPost(CreateView):
    form_class = AddPage
    template_name = 'women/addpage.html'

    def get_context_data(self,*, object_list=None, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Добавление статьи'
        return context 


def contact(request):
    return HttpResponse("Contact")
    
def login(request):
    return HttpResponse("Login")


def pageNotFound(request,exeption):
    return HttpResponseNotFound('<h1> Page not found :(</h1>')

# def show_post(request,post_slug):
#     post = get_object_or_404(Women ,slug=post_slug)

#     contex = {
#         'post': post,
#         'menu' : menu,
#         'title' : post.title,
#         'cat_selected' : post.cat
#     }

#     return render (request,'women/post.html',context=contex)

class ShowPost(DetailView):
    model = Women
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'
     
     
    def get_context_data(self,*, object_list=None, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['cat_selected'] = 0
        context['title'] = 'Главная страница'
        return context


class ShowCategory(ListView):
    model =Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self) :
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self,*, object_list=None, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Категория - '+ str(context['posts'][0].cat)
        context['cat_selected'] = context['posts'][0].cat_id
        return context

# def show_category(request,cat_id):
#     posts = Women.objects.filter(cat_id=cat_id)
#     print(posts,"-------------------------------------------------")
#     context =  {
#         'title':'Ототброжение по рубрикам ',
#         'posts': posts,
    
#         'menu' : menu,
#         'cat_selected': cat_id,
        
#     }
#     return render(request,'women/index.html',context=context)