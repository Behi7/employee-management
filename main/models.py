from django.db import models

class Position(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Shift(models.Model):
    name = models.CharField(max_length=255)
    time_start = models.TimeField()
    time_stop = models.TimeField()

    def __str__(self) -> str:
        return f"{self.name}: {self.time_start} - {self.time_stop}"


class Staff(models.Model):
    f_name = models.CharField(max_length=144)
    l_name = models.CharField(max_length=255)
    age = models.IntegerField()
    number = models.CharField(max_length=255)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f"{self.f_name} {self.l_name} - {self.position}"


class StaffShift(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.staff}-{self.shift}"


class StaffAttandance(models.Model):
    detatime = models.DateTimeField(auto_now_add=True, blank=True)
    staff = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f"{self.staff}-{self.detatime}"
