"""CRUDOperation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.showlocation,name="showlocation"),
    path('Insert',views.Insertloc,name="Insertloc"),
    path('Edit/<int:location_id>',views.Editloc,name="Editloc"),
    path('Update/<int:location_id>',views.updateloc,name="updateloc"),
    path('Delete/<int:location_id>',views.Delloc,name="Delloc"),
    
    path('company/',views.showcom,name="showcom"),
    path('Insertcom/',views.Insertcom,name="Insertcom"),
    path('Editcom/<int:company_id>',views.Editcom,name="Editcom"),
    path('Updatecom/<int:company_id>',views.updatecom,name="updatecom"),
    path('Deletecom/<int:company_id>',views.Delcom,name="Deletecom"),

    path('query/',views.runquery,name="runquery"),
    path('query1/',views.runquery1,name="runquery1"),
    path('query2/',views.runquery2,name="runquery2"),
]
