from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # verifica se usuário e senha estão certos
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # loga o usuário
            return redirect('dashboard')  # redireciona pro dashboard
        else:
            # se falhar, volta pro login com uma mensagem de erro
            return render(request, 'login.html', {'erro': 'Usuário ou senha inválidos.'})

    # se for GET, só mostra a tela de login
    return render(request, 'login.html')

# o dash


@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html')

# logout


def logout_view(request):
    logout(request)
    return redirect('login')
