from django.shortcuts import render
from .models import Reminder_mod
from django.forms import ModelForm

# Create your views here.
class Reminder_form(ModelForm):
    class Meta():
        model=Reminder_mod
        fields='__all__'


def get_home(request):
    return render(request,"home.html",{})
def add_reminder(request):
    if request.method=='GET':
        ob=Reminder_form()
        return render(request,"add.html",{'form':ob})
    if request.method=='POST':
        ob=Reminder_form(request.POST)
        print(ob.errors)
        if ob.is_valid():
            r_Name=ob.cleaned_data['name']
            r_Date=ob.cleaned_data['date']
            r_Time=ob.cleaned_data['time']
            e=Reminder_mod(name=r_Name,date=r_Date,time=r_Time)
            e.save()
            print("saved")
            print(r_Name)
            print(r_Date)
            print(r_Time)
    return render(request, "add2.html", {'form': ob})
def get_list(request):
    ob=Reminder_mod.objects.all()
    data={}
    data['object_list']=ob
    return render(request,"list.html",data)
def get_view(request,pk):
    rem=Reminder_mod.objects.get(pk=pk)
    return render(request,"view.html",{'object':rem})
def get_edit(request,pk):
    rem=Reminder_mod.objects.get(pk=pk)
    form=Reminder_form(request.POST or None,instance=rem)
    if form.is_valid():
        form.save()
        print("saved")
        return get_list(request)
    return render(request,"update.html",{'form':form})

    # ob=Book_mod.objects.get(pk=pk)
    # form = Book_form(request.POST or None, instance=ob)
    # if form.is_valid():
    #     form.save()
    #     return list(request)
    # return render(request, "edit.html", {'form': form})