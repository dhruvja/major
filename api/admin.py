from django.contrib import admin
from .models import Admission, AdmissionFile 
from more_admin_filters import MultiSelectDropdownFilter
# from .models import Bos,NewCoursesIntroduced, Consultants, Bookchapter, Seedmoney, Proposal, Journal, Grant,StudentsHigherEducation, AwardsAndRecognistionTeachersStudents, ListMajorMinorResearchProjects, SpecialLectureInCollege, ConferenceAttendedByTeachers, ConferenceConductedInCollege, ProfessionalDevelopmentProg, CollabrativeActivity, FundingStudentProjects, WorkshopAndSeminars, FacultyProfile

from import_export.admin import ImportExportModelAdmin, ExportActionMixin

class AdmissionFileAdminInline(admin.TabularInline):
    model = AdmissionFile

class AdmissionAdmin(ImportExportModelAdmin, ExportActionMixin,  admin.ModelAdmin):
    list_filter = [("batch", MultiSelectDropdownFilter), ("semester", MultiSelectDropdownFilter)] 
    list_display = ('semester', 'batch', 'cet', 'comedk', 'management', 'diploma', 'cob')
    inlines = (AdmissionFileAdminInline, )
    class Media:
        js = ('/media/hide_attribute.js',)
admin.site.register(Admission, AdmissionAdmin)



