from django.http import HttpResponse


def home_page(request):
    print('home pahe requested')
    return HttpResponse('this is home page')