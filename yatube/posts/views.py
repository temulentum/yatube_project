from django.http import HttpResponse


# Главная страница
def index(request):    
    return HttpResponse('Морда')


# Страница групповых постов
def group_posts(request, slug):
    return HttpResponse(f'Посты {slug}')
