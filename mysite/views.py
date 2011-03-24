from django.http import HttpResponse, Http404
from db2.models import Users
from django.shortcuts import render_to_response
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('time.html', {'current_date': now})

def hello(request):
    return HttpResponse("Hello world")

def show_color(request):
    if "favorite_color" in request.COOKIES:
        return HttpResponse("Your favorite color is %s" % request.COOKIES["favorite_color"])
    else:
        return HttpResponse("You don't have a favorite color.")

def set_color(request):
    response = HttpResponse("Your cookie has been set")
    response.set_cookie("favorite_color", 'yellow')
    return response

def post_comment(request):
    if request.method != 'POST':
        raise Http404('Only POSTs are allowed')
    if 'comment' not in request.POST:
        raise Http404('Comment not submitted')
    if request.session.get('has_commented', False):
        return HttpResponse("You've already commented.")
    c = comments.Comment(comment=request.POST['comment'])
    c.save()
    request.session['has_commented'] = True
    return HttpResponse('Thanks for your comment!')

def login(request):
        #m = Member.objects.get(username=request.POST['username'])
    #return HttpResponse("ok")
    name = request.POST.get('username', '')
    #return HttpResponse(name)
    user = Users.objects.filter(username=name)
    if user[0].password == request.POST['password']:
        request.session['member_id'] = user[0].session
    HttpResponse(request.session['member_id'])
    return render_to_response('login.html', {'list': user[0].message})

def logout(request):
    try:
        del request.session['member_id']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")

def register(request):
   import random, string
   name = request.POST.get('name', '')
   username = request.POST.get('username', '')
   password = request.POST.get('password', '')
   cpassword = request.POST.get('cpassword', '')
   user = Users(username = username, name = name, password = password ,message ='', session=''.join(random.choice(string.letters) for i in xrange(10)))
   user.save()
   return HttpResponse("You've registered successfully")           

def add(request):
   #name = request.POST.get('name', '')
   message_new = request.POST.get('list', '')
   #name = 'ram'
   #return HttpResponse(request.session['member_id'])
   user = Users.objects.filter(session = request.session['member_id'])
   #return HttpResponse(str(user[0].name))#.message)
   user.update(message = user[0].message + message_new)
   return render_to_response('login.html', {'list':user[0].message})
