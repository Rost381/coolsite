from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from uuslug import slugify

from .forms import *
from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]

class WomenHome(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts' #Заменяем стандартную  object_list

    def get_context_data(self, *, object_list=None, **kwargs): #Создает динамический контекс
        context = super().get_context_data(**kwargs) #Конструктор родителя - берет и распаковывает существующие параметры из словаря **kwargs
        #Добавляем к уже полученным из SUPER
        context['menu'] = menu
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0 #Выделяет ПЕРВЫЙ пункт меню
        return context

    def get_queryset(self): #Что отображаем
        return Women.objects.filter(is_published=True)

# Функциональное ВЬЮ
# def index(request):
#     posts = Women.objects.all()
#
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Главная страница',
#         'cat_selected': 0,
#     }
#
#     return render(request, 'women/index.html', context=context)

def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О сайте'})

class AddPage(CreateView):
    form_class = AddPostForm #Указывает на класс формы
    template_name = 'women/addpage.html'
    # reverse пытается сразу построить нужный маршрут в момент создания класса
    # reverse_lazy строит маршрут в момент, когда он понадобиться
    success_url = reverse_lazy('home') #Куда перенаправиться в случае успешного создания статьи

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление статьи'
        context['menu'] = menu
        return context
# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#
#         if form.is_valid():
#             form.save()  # Когда форма УЖЕ  связана с БД
#             #print(form.cleaned_data)
#             # try:
#             #     #Women.objects.create(**form.cleaned_data) #Когда форма не связана с БД
#             return redirect('home')
#             # except:
#             #     form.add_error(None, 'Ошибка добавления поста')
#     else:
#         form = AddPostForm()
#     return render(request, 'women/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})

def contact(request):
    # print(request.COOKIES)
    # print(request.headers)
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

class ShowPost(DetailView):
    model = Women
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug' #Переменная для Слага своя
    #pk_url_kwarg = 'pk' Если использовать не Слаг а pk, 'pk' по умолчанию, можно свою - 'post_pk'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        context['menu'] = menu
        return context

# def show_post(request, post_slug):
#     post = get_object_or_404(Women, slug=post_slug)
#
#     context = {
#         'post': post,
#         'menu': menu,
#         'title': post.title,
#         'cat_selected': post.cat_id,
#     }
#     return render(request, 'women/post.html', context=context)


class WomenCategory(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False #404 Если поста нет

    def get_queryset(self):
        #self.kwargs Получает все параметры маршрута, cat_slug это slug slug Модели class Category
        # cat__slug: cat есть в модели class Women и сылается на slug Модели class Category
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        context['menu'] = menu
        context['cat_selected'] = context['posts'][0].cat_id
        return context
# def show_category(request, cat_slug):
#     cat_id = Category.objects.get(slug =cat_slug).id
#     posts = Women.objects.filter(cat_id=cat_id)
#     Women.objects.filter(cat__in=Category.objects.filter(slug=cat_slug))
#
#     if len(posts) == 0:
#         raise Http404()
#
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Отображение по рубрикам',
#         'cat_selected': posts[0].cat_id,
#     }
#
#     return render(request, 'women/index.html', context=context)

def react(request):
    return render(request, 'women/react.html')