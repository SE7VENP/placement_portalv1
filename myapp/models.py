from django.db import models
from django.utils.safestring import mark_safe
# Create your models here.
class login_table(models.Model):
    email_id=models.EmailField()
    phone_no=models.IntegerField()
    dp=models.ImageField(upload_to="photos")
    password = models.CharField(max_length=300, default="admin")
    Role=models.CharField(max_length=100)
    status=(
        (0,'inactive'),
        (1,'active'),
        )
    Status=models.CharField(max_length=10,choices=status)


    def admin_photos(self):
        return mark_safe('<img src ="{}" width ="100"/>'.format(self.dp.url))

    admin_photos.allow_tags = True

    def __str__(self):
        return self.email_id



class state_table(models.Model):
    state_name=models.CharField(max_length=25)
    def __str__(self):
        return self.state_name





class city(models.Model):
    city_name=models.CharField(max_length=25)
    state_id=models.ForeignKey(state_table,on_delete=models.CASCADE)

    def __str__(self):
        return self.city_name





class area_table(models.Model):
    city_id=models.ForeignKey(city,on_delete=models.CASCADE)
    state_id=models.ForeignKey(state_table,on_delete=models.CASCADE)
    area_name=models.CharField(max_length=25)
    def __str__(self):
        return self.area_name


class university_table(models.Model):
    university_name=models.CharField(max_length=25)

    def __str__(self):
        return self.university_name




class college_table(models.Model):
    college_name=models.CharField(max_length=25)
    university_id=models.ForeignKey(university_table,on_delete=models.CASCADE)

    def __str__(self):
        return self.college_name



class branch_table(models.Model):
    college_id=models.ForeignKey(college_table,on_delete=models.CASCADE)
    university_id=models.ForeignKey(university_table,on_delete=models.CASCADE)
    branch_name=models.CharField(max_length=25)

    def __str__(self):
        return self.branch_name


class user_detail_table(models.Model):
    l_id=models.ForeignKey(login_table,on_delete=models.CASCADE)
    name=models.CharField(max_length=25)
    Enrollment=models.CharField(max_length=25,default="")
    passoutyear=models.IntegerField(default=2020)
    dob=models.DateField()
    address=models.TextField()
    area_id=models.ForeignKey(area_table,on_delete=models.CASCADE)
    city_id=models.ForeignKey(city,on_delete=models.CASCADE)
    state_id=models.ForeignKey(state_table,on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class company_details(models.Model):
    l_id=models.ForeignKey(login_table,on_delete=models.CASCADE)
    company_name=models.CharField(max_length=50)
    company_type=models.CharField(max_length=50)
    company_address=models.TextField()
    company_webiste=models.CharField(max_length=50)
    founded_year=models.IntegerField()
    company_support_mail=models.EmailField()
    company_support_phone=models.IntegerField()
    company_size=models.IntegerField()
    company_city = models.CharField(max_length=50, default="")
    company_area = models.CharField(max_length=50, default="")


    def __str__(self):
        return self.company_name

class skills_table(models.Model):
    skills_name=models.CharField(max_length=25)

    def __str__(self):
        return self.skills_name

class requirement_jobs(models.Model):
    company_id=models.ForeignKey(company_details,on_delete=models.CASCADE)
    job_type=models.CharField(max_length=35)
    job_description=models.TextField()
    vacancy=models.IntegerField()
    basic_pay=models.IntegerField()
    date=models.DateField(auto_now=True, editable=False)
    time=models.TimeField(auto_now=True, editable=False)
    job_skill = models.CharField(max_length=35, default="")
    status=(
        ("OPEN","OPEN"),
        ("CLOSED","CLOSED"),
    )
    Status=models.CharField(choices=status,max_length=10)

    def __str__(self):
        return self.job_type

class user_skill_table(models.Model):
    l_id=models.ForeignKey(login_table,on_delete=models.CASCADE)
    skill_id=models.ForeignKey(skills_table,on_delete=models.CASCADE)
    skill_level = models.IntegerField(default=25)

class 	resume_table(models.Model):
    l_id=models.ForeignKey(login_table,on_delete=models.CASCADE)
    file_path=models.FileField(upload_to='file')

    def file(self):
        return mark_safe('<img src ="{}" width ="100"/>'.format(self.file_path.url))

    file.allow_tags = True






class feedback(models.Model):
    name=models.CharField(max_length=50,default="")
    email=models.EmailField(default="")
    comment=models.CharField(max_length=300)

    def __str__(self):
        return self.name

class appliedjob(models.Model):
    l_id = models.ForeignKey(login_table, on_delete=models.CASCADE)
    applied_job_id = models.ForeignKey(requirement_jobs, on_delete=models.CASCADE)
    candidate_details = models.ForeignKey(user_detail_table, on_delete=models.CASCADE)
    applied_company_id = models.ForeignKey(company_details, on_delete=models.CASCADE,default="")
    applied_datetime = models.DateTimeField(auto_now=True, editable=False)
    candidate_resume = models.ForeignKey(resume_table, on_delete=models.CASCADE,default="")
    job_status = (
        ("Under Review", "Under Review"),
        ("Shown Interest", "Shown Interest"),
        ("Rejected", "Rejected"),
    )
    applied_job_status = models.CharField(max_length=50,default="Under Review",choices=job_status)
    show_interest_button = models.BooleanField(default=True)
    rejected = models.BooleanField(default=False)


class feedbackpagesubmit(models.Model):
    name=models.CharField(max_length=50,default="")
    email=models.EmailField(default="")
    comment=models.CharField(max_length=300)

    def __str__(self):
        return self.name