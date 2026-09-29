from django.contrib import admin
from .models import login_table
from .models import state_table
from .models import city
from .models import area_table
from .models import university_table
from .models import college_table
from .models import branch_table
from .models import user_detail_table
from .models import company_details
from .models import requirement_jobs
from .models import resume_table
from .models import skills_table
from .models import user_skill_table
from .models import feedback
from .models import appliedjob
from .models import feedbackpagesubmit
# Register your models here.

class LOGIN_TABLE(admin.ModelAdmin):
    list_display = ["email_id","phone_no","admin_photos","Role","Status"]
admin.site.register(login_table,LOGIN_TABLE)


class STATE_TABLE(admin.ModelAdmin):
    list_display = ["state_name"]

admin.site.register(state_table,STATE_TABLE)

class CITY(admin.ModelAdmin):
    list_display = ["city_name","state_id"]

admin.site.register(city,CITY)

class AREA_TABLE(admin.ModelAdmin):
    list_display = ["city_id","state_id","area_name"]
admin.site.register(area_table,AREA_TABLE)

class UNIVERSITY_TABLE(admin.ModelAdmin):
    list_display = ["university_name"]
    list_filter = ["university_name"]
admin.site.register(university_table,UNIVERSITY_TABLE)

class COLLEGE_TABLE(admin.ModelAdmin):
    list_display = ["college_name","university_id"]

admin.site.register(college_table,COLLEGE_TABLE)

class BRANCH_TABLE(admin.ModelAdmin):
    list_display = ["college_id","university_id","branch_name"]
admin.site.register(branch_table,BRANCH_TABLE)

class USER_DETAIL_TABLE(admin.ModelAdmin):
    list_display = ["l_id","name","Enrollment","passoutyear","dob","address","area_id","city_id","state_id"]
admin.site.register(user_detail_table,USER_DETAIL_TABLE)

class COMPANY_DETAILS(admin.ModelAdmin):
    list_display = ["l_id","company_name","company_type","company_address","company_webiste","founded_year","company_support_mail","company_support_phone","company_size"]
admin.site.register(company_details,COMPANY_DETAILS)


class REQUIREMENT_JOBS(admin.ModelAdmin):
    list_display = ["company_id","job_type","job_skill","job_description","vacancy","basic_pay","date","time","Status"]
admin.site.register(requirement_jobs,REQUIREMENT_JOBS)

class RESUME_TABLE(admin.ModelAdmin):
    list_display = ["l_id","file_path"]
admin.site.register(resume_table,RESUME_TABLE)

class SKILLS_TABLE(admin.ModelAdmin):
    list_display = ["id","skills_name"]
admin.site.register(skills_table,SKILLS_TABLE)

class USER_SKILL_TABLE(admin.ModelAdmin):
    list_display = ["l_id","skill_id","skill_level"]
admin.site.register(user_skill_table,USER_SKILL_TABLE)

class FEEDBACK(admin.ModelAdmin):
    list_display = ["name","email","comment"]
admin.site.register(feedback,FEEDBACK)

class APPLIEDJOB(admin.ModelAdmin):
    list_display = ["l_id","applied_job_id","candidate_details","applied_company_id","applied_datetime","candidate_resume","applied_job_status","show_interest_button","rejected"]
admin.site.register(appliedjob,APPLIEDJOB)

class FEEDBACKPAGE(admin.ModelAdmin):
    list_display = ["name","email","comment"]
admin.site.register(feedbackpagesubmit,FEEDBACKPAGE)




