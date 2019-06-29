from django.contrib import admin

# Register your models here.

from app_home.models import (StaffModel, GenderModel, GroupModel, StudentModel,
     DepartmentModel, SubjectModel, TeacherModel, Gallery, StudentResult)

admin.site.register(StaffModel)
admin.site.register(GenderModel)
admin.site.register(DepartmentModel)
admin.site.register(SubjectModel)
admin.site.register(GroupModel)
admin.site.register(StudentModel)
admin.site.register(TeacherModel)
admin.site.register(Gallery)
admin.site.register(StudentResult)
