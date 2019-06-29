from django.db import models

# Create your models here.

class GenderModel(models.Model):
    gender = models.CharField(max_length=20)

    def __str__(self):
        return self.gender

class GroupModel(models.Model):
    group = models.CharField(max_length=20)

    def __str__(self):
        return self.group

class StaffModel(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email  = models.CharField(max_length=120)
    nid = models.CharField(max_length=20)
    gender = models.ForeignKey(GenderModel)
    address = models.TextField()
    image = models.ImageField(upload_to='staff')

    def __str__(self):
        return f'{self.name} - {self.phone} - {self.email}'


class DepartmentModel(models.Model):
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.department

class SubjectModel(models.Model):
    department = models.ForeignKey(DepartmentModel)
    subject = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.subject}'

class TeacherModel(models.Model):
    name = models.CharField(max_length=100)
    subject = models.ForeignKey(SubjectModel)
    phone = models.CharField(max_length=15)
    email  = models.CharField(max_length=120)
    nid = models.CharField(max_length=20)
    gender = models.ForeignKey(GenderModel)
    address = models.TextField()
    image = models.ImageField(upload_to='staff')

    def __str__(self):
        return f'{self.name} - {self.phone} - {self.email}'

class StudentModel(models.Model):
    name = models.CharField(max_length=100)
    father = models.CharField(max_length=100)
    mother = models.CharField(max_length=100)
    roll = models.CharField(max_length=15)
    session =  models.CharField(max_length=20)
    group = models.ForeignKey(GroupModel)
    phone = models.CharField(max_length=15)
    gender = models.ForeignKey(GenderModel)
    address = models.TextField()
    image = models.ImageField(upload_to='staff')

    def __str__(self):
        return f'{self.name} - {self.roll} - {self.session}'

class Gallery(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='gallery')
    def __str__(self):
        return f'{self.name}-{self.image}'

class StudentResult(models.Model):
    roll = models.CharField(max_length=15)
    bangla  = models.DecimalField(decimal_places=2, max_digits=5)
    english = models.DecimalField(decimal_places=2, max_digits=5)
    mathematics = models.DecimalField(decimal_places=2, max_digits=5)
    social_science = models.DecimalField(decimal_places=2, max_digits=5)
    religion = models.DecimalField(decimal_places=2, max_digits=5)
    physics = models.DecimalField(decimal_places=2, max_digits=5)
    chemsitry = models.DecimalField(decimal_places=2, max_digits=5)
    higher_math = models.DecimalField(decimal_places=2, max_digits=5)
    biology = models.DecimalField(decimal_places=2, max_digits=5)

    def __str__(self):
        return self.roll

class ResultUpload(models.Model):
    result_upload = models.FileField(upload_to='ResultUpload')

    def __str__(self):
        self.result_upload




