from django.shortcuts import render,redirect
from django.urls import reverse_lazy,reverse
from django.views.generic import ListView,CreateView,UpdateView
from .forms import KeijibanForm,SignupForm,ProfileForm,LoginForm,CreateForm
from django.contrib.auth import authenticate, login, logout
from .models import User,Keijiban
from django.utils.safestring import mark_safe
import json


class List(ListView) :
    model = Keijiban
    form_class = KeijibanForm
    template_name = 'list.html'

    def get_context_data(self):
        context=super(List,self).get_context_data()
        queryset = Keijiban.objects.order_by('created_at').reverse()
        context['object_list'] = queryset
        return context






class Create(CreateView) :
    model = Keijiban
    form_class = CreateForm
    template_name = 'create.html'
    success_url = reverse_lazy('list')

    def form_valid(self,form):
        form.instance.author_id = self.request.user.id
        return super(Create,self).form_valid(form)



class Profile(UpdateView) :
    model = User
    form_class = ProfileForm
    template_name = 'profile.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    success_url=reverse_lazy('list')


class Signup(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'signup.html'

    def get_success_url(self):
        form=self.get_form()
        # print(form.data)
        username = form.data['username']
        password = form.data['password1']
        user = authenticate(self.request,username=username,password=password)
        login(self.request,user)
        return reverse('profile',kwargs={'username':username})


def loginfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
        else:
            return redirect('login')
    else :
        loginform = LoginForm()
        return render(request,'login.html',{'loginform':loginform})
    return redirect('list')




def chat(request):
    return render(request, 'chat.html',{})

def room(request, room_name):
    return render(request, 'room.html', {
        'room_name': room_name
    })
