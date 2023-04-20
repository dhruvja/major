from django.contrib import admin
from .models import Admission, AdmissionFile, Result, ResultFile, Placement, PlacementFile
from more_admin_filters import MultiSelectDropdownFilter
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseRedirect
# from pyExcelerator import * 
# from django.contrib.admin.util import lookup_field
from django.utils.html import strip_tags
from django.contrib import messages
from openpyxl import Workbook
from django.db import connection
import xlsxwriter
# from .actions import export_as_xls
# from .models import Bos,NewCoursesIntroduced, Consultants, Bookchapter, Seedmoney, Proposal, Journal, Grant,StudentsHigherEducation, AwardsAndRecognistionTeachersStudents, ListMajorMinorResearchProjects, SpecialLectureInCollege, ConferenceAttendedByTeachers, ConferenceConductedInCollege, ProfessionalDevelopmentProg, CollabrativeActivity, FundingStudentProjects, WorkshopAndSeminars, FacultyProfile

from import_export.admin import ImportExportModelAdmin, ExportActionMixin

class AdmissionFileAdminInline(admin.TabularInline):
    model = AdmissionFile

class AdmissionAdmin(ImportExportModelAdmin, ExportActionMixin,  admin.ModelAdmin):
    list_filter = [("admission_year", MultiSelectDropdownFilter)] 
    list_display = ( 'admission_year', 'CET', 'comedk', 'management', 'diploma', 'CoB_incoming', 'CoB_outgoing', 'snq', 'total')
    inlines = (AdmissionFileAdminInline, )
    exclude = ('total',)

    def export (self, request, queryset): 
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM api_admission LEFT JOIN api_placement ON api_admission.admission_year = api_placement.admission_year")
            row = cursor.fetchall()
            print(row)
            column_names = []
            cursor.execute("DESCRIBE api_admission")
            admission = cursor.fetchall()
            cursor.execute("DESCRIBE api_placement")
            placement = cursor.fetchall()
            for col in admission:
                column_names.append(col[0])
            for col in placement:
                column_names.append(col[0])
            print(column_names)
            workbook = xlsxwriter.Workbook('write_list.xlsx')
            worksheet = workbook.add_worksheet()

            for col_num, data in enumerate(column_names):
                worksheet.write(0, col_num, data)

            for row_num, row_data in enumerate(row):
                for col_num, col_data in enumerate(row_data):
                    worksheet.write(row_num+1, col_num, col_data)

            workbook.close()
            with open("write_list.xlsx", 'rb') as f:
                text = f.read()
                print(text)
                response = HttpResponse(text, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
                response['Content-Disposition'] = 'attachment; filename=write_list.xlsx'
                return response
            
    actions = [export]

    
    class Media:
        js = ('/media/hide_attribute.js',)

class AdmissionFileAdmin(admin.ModelAdmin):
    list_display = ('get_batch', 'name', 'file')
    list_filter = [("admission__batch", MultiSelectDropdownFilter)] 
    # list_filter = ("admission__batch", "admission__semester",)
    @admin.display(description='Batch', ordering='admission__batch')
    def get_batch(self, obj):
        return obj.admission.admission_year

class ResultFileAdminInline(admin.TabularInline):
    model = ResultFile

class ResultAdmin(ImportExportModelAdmin, ExportActionMixin,  admin.ModelAdmin):
    list_filter = [("admission_year", MultiSelectDropdownFilter), ("semester", MultiSelectDropdownFilter)] 
    list_display = ( 'admission_year', 'semester', 'without_backlog','single_backlog','double_backlog','triple_backlog','more_than_3_backlog','dropouts')
    inlines = (ResultFileAdminInline, )

class ResultFileAdmin(admin.ModelAdmin):
    list_display = ('get_batch', 'get_semester', 'name', 'file')
    list_filter = [("result__batch", MultiSelectDropdownFilter), ("result__semester", MultiSelectDropdownFilter)] 
    # list_filter = ("result__batch", "result__semester",)
    @admin.display(description='Batch', ordering='result__batch')
    def get_batch(self, obj):
        return obj.result.admission_year
    @admin.display(description='Semester', ordering='result__semester')
    def get_semester(self, obj):
        return obj.result.semester
    
class PlacementFileAdminInline(admin.TabularInline):
    model = PlacementFile

class PlacementAdmin(ImportExportModelAdmin, ExportActionMixin, admin.ModelAdmin):
    list_filter = [("admission_year", MultiSelectDropdownFilter), ] 
    list_display = ( 'admission_year', 'on_campus','off_campus','internship')
    inlines = (PlacementFileAdminInline, )

class PlacementFileAdmin(admin.ModelAdmin):
    list_display = ('get_batch', 'name', 'file')
    list_filter = [("placement__batch", MultiSelectDropdownFilter)] 
    # list_filter = ("result__batch", "result__semester",)
    @admin.display(description='Batch', ordering='placement__batch')
    def get_batch(self, obj):
        return obj.placement.admission_year

admin.site.register(Admission, AdmissionAdmin)
admin.site.register(AdmissionFile, AdmissionFileAdmin)
admin.site.register(Result, ResultAdmin)
admin.site.register(ResultFile, ResultFileAdmin)
admin.site.register(Placement, PlacementAdmin)
admin.site.register(PlacementFile, PlacementFileAdmin)



