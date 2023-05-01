from django.contrib import admin
from .models import Admission, AdmissionFile, StudentResult, Placement, PlacementFile, StudentProfile, Subject
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
from django.db.models import Count, Case, When, Q
from django.db import models
from django.views.generic import TemplateView
from django.urls import path, reverse
from django.views.generic.detail import SingleObjectMixin, DetailView
from django.utils.html import format_html
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

# class ResultFileAdminInline(admin.TabularInline):
#     model = ResultFile

# class ResultAdmin(ImportExportModelAdmin, ExportActionMixin,  admin.ModelAdmin):
#     list_filter = [("admission_year", MultiSelectDropdownFilter), ("semester", MultiSelectDropdownFilter)] 
#     list_display = ( 'admission_year', 'semester', 'without_backlog','single_backlog','double_backlog','triple_backlog','more_than_3_backlog','dropouts')
#     # inlines = (ResultFileAdminInline, )

# class ResultFileAdmin(admin.ModelAdmin):
#     list_display = ('get_batch', 'get_semester', 'name', 'file')
#     list_filter = [("result__batch", MultiSelectDropdownFilter), ("result__semester", MultiSelectDropdownFilter)] 
#     # list_filter = ("result__batch", "result__semester",)
#     @admin.display(description='Batch', ordering='result__batch')
#     def get_batch(self, obj):
#         return obj.result.admission_year
#     @admin.display(description='Semester', ordering='result__semester')
#     def get_semester(self, obj):
#         return obj.result.semester
    
class PlacementFileAdminInline(admin.TabularInline):
    model = PlacementFile

class StudentResultInline(admin.TabularInline):
    model = StudentResult

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

# class StudentProfileAdmin(admin.ModelAdmin):
#     list_display = ('usn', 'admission_year', 'admission_quota')
   

# class StudentProfileAdmin(admin.ModelAdmin):
#     list_display = ('admission_year', 'num_cet', 'num_management', 'num_comedk', 'num_snq')

#     def get_queryset(self, request):
#         queryset = super().get_queryset(request)
#         distinct_values = []
#         values = list(queryset.values_list())
#         print(values)
#         # for val in values:
#         #     if 
#         queryset = queryset.annotate(
#             num_cet=Count(
#                 Case(
#                     When(admission_quota='CET', then=1)
#                 )
#             ),
#             num_management=Count(
#                 Case(
#                     When(admission_quota='MANAGEMENT', then=1)
#                 )
#             ),
#             num_comedk=Count(
#                 Case(
#                     When(admission_quota='COMED-K', then=1)
#                 )
#             ),
#             num_snq=Count(
#                 Case(
#                     When(admission_quota='SNQ', then=1)
#                 )
#             ),
#         )
#         # for query in queryset:
#             # print(query.update(num_cet=10))
#         # query = queryset.filter(admission_year = 2019)
#         # user_dict = dict(queryset)
#         # print("This is user dict", queryset, user_dict)
#         # update(admission_year = 2020)
#         # query.update(admission_year = 2020)
#         print(queryset[0].admission_year)
#         print("This is queryset", queryset.distinct())
#         return queryset

#     def num_cet(self, obj):
#         return obj.num_cet
#     num_cet.short_description = 'CET'

#     def num_management(self, obj):
#         return obj.num_management
#     num_management.short_description = 'MANAGEMENT'

#     def num_comedk(self, obj):
#         return obj.num_comedk
#     num_comedk.short_description = 'COMED-K'

#     def num_snq(self, obj):
#         return obj.num_snq
#     num_snq.short_description = 'SNQ'

#     def has_add_permission(self, request, obj=None):
#         return False

#     def has_change_permission(self, request, obj=None):
#         return False

#     def has_delete_permission(self, request, obj=None):
#         return False
    

class QuotaAggregateView(DetailView):
    template_name = "admin/quota/detail.html"
    model = StudentProfile 

    def get_context_data(self, *args, **kwargs):
        context = super(QuotaAggregateView,
             self).get_context_data(*args, **kwargs)
        print("This is context", context)
        context["category"] = "MISC"       
        queryset = super().get_queryset()
        queryset = queryset.values('admission_year').annotate(
            cet_count=Count('admission_quota', filter=Q(admission_quota='CET')),
            management_count=Count('admission_quota', filter=Q(admission_quota='MANAGEMENT')),
            comedk_count=Count('admission_quota', filter=Q(admission_quota='COMED-K')),
            snq_count=Count('admission_quota', filter=Q(admission_quota='SNQ')),
        ).order_by('admission_year')
        # convert ValuesQuerySet to QuerySet
        queryset = list(queryset)
        print("This is queryset", queryset)
        context['aggregate'] = queryset
        return {
            **super().get_context_data(**kwargs),
            **admin.site.each_context(self.request),
            "opts": self.model._meta,
            "context": context
        }

class PlacementAggregateView(DetailView):
    template_name = "admin/placement/detail.html"
    model = StudentProfile 

    def get_context_data(self, *args, **kwargs):
        context = super(PlacementAggregateView,
             self).get_context_data(*args, **kwargs)
        print("This is context", context)
        context["category"] = "MISC"       
        queryset = super().get_queryset()
        queryset = queryset.values('admission_year').annotate(
            on_campus_count=Count('placement', filter=Q(placement='ON_CAMPUS')),
            off_campus_count=Count('placement', filter=Q(placement='OFF_CAMPUS')),
            internship_count=Count('placement', filter=Q(placement='INTERNSHIP')),
        ).order_by('admission_year')
        # convert ValuesQuerySet to QuerySet
        queryset = list(queryset)
        print("This is queryset", queryset)
        context['aggregate'] = queryset
        return {
            **super().get_context_data(**kwargs),
            **admin.site.each_context(self.request),
            "opts": self.model._meta,
            "context": context
        }

@admin.register(StudentProfile)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['usn', 'admission_year', 'admission_quota', 'quota_aggregate', 'placement_aggregate']
    inlines = (StudentResultInline, )

    def get_urls(self):
        return [
            path(
                "<pk>/quota",
                self.admin_site.admin_view(QuotaAggregateView.as_view()),
                name=f"quota_aggregate",
            ),
            path(
                "<pk>/placement",
                self.admin_site.admin_view(PlacementAggregateView.as_view()),
                name=f"placement_aggregate",
            ),
            *super().get_urls(),
        ]

    def quota_aggregate(self, obj: StudentResult) -> str:
        url = reverse("admin:quota_aggregate", args=[obj.pk])
        return format_html(f'<a href="{url}">📝</a>')
    
    def placement_aggregate(self, obj: StudentResult) -> str:
        url = reverse("admin:placement_aggregate", args=[obj.pk])
        return format_html(f'<a href="{url}">📝</a>')

# admin.site.register(Admission, AdmissionAdmin)
# admin.site.register(AdmissionFile, AdmissionFileAdmin)
admin.site.register(StudentResult)
# admin.site.register(ResultFile, ResultFileAdmin)
# admin.site.register(Placement, PlacementAdmin)
# admin.site.register(PlacementFile, PlacementFileAdmin)
# admin.site.register(StudentProfile, StudentProfileAdmin)
admin.site.register(Subject)


