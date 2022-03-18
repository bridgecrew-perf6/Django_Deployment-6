from django.shortcuts import render
from django.http import HttpResponse
from .models import User

def home(request):
     if 'user' in request.session :
        current_user = request.session['user']
        param = {'current_user' : current_user }
        return render(request, 'F02/base.html', param)
     else :
        return render(request, 'F02/login.html')
     return render(request,'F02/login.html')

def signup(request) :
     if request.method == "POST" :
         uname = request.POST.get('uname')
         pwd  = request.POST.get('pwd')
         if User.objects.filter(username=uname).count()> 0:
             return HttpResponse('Username already exists')
         else :
            user = User( username=uname, password =pwd)
            user.save()
            return render(request, 'F02/login.html')
     else :
         return render (request, 'F02/signup.html')

def login(request) :
     if request.method == 'POST' :
         uname = request.POST.get('uname')
         pwd = request.POST.get('pwd')

         check_user = User.objects.filter(username=uname, password= pwd)

         if check_user:
            request.session['user'] = uname
            return render(request, 'F02/base.html')
         else :
            return HttpResponse('Pls enter valid Username or Password')
     return render(request, 'F02/login.html')

def logout(request):
     try :
        del request.session['user']

     except :
        return render (request, 'F02/login.html')
     return render (request, 'F02/login.html')

















 # ----- Send Email ----
# def sendMail(request):
#     messageSent= false
#     if request.method == "POST" :
#         form = EmailForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             subject =
#             message = cd['message']
#             recipient = cd['recipient']
#             send_mail(subject, message, setting.DEFAULT_FROM_EMAIL, [recipient]):
#         messageSent = true
#     else
#         form = EmailForm()
#     return render(request,'index.html',{'form' : form, "message" : messageSent})




# def Index(request):
#     return render (request,'F02/home.html')
# def about(request):
#     return render(request,'F02/about.html')
#
# def data(request):
#     celebrity_list = Celebrity.objects.all()
#     return render(request,'F02/data.html', {'data' :celebrity_list})


# def listing(request):
#     customer_list= Customer.objects.all()
#     paginator = Paginator(customer_list,3)
#     pagenumber= request.GET.get('page')
#     try :
#             customer =paginator.page(pagenumber)
#
#     except PageNotAnInteger :
#             customer =paginator.page(1)
#     except EmptyPage:
#             customer =paginator.page(paginator.num_pages)
#     #
#     return render(request,'F02/homepage.html', {'Customer': customer})

# def Home(request):
#     return render(request,'F02/homepage.html')
#
# def Signup(request):
#     return render(request,'F02/Signup.html')

# Create your views here.
