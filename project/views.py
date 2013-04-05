# Create your views here.


from django.http import HttpResponse

from django.template import Context

from django.template.loader import get_template

from django.http import HttpResponse, Http404
from django.contrib.auth.models import User

def user_page(request, username):
    try:
        user=User.objects.get(username=username)
    except:
        raise Http404('Requested user not found, booya!')
    bookmarks=user.bookmark_set.all()
    template=get_template('user_page.html')
    variables=Context({
        'username':username,
        'bookmarks':bookmarks
    })
    output=template.render(variables)
    return HttpResponse(output)

def main_page (request):
    template=get_template('main_page.html')
    variables=Context({
        'head_title':'Django Bookmarks',
        'page_title':"Welcome to Lisa's Bookmarks",
        'page_body':'Where you can store and share some pretty cool stuff :)'
        })
    output=template.render(variables)
    return HttpResponse(output)

    
#def main_page(request):
 #   output='''
#<html>
#<head><title>%s</title></head>
#<body>
#<h1>%s</h1><p>%s</p>
#v</body>
#</html>
#''' % ( 'Django Bookmarks', "Welcome to Lisa's site", 'Where you can share some really cool stuff :D')
#    return HttpResponse(output)
        


