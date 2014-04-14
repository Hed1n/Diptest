# Create your views here.
from django.shortcuts import render_to_response
from django.contrib.auth.forms import UserCreationForm
from accounts.froms import regform
from django.template import RequestContext
from django.contrib.auth.models import User, UserManager
from baseapp.models import AuthUser

def registr(request, template_name="registration/registration.html"):

    userset = User.objects.all()

    uniklelogin = 0
    validpassword = 0
    form = regform
    if request.method == 'POST':
        form = regform(request.POST)
        postdata = request.POST.copy()
        un = postdata.get('login', '')
        pw1 = postdata.get('password1', '')
        pw2 = postdata.get('password2', '')
        email = postdata.get('email', '')


        if pw1 == pw2:
            User.objects.create_user(un, email, pw1)

#        User.objects.create_user('KpeoJI11', 'xp44@mail.ru', '1234567890')




    context = RequestContext(request, {'form' : form})
    return render_to_response(template_name, context)
