from django.shortcuts import render, redirect
from . import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def main(request):
    if not request.user.is_authenticated:
        return redirect('login')
    staff_len = len(models.Staff.objects.all())
    late = 0
    staff_attadance = models.StaffAttandance.objects.all()
    for attadance in staff_attadance:
        staff_shift = models.StaffShift.objects.get(staff = attadance.staff.id)
        if staff_shift.shift.time_start < attadance.detatime.time():
            late += 1
    no_late =  len(staff_attadance) - late
    return render(request, 'index.html', {"staff_len":staff_len, 'late':late, 'no_late':no_late})

def createPosition(request):
    if request.method == "POST":
        models.Position.objects.create(
            name = request.POST['name']
        )
        return redirect('listposition')
    return render(request, 'positioncreate.html')


def listPosition(request):
    if not request.user.is_authenticated:
        return redirect('login')
    positions = models.Position.objects.all()
    return render(request, 'positionlist.html', {'positions': positions})

def updatePosition(request, id):
    position = models.Position.objects.get(id=id)
    if request.method == "POST":
        position.name = request.POST['name']
        position.save()
        return redirect('listposition')
    return render(request, 'positioncreate.html', {'position':position})

def deletePositon(request, id):
    models.Position.objects.get(id=id).delete()
    return redirect('listposition')

def createStaff(request):
    positions = models.Position.objects.all()
    shifts = models.Shift.objects.all()
    if request.method == "POST":
        position = models.Position.objects.get(id=request.POST['position'])
        shift = models.Shift.objects.get(id=request.POST['shift'])
        staff = models.Staff.objects.create(
            f_name = request.POST['f_name'],
            l_name = request.POST['l_name'],
            number = request.POST['number'],
            age = request.POST['age'],
            position = position
        )
        models.StaffShift.objects.create(
            staff = staff,
            shift = shift
        )
        return redirect('stafflist')
    return render(request, 'staffcreate.html', {'positions':positions, 'shifts':shifts})


def staffList(request):
    if not request.user.is_authenticated:
        return redirect('login')
    staffes = models.Staff.objects.all()
    return render(request, 'stafflist.html', {'staffes':staffes})

def staffUpdate(request, id):
    positions = models.Position.objects.all()
    staff = models.Staff.objects.get(id=id)
    shift = models.StaffShift.objects.get(staff=staff).shift
    shifts = models.Shift.objects.all()
    position = staff.position
    if request.method == 'POST':
        position = models.Position.objects.get(id = request.POST['position'])
        shift = models.Shift.objects.get(id=request.POST['shift'])
        staff_shift = models.StaffShift.objects.get(staff = staff)
        staff.f_name = request.POST['f_name']
        staff.l_name = request.POST['l_name']
        staff.number = request.POST['number']
        staff.age = request.POST['age']
        staff_shift = request.POST['shift']
        staff_shift = request.POST['position']
        staff.save()
        staff_shift.save()
        return redirect('stafflist')
    context = {'staff':staff, 'positions':positions, 'shifts':shifts, 'position':position, 'shift':shift}
    return render(request, 'staffcreate.html', context)

def staffDelete(request, id):
    models.Staff.objects.get(id=id).delete()
    return redirect('stafflist')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
        else:
            return redirect('login')
    return render(request, 'login.html')


def log_out(request):
    logout(request)
    return redirect('login')

def listAttadance(request):
    if not request.user.is_authenticated:
        return redirect('login')
    staffes = models.Staff.objects.all()
    return render(request, "visit/createvisit.html", {'staffes':staffes})

def createAttadance(request, id):
    staff = models.Shift.objects.get(id=id)
    models.StaffAttandance.objects.create(
            staff = staff
        )
    return redirect('listattadance')

def visitList(request):
    if not request.user.is_authenticated:
        return redirect('login')
    attadances = models.StaffAttandance.objects.all()
    for attadance in attadances:
        staff_shift = models.StaffShift.objects.get(staff = attadance.staff.id)
        if staff_shift.shift.time_start < attadance.detatime.time():
            attadance.state = False
        else:
            attadance.state = True
        attadance.staff_shift = models.StaffShift.objects.get(staff = attadance.staff.id)
    return render(request, 'visit.html', {'attadances':attadances})

def createShift(request):
    if request.method == 'POST':
        models.Shift.objects.create(
        name = request.POST['name'],
        time_start = request.POST['time_start'],
        time_stop = request.POST['time_stop']
        )
        return redirect('listshift')
    return render(request, 'createshift.html')

def listShift(request):
    shifts = models.Shift.objects.all()
    return render(request,'listshift.html', {'shifts':shifts})

def deleteshift(request, id):
    models.Shift.objects.get(id=id).delete()
    return redirect('listshift')