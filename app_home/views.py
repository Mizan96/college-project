from django.shortcuts import render, redirect
import math
import xlrd

from app_home.models import (StudentResult, StaffModel, TeacherModel,
                             StudentModel, StaffModel, Gallery, DepartmentModel, SubjectModel)

from app_home.forms import UploadResultForm

# Create your views here.


def upload_result_fun(url):
    book = xlrd.open_workbook(url)
    sh = book.sheet_by_index(0)
    for row in range(1, sh.nrows):
        for col in range(sh.ncols):
            if StudentResult.objects.filter(roll=str(int(sh.cell_value(row, 0)))).count() == 0:
                StudentResult.objects.create(
                    roll=str(int(sh.cell_value(row, 0))),
                    bangla=sh.cell_value(row, 1),
                    english=sh.cell_value(row, 2),
                    mathematics=sh.cell_value(row, 3),
                    social_science=sh.cell_value(row, 4),
                    religion=sh.cell_value(row, 5),
                    physics=sh.cell_value(row, 6),
                    chemsitry=sh.cell_value(row, 7),
                    higher_math=sh.cell_value(row, 8),
                    biology=sh.cell_value(row, 9)
                )


def gpa(mark):
    mark = math.ceil(mark)
    if mark >= 0 and mark <= 32:
        return 'F', 0
    elif mark >= 33 and mark <= 39:
        return 'D', 1
    elif mark >= 40 and mark <= 49:
        return 'C', 2
    elif mark >= 50 and mark <= 59:
        return 'B', 3
    elif mark >= 60 and mark <= 69:
        return 'A-', 3.5
    elif mark >= 70 and mark <= 79:
        return 'A', 4
    else:
        return 'A+', 5


def index(request):
    staffs = StaffModel.objects.all()
    context = {
        'staffs': staffs
    }
    return render(request, 'index.html', context)


def about(request):
    context = {
    }
    return render(request, 'about.html', context)


def staff(request):
    staffs = StaffModel.objects.all()
    context = {
        'staffs': staffs
    }
    return render(request, 'staff.html', context)


def teacher(request):
    teachers = TeacherModel.objects.all()
    context = {
        'teachers': teachers
    }
    return render(request, 'teacher.html', context)


def submit_result(request):
    form = UploadResultForm()
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = UploadResultForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.save()
            return redirect('excelToupload', url=str(name.result_upload).split('/')[1].split('.')[0])
    return render(request, 'submitResult.html', context)
    

def excel_to_upload(requset, url):
    upload_result_fun('./media/ResultUpload/' + url + '.xlsx')
    return redirect('teacher')


def student(request):
    students = StudentModel.objects.all()
    context = {
        'students': students
    }
    return render(request, 'student.html', context)


def department(request):
    departments = DepartmentModel.objects.all()
    context = {
        'departments': departments
    }
    return render(request, 'department.html', context)


def subject(request, id):
    subjects = SubjectModel.objects.filter(department=id)
    context = {
        'subjects': subjects
    }
    return render(request, 'subject.html', context)


def gallery(request):
    images = Gallery.objects.all()
    context = {
        'images': images
    }
    return render(request, 'gallery.html', context)

def result(request, roll):
    student = StudentModel.objects.get(roll=roll)
    result = StudentResult.objects.get(roll=roll)
    # result = StudentResult.objects.get(roll='1402051')
    bangla_grade, bangla_point = gpa(result.bangla)
    english_grade, english_point = gpa(result.english)
    math_grade, math_point = gpa(result.mathematics)
    social_grade, social_point = gpa(result.social_science)
    religion_grade, religion_point = gpa(result.religion)
    physics_grade, physics_point = gpa(result.physics)
    chemistry_grade, chemistry_point = gpa(result.chemsitry)
    h_math_grade, h_math_point = gpa(result.higher_math)
    biology_grade, biology_point = gpa(result.biology)
    c_gpa = (bangla_point+english_point+math_point+social_point +
             religion_point+physics_point+chemistry_point+h_math_point)/8
    context = {
        'cgpa': format(c_gpa, '.2f'),
        'bangla_grade': bangla_grade,
        'bangla_point': format(bangla_point, '.1f'),
        'english_grade': english_grade,
        'english_point': format(english_point, '.1f'),
        'math_grade': math_grade,
        'math_point': format(math_point, '.1f'),
        'social_grade': social_grade,
        'social_point': format(social_point, '.1f'),
        'religion_grade': religion_grade,
        'religion_point': format(religion_point, '.1f'),
        'physics_grade': physics_grade,
        'physics_point': format(physics_point, '.1f'),
        'chemistry_grade': chemistry_grade,
        'chemistry_point': format(chemistry_point, '.1f'),
        'h_math_grade': h_math_grade,
        'h_math_point': format(h_math_point, '.1f'),
        'biology_grade': biology_grade,
        'biology_point': format(biology_point, '.1f'),
        'student': student
    }
    return render(request, 'result.html', context)
