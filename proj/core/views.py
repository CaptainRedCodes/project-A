from django.shortcuts import redirect, render
from item.models import Category,Item
from .forms import SignUpForm
from django.contrib.auth import logout
from django.contrib.auth.views import LogoutView
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_GET
# Create your views here.
def index(request):
    items=Item.objects.filter(is_sold=False)[0:6]
    categories=Category.objects.all
    return render(request,'core/index.html',{
                  'categories':categories,
                  'items':items,
    })

def contact(request):
    return render(request,'core/contact.html')

def signup(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login') #to login
    else:
        form=SignUpForm()

    return render(request,'core/signup.html',{'form':form})


class CustomLogoutView(LogoutView):
    @method_decorator(require_GET)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

