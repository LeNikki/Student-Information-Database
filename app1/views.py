from django.shortcuts import render, redirect #default
from django.contrib import messages
from django.db import connection
from .forms import StudentsForm    #use app name, class name
from .models import *
#from .filters import StdFilter

# Create your views here.
def std (request):
    if request.method == "POST":
        form = StudentsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Form has been submitted')
                return redirect ('home')
            except:
                pass
    else:
        form = StudentsForm() 
        return render(request, 'index.html', {'form' : form})
        #return render_to_response("index.html", {'form':form}, context_instance=RequestContext(request))

#def search (request, prim_key):
    #WA PA NAHUMAN,
    #search = Search.objects
    #myfilter = StdFilter()

def data (request):
    #if 'search' in request.GET:
    #    search = request.GET['search']
    #    data = App1Students.objects.filter(title__icontains = search)
   # else:  
      # data = App1Students.objects.all()
        #context = {
        #    'no_field':data.no_field, 'sid':data.sid, 'f_name':data.f_name, 
        #    'l_name':data.l_name, 'email': data.email, 'contact': data.contact,
        #    'yr_sec': data.yr_sec,
        # }
         data = App1Students.objects.all()
         context = {
            'data':data
        }
         return render (request, 'students.html', context)

#def searchbyval (request):
#    cursor = connection.cursor()
#    cursor.execute(call, 'SearchByVal()')
 #   results = cursor.fetchall() #fetches all methods
  #  return render (request, 'searchbyval.html', {'App1Students': results})

def delete (request, no_field):
    data = App1Students.objects.get(no_field = no_field)
    data.delete()
    return redirect ("data")

def edit (request, no_field):
    data = App1Students.objects.get(no_field = no_field)
    form = StudentsForm (request.POST, instance = data)  #it will save it as that instance instead of creating a new one 

    
    if form.is_valid():
        try:
            data = form.save(commit = False)
            data.save()
            messages.success(request, 'Form has been submitted')
            return redirect ('data')
        except:
            pass
     
    return render (request, 'index.html', {'form': form})

def search (request):
    
    if request.method == 'POST':
        searched = request.POST['searched']
        data = App1Students.objects.filter( l_name = searched )
        return render (request, 'search.html', {'searched': searched, 'data':data})
