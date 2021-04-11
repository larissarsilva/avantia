from django.contrib.auth.views import LoginView


#Logar usuário
class UserLoginView(LoginView):
    template_name = 'users/login.html'    
