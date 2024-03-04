from django.shortcuts import render
from app1.models import Movie
from app1.forms import bookform
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.
#def home(request):
    #m=Movie.objects.all()
    #return render(request,'home.html',{'m':m})

class MovieList(ListView):
    model=Movie
    template_name ="home.html"
    context_object_name ="m"

#def add(request):
    #if (request.method=="POST"):
        #form=bookform(request.POST)
        #if form.is_valid():
            #form.save()
            #return home(request)
    #form=bookform()
    #return render(request,'addmovie.html',{'form':form})

class Movieadd(CreateView):
    model=Movie
    template_name="addmovie.html"
    fields='__all__'
    success_url=reverse_lazy('app1:home')



#def details(request,p):
    #c=Movie.objects.filter(id=p)
    #return render(request,'details.html',{'b':c})

class MovieDetail(DetailView):
    model=Movie
    template_name="details.html"
    context_object_name="b"







#def edit(request,p):
    #b=Movie.objects.get(id=p)

    #if(request.method=="POST"):#after submission
        #form=bookform(request.POST,request.FILES,instance=b)#create form object initialize wuth values inside request.POST
        #if form.is_valid():
            #form.save()#saves form object in db  model book
            #return home(request)


    #form=bookform(instance=b)
    #return render(request,'edit.html',{'form':form})


class Movieupdate(UpdateView):
    model=Movie
    template_name="edit.html"
    fields='__all__'
    success_url=reverse_lazy('app1:home')


#def delete(request,p):
    #b=Movie.objects.get(id=p)
    #b.delete()
    #return home(request)

class Moviedelete(DeleteView):
    model=Movie
    success_url=reverse_lazy('app1:home')
    template_name="delete.html"
