from django.http import HttpResponse

def about(request):
''' request is the object received from the browser '''
    return HttpResponse("about")