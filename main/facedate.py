import random
from faker import Faker
from main.models import Position, Shift, Staff, StaffShift, StaffAttandance

fake = Faker()

def create_fake_positions(n=5):
    for _ in range(n):
        position = Position.objects.create(name=fake.job())

def create_fake_shifts(n=5):
    for _ in range(n):
        time_start = fake.time()
        time_stop = fake.time()
        shift = Shift.objects.create(name=fake.word(), time_start=time_start, time_stop=time_stop)

def create_fake_staff(n=10):
    positions = list(Position.objects.all())

    for _ in range(n):
        f_name = fake.first_name()
        l_name = fake.last_name()
        age = random.randint(20, 60)
        number = fake.phone_number()
        position = random.choice(positions) if positions else None
        staff = Staff.objects.create(f_name=f_name, l_name=l_name, age=age, number=number, position=position)

def create_fake_staff_shifts(n=10):
    staff_members = list(Staff.objects.all())
    shifts = list(Shift.objects.all())
    
    if not staff_members or not shifts:
        return
    
    for _ in range(n):
        staff = random.choice(staff_members)
        shift = random.choice(shifts)
        staff_shift = StaffShift.objects.create(staff=staff, shift=shift)

def create_fake_attendance(n=10):
    staff_members = list(Staff.objects.all())
    
    if not staff_members:
        return
    for _ in range(n):
        staff = random.choice(staff_members)
        attendance = StaffAttandance.objects.create(staff=staff)

def populate_database():
    create_fake_positions()
    create_fake_shifts()
    create_fake_staff()
    create_fake_staff_shifts()
    create_fake_attendance()
