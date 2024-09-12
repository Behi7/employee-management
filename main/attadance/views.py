from django.shortcuts import render, redirect
from main import models

def listAttadance(request):
    staffes = models.Staff.objects.all()
    return render(request, "visit/createvisit.html", {'staffes':staffes})

def createAttadance(request, id):
    staff = models.Staff.objects.get(id=id)
    models.StaffAttandance.objects.create(
            staff = staff
        )
    return redirect('listattadance')