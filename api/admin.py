from django.contrib import admin
from .models import Admission, AdmissionFile, Result, ResultFile, Placement, PlacementFile
from more_admin_filters import MultiSelectDropdownFilter
# from .models import Bos,NewCoursesIntroduced, Consultants, Bookchapter, Seedmoney, Proposal, Journal, Grant,StudentsHigherEducation, AwardsAndRecognistionTeachersStudents, ListMajorMinorResearchProjects, SpecialLectureInCollege, ConferenceAttendedByTeachers, ConferenceConductedInCollege, ProfessionalDevelopmentProg, CollabrativeActivity, FundingStudentProjects, WorkshopAndSeminars, FacultyProfile

from import_export.admin import ImportExportModelAdmin, ExportActionMixin

class AdmissionFileAdminInline(admin.TabularInline):
    model = AdmissionFile

class AdmissionAdmin(ImportExportModelAdmin, ExportActionMixin,  admin.ModelAdmin):
    list_filter = [("batch", MultiSelectDropdownFilter), ("semester", MultiSelectDropdownFilter)] 
    list_display = ( 'batch', 'semester', 'cet', 'comedk', 'management', 'diploma', 'cob')
    inlines = (AdmissionFileAdminInline, )
    class Media:
        js = ('/media/hide_attribute.js',)

class AdmissionFileAdmin(admin.ModelAdmin):
    list_display = ('get_batch', 'get_semester', 'name', 'file')
    list_filter = [("admission__batch", MultiSelectDropdownFilter), ("admission__semester", MultiSelectDropdownFilter)] 
    # list_filter = ("admission__batch", "admission__semester",)
    @admin.display(description='Batch', ordering='admission__batch')
    def get_batch(self, obj):
        return obj.admission.batch
    @admin.display(description='Semester', ordering='admission__semester')
    def get_semester(self, obj):
        return obj.admission.semester

class ResultFileAdminInline(admin.TabularInline):
    model = ResultFile

class ResultAdmin(ImportExportModelAdmin, ExportActionMixin,  admin.ModelAdmin):
    list_filter = [("batch", MultiSelectDropdownFilter), ("semester", MultiSelectDropdownFilter)] 
    list_display = ( 'batch', 'semester', 'without_backlog','single_backlog','double_backlog','triple_backlog','more_than_3_backlog','dropouts')
    inlines = (ResultFileAdminInline, )

class ResultFileAdmin(admin.ModelAdmin):
    list_display = ('get_batch', 'get_semester', 'name', 'file')
    list_filter = [("result__batch", MultiSelectDropdownFilter), ("result__semester", MultiSelectDropdownFilter)] 
    # list_filter = ("result__batch", "result__semester",)
    @admin.display(description='Batch', ordering='result__batch')
    def get_batch(self, obj):
        return obj.result.batch
    @admin.display(description='Semester', ordering='result__semester')
    def get_semester(self, obj):
        return obj.result.semester
    
class PlacementFileAdminInline(admin.TabularInline):
    model = PlacementFile

class PlacementAdmin(ImportExportModelAdmin, ExportActionMixin, admin.ModelAdmin):
    list_filter = [("batch", MultiSelectDropdownFilter), ] 
    list_display = ( 'batch', 'on_campus','off_campus','internship')
    inlines = (PlacementFileAdminInline, )

class PlacementFileAdmin(admin.ModelAdmin):
    list_display = ('get_batch', 'name', 'file')
    list_filter = [("placement__batch", MultiSelectDropdownFilter)] 
    # list_filter = ("result__batch", "result__semester",)
    @admin.display(description='Batch', ordering='placement__batch')
    def get_batch(self, obj):
        return obj.placement.batch

admin.site.register(Admission, AdmissionAdmin)
admin.site.register(AdmissionFile, AdmissionFileAdmin)
admin.site.register(Result, ResultAdmin)
admin.site.register(ResultFile, ResultFileAdmin)
admin.site.register(Placement, PlacementAdmin)
admin.site.register(PlacementFile, PlacementFileAdmin)



