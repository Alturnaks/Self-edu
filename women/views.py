from django.views.generic import ListView , DetailView , CreateView, FormView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from women.forms import *
from django.shortcuts import redirect 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout , login
from women.models import Category, Women
from .utils import *



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


class WomenHome(DataMixin , ListView):
    
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
 
    

    def get_context_data(self,*, object_list=None, **kwargs) :
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items())+list(c_def.items()))
    
    def get_queryset(self) :
        return Women.objects.filter(is_published=True).select_related('cat')

    
# def addpage(request):
#     if request.method == 'POST':
#         form = AddPage(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return вredirect('home')
#     else:
#         form = AddPage()
 
#     return render(request, 'women/addpage.html',{'form':form,'menu':menu,'title':'Добавдение статьи'})

class AddPost(LoginRequiredMixin,DataMixin,CreateView):
    form_class = AddPage
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self,*, object_list=None, **kwargs) :
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление статьи")
        return dict(list(context.items())+list(c_def.items()))
        


class ContactFormView(DataMixin,FormView):
    template_name = 'women/contact.html'
    form_class = ContactForm
    success_url = 'home'

    def get_context_data(self,*, object_list=None, **kwargs) :
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title ="FeedBack" )
        return dict(list(context.items())+list(c_def.items()))

    def form_valid(self, form) :
        print(form.cleaned_data)
        return redirect('home')




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

class ShowPost(DataMixin,DetailView):
    model = Women
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'
     
     
    def get_context_data(self,*, object_list=None, **kwargs) :
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items())+list(c_def.items()))



class ShowCategory(DataMixin,ListView):
    model =Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self) :
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')

    def get_context_data(self,*, object_list=None, **kwargs) :
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title='Категория - '+ str(c.name),cat_selected = c.pk)
        return dict(list(context.items())+list(c_def.items()))

# def show_category(request,cat_id):
#     posts = Women.objects.filter(cat_id=cat_id)
#     print(posts,"-------------------------------------------------")
#     context =  {
#         'title':'Ототброжение по рубрикам ',
#         'posts': posts,
    
#         'menu' : menu,
#         'cat_selected': cat_id,
        
#     }
#     return render(request,'women/index.html',conte
class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'women/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self,*, object_list=None, **kwargs) :
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title ="Регистрация" )
        return dict(list(context.items())+list(c_def.items()))

    def form_valid(self, form) :
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin,LoginView):
    form_class = LoginUserForm
    template_name = 'women/login.html'

    def get_context_data(self,*, object_list=None, **kwargs) :
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title ="Войти" )
        return dict(list(context.items())+list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')
def logout_user(request):
    logout(request)
    return redirect('login')