from django.shortcuts import render, HttpResponseRedirect
from home_page.forms import StudentRegistration

from home_page.models import Student
from .models import Student

from django.contrib import messages
# Create your views here.




# THIS IS FUNCTION FOR INSERTING DATA 

def index(request):
    if request.method == 'POST':
        form_object = StudentRegistration(request.POST)
        if form_object.is_valid():
            name = form_object.cleaned_data['name']
            email = form_object.cleaned_data['email']
            password = form_object.cleaned_data['password']
            insert = Student(name=name, email=email, password=password)
            insert.save()
            messages.success(request, 'Data Sent Successfully')

            form_object = StudentRegistration()
 
            # form_object.save()

    else:
        form_object = StudentRegistration()
    stud = Student.objects.all()

    # return HttpResponse("This is contact Page")
    return render(request, 'index.html', {'form':form_object, 'stu':stud})
    

# THIS FUNCTION UPDATE DATA 

def update_data(request, id):
    
    if request.method == 'POST':
        pi = Student.objects.get(pk=id)
        form_obj = StudentRegistration(request.POST, instance=pi)
        if form_obj.is_valid():
            form_obj.save()
            messages.success(request, 'Updated Successfully')

    else:
        pi = Student.objects.get(pk=id)
        form_obj = StudentRegistration(instance=pi)

    return render(request, 'updatestudent.html', {'form': form_obj})


# this function wil delete data 
def delete_data(request, id):
    if request.method == 'POST':
        pi = Student.objects.get(pk=id)
        pi.delete()
        messages.error(request, 'Deleted Successfully')

        return HttpResponseRedirect('/')




# def update(request):
#     # return HttpResponse("This is contact Page")
#     return render(request, 'updatestudent.html')