from django.shortcuts import render
from CRUDOperation.models import locationModel
from CRUDOperation.models import dcompanyModel
from django.contrib import messages
from CRUDOperation.forms import locforms
from CRUDOperation.forms import comforms
from django.db import connection

def showlocation(request):
    showall=locationModel.objects.all()
    return render(request,'loc.html',{"data":showall})

def Insertloc(request):
    if request.method=="POST":
        if request.POST.get('location_id') and request.POST.get('street_add') and request.POST.get('city') and request.POST.get('state') and request.POST.get('contry'):
            saverecord=locationModel()
            saverecord.location_id=request.POST.get('location_id')
            saverecord.street_add=request.POST.get('street_add')
            saverecord.city=request.POST.get('city')
            saverecord.state=request.POST.get('state')
            saverecord.contry=request.POST.get('contry')
            saverecord.save()
            messages.success(request, 'street_add '+saverecord.street_add+ ' Is saved successfully!!!')
            return render(request,'Insert_location.html')
    else:
        return render(request,'Insert_location.html')

def Editloc(request,location_id):
    editlocobj=locationModel.objects.get(location_id=location_id)
    return render(request,'Edit_location.html',{"locationModel":editlocobj})

def updateloc(request,location_id):
    Updateloc=locationModel.objects.get(location_id=location_id)
    form=locforms(request.POST,instance=Updateloc)
    if form.is_valid():
        form.save()
        messages.success(request,'Location Information Updated Successfully!!!')
        return render(request,'Edit_location.html',{"locationModel":Updateloc})

def Delloc(request,location_id):
    delloc=locationModel.objects.get(location_id=location_id)
    delloc.delete()
    showall=locationModel.objects.all()
    return render(request,"loc.html",{"data":showall})

def showcom(request):
    showallcom=dcompanyModel.objects.all()
    return render(request,'company.html',{"data":showallcom})

def Insertcom(request):
    if request.method=="POST":
        if request.POST.get('company_id') and request.POST.get('company_name') and request.POST.get('street_add') and request.POST.get('highest_no_worker') and request.POST.get('region_id') and request.POST.get('company_name'):
            saverecord=dcompanyModel()
            saverecord.company_id=request.POST.get('company_id')
            saverecord.company_type=request.POST.get('company_type')
            saverecord.street_add=request.POST.get('street_add')
            saverecord.highest_no_worker=request.POST.get('highest_no_worker')
            saverecord.region_id=request.POST.get('region_id')
            saverecord.company_name=request.POST.get('company_name')
            saverecord.save()
            messages.success(request, 'company_name '+saverecord.company_name+ ' Is saved successfully!!!')
            return render(request,'Insert_company.html')
    else:
        return render(request,'Insert_company.html')

def Editcom(request,company_id):
    editcomobj=dcompanyModel.objects.get(company_id=company_id)
    return render(request,'Edit_company.html',{"dcompanyModel":editcomobj})

def updatecom(request,company_id):
    Updatecom=dcompanyModel.objects.get(company_id=company_id)
    form=comforms(request.POST,instance=Updatecom)
    if form.is_valid():
        form.save()
        messages.success(request,'Company Information Updated Successfully!!!')
        return render(request,'Edit_company.html',{"dcompanyModel":Updatecom})

def Delcom(request,company_id):
    delcom=dcompanyModel.objects.get(company_id=company_id)
    delcom.delete()
    showallcom=dcompanyModel.objects.all()
    return render(request,"company.html",{"data":showallcom})

def runquery(request):
    raw_query = "select * from labor_wages_t18.company_details where company_type='Private'"
    cursor = connection.cursor()
    cursor.execute(raw_query)
    data = cursor.fetchall()
    return render(request,"query.html",{"data":data})

def runquery1(request):
    raw_query = "select * from labor_wages_t18.company_details where company_type='Government'"
    cursor = connection.cursor()
    cursor.execute(raw_query)
    data = cursor.fetchall()
    return render(request,"query1.html",{"data":data})

def runquery2(request):
    raw_query = "select * from labor_wages_t18.company_details where highest_no_worker>400"
    cursor = connection.cursor()
    cursor.execute(raw_query)
    data = cursor.fetchall()
    return render(request,"query2.html",{"data":data})




