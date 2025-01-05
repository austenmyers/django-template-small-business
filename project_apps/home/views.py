from django.http import HttpResponse
from django.template import loader


def home(request):
    template = loader.get_template('pages/home.html')
    context = {
        'welcome': 'Hello, World!'
    }
    return HttpResponse(template.render(context, request))
