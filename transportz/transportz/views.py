from django.http import HttpResponse
from django.shortcuts import render, redirect
from transportz.models import User, Line, Arret, Signal

def login_view(request) :
    if 'pseudo' in request.GET and 'phrasepass' in request.GET:
        pp=request.GET['phrasepass']
        psah=request.GET['pseudo']
        if len(User.objects.filter(pseudo=psah).filter(phrasepass=pp))==1:
                request.session['pseudo']=psah
                return redirect('/home')
        else:
            templates_valuz={'yo': 'incorrect password or pseudo'}
            return render(request, 'login.html', templates_valuz)
    else:
        return render(request, 'login.html')

def register_view(request):
    if 'email' in request.GET:
        if len(request.GET['pseudo'])>4 and len(request.GET['phrasepass'])>8 and request.GET['password']=='2022':
            NewUser = User(firstname=request.GET['firstname'],
                       lastname=request.GET['lastname'],
                       email=request.GET['email'],
                       pseudo=request.GET['pseudo'],
                       phrasepass=request.GET['phrasepass'],
                       gender=request.GET['gender'],
                       admin=True)
            NewUser.save()
            return redirect('/login')
        elif len(request.GET['pseudo'])>4 and len(request.GET['phrasepass'])>8:
            NewUser = User(firstname=request.GET['firstname'],
                       lastname=request.GET['lastname'],
                       email=request.GET['email'],
                       pseudo=request.GET['pseudo'],
                       phrasepass=request.GET['phrasepass'],
                       gender=request.GET['gender'],
                       admin=False)
            NewUser.save()
            return redirect('/login')
        else:
            templates_value={'error':'length of pseudo or phrasepass is not long enough'}
            return render(request, 'register.html', templates_value)

    else:
        return render(request, 'register.html')


def home_view(request):
    if 'pseudo' in request.session:
        p=request.session['pseudo']
        U=User.objects.get(pseudo=p)
        admin_statut=U.admin
        if U.admin==True:
            templates_value={'pseu': p, 'statut': admin_statut}
            response =  render(request, 'home.html', templates_value)
            return response
        else:
            templates_value={'pseu':p}
            return render (request, 'home.html', templates_value)


def signal_view(request) :
    if 'arret' in request.GET and 'pseudo' in request.session:
        A=Arret.objects.get(arret=request.GET['arret'])
        U=User.objects.get(psedo=request.session['pseudo'])
        Newsignal= Signal(arret=A, who=U)
        Newsignal.save()
        return render(request, 'signal.html')
    else:
        return redirect("/")


def line_view(request) :
    if 'line' in request.POST:
        NewInfo= Line(name=request.POST['line'])
        NewInfo.save()
        return redirect('/arret', line=request.POST['line'])
    if 'line' in request.GET:

    	return render(request, 'line.html')

def arret_view(request):
    print(request)
    if 'arret' in request.POST:
        Newarret=Arret(arret=request.POST['arret'])
        Newarret.save()
        #return redirect('/')
    return render(request, 'arret.html')



def control_view(request) :
    Signalz=Signal.objects.all()
    poucave=Signal.arret(user=request.session['pseudo'])
    templates_value={"controle": Signalz,"who_writed": poucave}
    return render(request, 'control.html', templates_value)
