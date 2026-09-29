from django.shortcuts import render, redirect
from .models import login_table, state_table, city, area_table, branch_table, university_table, college_table, user_detail_table, resume_table, skills_table, user_skill_table, company_details, requirement_jobs, appliedjob, feedback, feedbackpagesubmit
from django.contrib import messages
from django.http import HttpResponseRedirect

#import paginator
from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger,
)
# Create your views here.

def index(request):
    try:
        uid = request.session['log_id']
        # usertypecheck = login_table.objects.get(l_id=uid)
        try:
            usertypecheck = login_table.objects.get(id=uid)
        except login_table.DoesNotExist:
            usertypecheck = None

        Comp = False
        if usertypecheck.Role == "company":
            Comp = True

        try:
            profiledata = user_detail_table.objects.get(l_id=uid)
        except user_detail_table.DoesNotExist:
            profiledata = None

        try:
            companydata = company_details.objects.get(l_id=uid)
        except company_details.DoesNotExist:
            companydata = None



        details = {
            'Comp': Comp,
            'profiledata': profiledata,
            'companydata': companydata,
           }

        return render(request, 'index.html', details)
    except:
        pass
    return render(request, 'index.html')

def about(request):
    try:
        uid = request.session['log_id']
        # usertypecheck = login_table.objects.get(l_id=uid)
        try:
            usertypecheck = login_table.objects.get(id=uid)
        except login_table.DoesNotExist:
            usertypecheck = None

        Comp = False
        if usertypecheck.Role == "company":
            Comp = True

        try:
            profiledata = user_detail_table.objects.get(l_id=uid)
        except user_detail_table.DoesNotExist:
            profiledata = None

        try:
            companydata = company_details.objects.get(l_id=uid)
        except company_details.DoesNotExist:
            companydata = None



        details = {
            'Comp': Comp,
            'profiledata': profiledata,
            'companydata': companydata,
           }

        return render(request, 'about.html', details)
    except:
        pass
    return render(request, 'about.html')

def contact(request):
    try:
        uid = request.session['log_id']
        # usertypecheck = login_table.objects.get(l_id=uid)
        try:
            usertypecheck = login_table.objects.get(id=uid)
        except login_table.DoesNotExist:
            usertypecheck = None

        Comp = False
        if usertypecheck.Role == "company":
            Comp = True

        try:
            profiledata = user_detail_table.objects.get(l_id=uid)
        except user_detail_table.DoesNotExist:
            profiledata = None

        try:
            companydata = company_details.objects.get(l_id=uid)
        except company_details.DoesNotExist:
            companydata = None



        details = {
            'Comp': Comp,
            'profiledata': profiledata,
            'companydata': companydata,
           }

        return render(request, 'contact.html', details)
    except:
        pass
    return render(request, 'contact.html')

def contactus(request):
    if request.method == 'POST':
        name = request.POST.get("Name")
        email = request.POST.get("Email")
        message = request.POST.get("message")

        contactdata = feedback(name=name,email=email,comment=message)
        contactdata.save()
        messages.success(request, 'Your Response recorded successfully')
        return redirect(contact)

def signup(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def viewdata(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        file = request.FILES['dp']
        role = request.POST.get("usertype")

        logindata = login_table(email_id=email, phone_no=phone, password=password,
                                dp=file, Role=role, Status=1)
        logindata.save()
        messages.success(request, 'Data Inserted Successfully. you can login now')
    else:
        messages.error(request, 'error occured')

    return render(request, 'index.html')


def checklogin(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        try:
            user = login_table.objects.get(email_id=username, password=password)
            request.session['log_user'] = user.email_id
            request.session['log_id'] = user.id
            request.session.save()

        except login_table.DoesNotExist:
            user = None

        if user is not None:
            print("successfully logged in")
            return redirect(index)  # ,context
        else:
            print("not logged in")
            messages.error(request, 'Invalid USER ID')
            return redirect(login)

def logout(request):
    try:
        del request.session['log_user']
        del request.session['log_id']
    except:
        pass
    return redirect(index)


def completeprofileuser(request):
    try:
        uid = request.session['log_id']
        try:
            usertypecheck = login_table.objects.get(id=uid)
        except login_table.DoesNotExist:
            usertypecheck = None

        Comp = False
        if usertypecheck.Role == "company":
            Comp = True

        try:
            profiledata = user_detail_table.objects.get(l_id=uid)
        except user_detail_table.DoesNotExist:
            profiledata = None

        try:
            companydata = company_details.objects.get(l_id=uid)
        except company_details.DoesNotExist:
            companydata = None

        statedetail = state_table.objects.all()
        citydetail = city.objects.all()
        areadetail = area_table.objects.all()

        details = {
            'Comp': Comp,
            'profiledata': profiledata,
            'companydata': companydata,
            'statedetail': statedetail,
            'citydetail': citydetail,
            'areadetail': areadetail,
           }

        return render(request, 'completeprofileuser.html', details)
    except:
        pass
    return render(request, 'completeprofileuser.html')

def completeprofile(request):
    uid = request.session['log_id']
    if request.method == 'POST':
        uname = request.POST.get("name")
        enroll = request.POST.get("enroll")
        passout = request.POST.get("passoutyear")
        uaddress = request.POST.get("address")
        udob = request.POST.get("dob")
        uarea = request.POST.get("areaname")
        ucity = request.POST.get("cityname")
        ustate = request.POST.get("statename")

        userdata = user_detail_table(l_id=login_table(id=uid), name=uname,Enrollment=enroll,passoutyear=passout, dob=udob, address=uaddress, area_id=area_table(id=uarea), city_id=city(id=ucity), state_id=state_table(id=ustate))
        userdata.save()
        messages.success(request, 'Data Inserted Successfully.')
        return redirect(index)
    else:
        messages.error(request, 'error occured')


def profilepage(request):
    try:
        uid = request.session['log_id']

        statedetail = state_table.objects.all()
        citydetail = city.objects.all()
        areadetail = area_table.objects.all()
        skilldetail = skills_table.objects.all()
        userskills = user_skill_table.objects.filter(l_id=uid)

        try:
            resumeinfo = resume_table.objects.get(l_id=uid)
        except resume_table.DoesNotExist:
            resumeinfo = None

        try:
            usertypecheck = login_table.objects.get(id=uid)
        except login_table.DoesNotExist:
            usertypecheck = None

        Comp = False
        if usertypecheck.Role == "company":
            Comp = True

        try:
            profiledata = user_detail_table.objects.get(l_id=uid)
        except user_detail_table.DoesNotExist:
            profiledata = None



        details = {
            'statedetail': statedetail,
            'citydetail': citydetail,
            'areadetail': areadetail,
            'profiledata': profiledata,
            'Comp': Comp,
            'resumeinfo': resumeinfo,
            'skilldetail': skilldetail,
            'userskills': userskills,
        }
        return render(request, 'yourprofile.html', details)
    except:
        pass
    return render(request, 'yourprofile.html')

def resumeupload(request):
    uid = request.session['log_id']

    if request.method == 'POST':
        file = request.FILES['resume']

        resumedata = resume_table(file_path=file, l_id=login_table(id=uid))
        resumedata.save()
        messages.success(request, 'Resume Uploaded Successfully')
    else:
        messages.error(request, 'error occured')

    return redirect(profilepage)

def deleteresume(request):
    uid = request.session['log_id']
    resume_table.objects.filter(l_id=uid).delete()

    return redirect(profilepage)

def editprofile(request):
    try:
        uid = request.session['log_id']
        try:
            usertypecheck = login_table.objects.get(id=uid)
        except login_table.DoesNotExist:
            usertypecheck = None

        Comp = False
        if usertypecheck.Role == "company":
            Comp = True

        try:
            profiledata = user_detail_table.objects.get(l_id=uid)
        except user_detail_table.DoesNotExist:
            profiledata = None


        statedetail = state_table.objects.all()
        citydetail = city.objects.all()
        areadetail = area_table.objects.all()

        details = {
            'Comp': Comp,
            'profiledata': profiledata,
            'statedetail': statedetail,
            'citydetail': citydetail,
            'areadetail': areadetail,
           }

        return render(request, 'editprofile.html', details)
    except:
        pass
    return render(request, 'editprofile.html')


def editprofilesubmit(request):
  uid = request.session['log_id']
  if request.method == 'POST':
    name = request.POST.get("name")
    email = request.POST.get("email")
    phone = request.POST.get("phone")
    enroll = request.POST.get("enroll")
    passout = request.POST.get("passoutyear")
    address = request.POST.get("address")
    areaid = request.POST.get("areaname")
    cityid = request.POST.get("cityname")
    stateid = request.POST.get("statename")



    cuser = login_table.objects.get(id=uid)

    cuser.email_id = email
    cuser.phone_no = phone

    cuser.save(update_fields=['email_id', 'phone_no'])

    cuser1 = user_detail_table.objects.get(l_id=uid)

    updcity = city.objects.get(id=cityid)
    updstate = state_table.objects.get(id=stateid)
    updarea= area_table.objects.get(id=areaid)

    cuser1.name = name
    cuser1.Enrollment = enroll
    cuser1.passoutyear = passout
    cuser1.address = address
    cuser1.area_id = updarea
    cuser1.city_id = updcity
    cuser1.state_id = updstate

    cuser1.save(update_fields=['name', 'Enrollment','passoutyear','address','area_id','city_id','state_id'])

    messages.success(request, 'Data Updated Successfully. ')

    return redirect(editprofile)

  else:
    messages.error(request, 'error occured')

  return redirect(editprofile)

def changedp(request):
    uid = request.session['log_id']
    if request.method == 'POST':
      file = request.FILES['changedp']

      cuser1 = login_table.objects.get(id=uid)
      cuser1.dp = file
      cuser1.save(update_fields=['dp'])
      messages.success(request, 'Picture Changed Successfully. ')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def changepw(request):
    uid = request.session['log_id']
    if request.method == 'POST':
      cpw = request.POST.get("oldpassword")
      npw = request.POST.get("password")

      cusercheck = login_table.objects.get(id=uid)

      checkpw = cusercheck.password
      print(checkpw)
      print(cpw)

      if checkpw == cpw:
          cuser1 = login_table.objects.get(id=uid)
          cuser1.password = npw
          cuser1.save(update_fields=['password'])
          messages.success(request, 'Password Changed Successfully. ')
      else:
          messages.error(request, 'Current Password is wrong.')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def completeprofilecomp(request):
    try:
        uid = request.session['log_id']
        try:
            usertypecheck = login_table.objects.get(id=uid)
        except login_table.DoesNotExist:
            usertypecheck = None

        Comp = False
        if usertypecheck.Role == "company":
            Comp = True

        try:
            companydata = company_details.objects.get(l_id=uid)
        except company_details.DoesNotExist:
            companydata = None

        statedetail = state_table.objects.all()
        citydetail = city.objects.all()
        areadetail = area_table.objects.all()

        details = {
            'Comp': Comp,
            'companydata': companydata,
            'statedetail': statedetail,
            'citydetail': citydetail,
            'areadetail': areadetail,
           }

        return render(request, 'completeprofilecomp.html', details)
    except:
        pass
    return render(request, 'completeprofilecomp.html')

def completeprofilecompsubmit(request):
    uid = request.session['log_id']
    if request.method == 'POST':
        cname = request.POST.get("name")
        caddress = request.POST.get("address")
        ctype = request.POST.get("type")
        cwebsite = request.POST.get("website")
        cyear = request.POST.get("fyear")
        csemail = request.POST.get("smail")
        csphone = request.POST.get("sphone")
        csize = request.POST.get("csize")
        carea = request.POST.get("area")
        ccity = request.POST.get("city")
        companydata = company_details(l_id=login_table(id=uid), company_name=cname, company_type=ctype, company_address=caddress, company_webiste=cwebsite, founded_year=cyear, company_support_mail=csemail, company_support_phone=csphone,
                                company_size=csize,company_city=ccity, company_area=carea)
        companydata.save()
        messages.success(request, 'Profile Created Successfully.')
        return redirect(index)
    else:
        messages.error(request, 'error occured')

def companyprofilepage(request):
    try:
        uid = request.session['log_id']
        try:
            usertypecheck = login_table.objects.get(id=uid)
        except login_table.DoesNotExist:
            usertypecheck = None

        Comp = False
        if usertypecheck.Role == "company":
            Comp = True

        try:
            companydata = company_details.objects.get(l_id=uid)
        except company_details.DoesNotExist:
            companydata = None

        statedetail = state_table.objects.all()
        citydetail = city.objects.all()
        areadetail = area_table.objects.all()

        details = {
            'Comp': Comp,
            'companydata': companydata,
            'statedetail': statedetail,
            'citydetail': citydetail,
            'areadetail': areadetail,
           }

        return render(request, 'companyprofile.html', details)
    except:
        pass
    return render(request, 'companyprofile.html')

def editprofilecompany(request):
    try:
        uid = request.session['log_id']
        try:
            usertypecheck = login_table.objects.get(id=uid)
        except login_table.DoesNotExist:
            usertypecheck = None

        Comp = False
        if usertypecheck.Role == "company":
            Comp = True

        try:
            companydata = company_details.objects.get(l_id=uid)
        except company_details.DoesNotExist:
            companydata = None

        statedetail = state_table.objects.all()
        citydetail = city.objects.all()
        areadetail = area_table.objects.all()

        details = {
            'Comp': Comp,
            'companydata': companydata,
            'statedetail': statedetail,
            'citydetail': citydetail,
            'areadetail': areadetail,
           }

        return render(request, 'editprofilecompany.html', details)
    except:
        pass
    return render(request, 'editprofilecompany.html')

def editprofilecompsubmit(request):
  uid = request.session['log_id']
  if request.method == 'POST':
    name = request.POST.get("name")
    email = request.POST.get("email")
    phone = request.POST.get("phone")
    type = request.POST.get("type")
    address = request.POST.get("address")
    website = request.POST.get("website")
    fyear = request.POST.get("fyear")
    smail = request.POST.get("smail")
    sphone = request.POST.get("sphone")
    csize = request.POST.get("csize")
    area = request.POST.get("area")
    city = request.POST.get("city")



    cuser = login_table.objects.get(id=uid)

    cuser.email_id = email
    cuser.phone_no = phone

    cuser.save(update_fields=['email_id', 'phone_no'])

    cuser1 = company_details.objects.get(l_id=uid)

    cuser1.company_name = name
    cuser1.company_type = type
    cuser1.company_address = address
    cuser1.company_webiste = website
    cuser1.founded_year = fyear
    cuser1.company_support_mail = smail
    cuser1.company_support_phone = sphone
    cuser1.company_size = csize
    cuser1.company_city = city
    cuser1.company_area = area

    cuser1.save(update_fields=['company_name', 'company_type','company_address','company_webiste','founded_year','company_support_mail','company_support_phone','company_size','company_city','company_area'])

    messages.success(request, 'Data Updated Successfully. ')

    return redirect(editprofilecompany)

  else:
    messages.error(request, 'error occured')

  return redirect(editprofilecompany)


def addjob(request):
    try:
        uid = request.session['log_id']
        try:
            usertypecheck = login_table.objects.get(id=uid)
        except login_table.DoesNotExist:
            usertypecheck = None

        Comp = False
        if usertypecheck.Role == "company":
            Comp = True

        try:
            companydata = company_details.objects.get(l_id=uid)
        except company_details.DoesNotExist:
            companydata = None

        statedetail = state_table.objects.all()
        citydetail = city.objects.all()
        areadetail = area_table.objects.all()

        details = {
            'Comp': Comp,
            'companydata': companydata,
            'statedetail': statedetail,
            'citydetail': citydetail,
            'areadetail': areadetail,
           }

        return render(request, 'addjob.html', details)
    except:
        pass
    return render(request, 'addjob.html')


def postjob(request):
    uid = request.session['log_id']

    if request.method == 'POST':
        jobname = request.POST.get("role")
        jobdesc = request.POST.get("jd")
        jobvac = request.POST.get("vacancy")
        jobpay = request.POST.get("pay")
        jobskill = request.POST.get("skill")

        cid = company_details.objects.get(l_id=uid)
        coid = cid.id


        jobdata = requirement_jobs(company_id=company_details(id=coid), job_type=jobname, job_description=jobdesc, vacancy= jobvac, basic_pay=jobpay, Status="OPEN", job_skill=jobskill)
        jobdata.save()
        messages.success(request, 'Job Posted Successfully. ')

    return redirect(addjob)


def youropenings(request):
    try:
        uid = request.session['log_id']


        cid = company_details.objects.get(l_id=uid)
        coid = cid.id

        try:
            usertypecheck = login_table.objects.get(id=uid)
        except login_table.DoesNotExist:
            usertypecheck = None

        Comp = False
        if usertypecheck.Role == "company":
            Comp = True


        postedjobdata = requirement_jobs.objects.filter(company_id=company_details(id=coid))



        try:
            companydata = company_details.objects.get(l_id=uid)
        except company_details.DoesNotExist:
            companydata = None

        details = {
            'companydata': companydata,
            'postedjobdata': postedjobdata,
            'Comp': Comp,
        }
        return render(request, 'youropenings.html', details)
    except:
        pass
    return render(request, 'youropenings.html')

def deletejob(request, jid):
    uid = request.session['log_id']

    cid = company_details.objects.get(l_id=uid)
    coid = cid.id

    requirement_jobs.objects.filter(company_id=company_details(id=coid), id=jid).delete()


    return redirect(youropenings)


def alljobs(request):
    try:
        uid = request.session['log_id']

        try:
            profiledata = user_detail_table.objects.get(l_id=uid)
        except user_detail_table.DoesNotExist:
            profiledata = None

        try:
            alljobdata = requirement_jobs.objects.all()
        except requirement_jobs.DoesNotExist:
            alljobdata = None

        default_page = 1
        page = request.GET.get('page', default_page)

        # Get queryset of items to paginate
        # items = FOOTWEAR_TABLE.objects.filter(CATEGORY_ID=1) this is query from old project
        try:
            items = requirement_jobs.objects.all()
        except requirement_jobs.DoesNotExist:
            items = None

        # Paginate items
        items_per_page = 2
        paginator = Paginator(items, items_per_page)

        try:
            items_page = paginator.page(page)
        except PageNotAnInteger:
            items_page = paginator.page(default_page)
        except EmptyPage:
            items_page = paginator.page(paginator.num_pages)

        details = {

            'profiledata': profiledata,
            'alljobdata': alljobdata,
            'items_page': items_page,

        }
        return render(request, 'alljobs.html',details)
    except:
        pass
    return render(request, 'alljobs.html')

def applyjob(request, ajid):
    uid = request.session['log_id']
    try:
        checkresume = resume_table.objects.get(l_id=login_table(id=uid))
    except resume_table.DoesNotExist:
        checkresume = None

    if checkresume is not None:
        try:
            appljob = appliedjob.objects.get(applied_job_id=requirement_jobs(id=ajid), l_id=login_table(id=uid))
        except appliedjob.DoesNotExist:
            appljob = None



        if appljob is None:
            uid = request.session['log_id']

            ud = user_detail_table.objects.get(l_id=uid)

            appjob = requirement_jobs.objects.get(id=ajid)
            appcomp = appjob.company_id.id
            cv = resume_table.objects.get(l_id=uid)

            applieddata = appliedjob(l_id=login_table(id=uid),applied_job_id=requirement_jobs(id=ajid),candidate_details=ud,applied_company_id=company_details(id=appcomp),candidate_resume=cv)
            applieddata.save()
            messages.success(request, 'You have applied for this job')

            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, 'You have already applied for this job')
            print("you have already applied")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        messages.error(request, 'Please upload your resume first in your Profile')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def viewyourapplications(request):
    try:
        uid = request.session['log_id']

        try:
            profiledata = user_detail_table.objects.get(l_id=uid)
        except user_detail_table.DoesNotExist:
            profiledata = None

        try:
            myapplications = appliedjob.objects.filter(l_id=login_table(id=uid))
        except appliedjob.DoesNotExist:
            myapplications = None



        details = {

            'profiledata': profiledata,
            'myapplications': myapplications,

        }
        return render(request, 'viewyourapplications.html', details)
    except:
        pass
    return render(request, 'viewyourapplications.html')

def deleteapplication(request, daid):
    appliedjob.objects.get(applied_job_id=requirement_jobs(id=daid)).delete()
    return redirect(viewyourapplications)

def viewcandidates(request):
    try:
        uid = request.session['log_id']

        cid = company_details.objects.get(l_id=uid)
        coid = cid.id
        cname = cid.company_name
        print(cname)

        try:
            usertypecheck = login_table.objects.get(id=uid)
        except login_table.DoesNotExist:
            usertypecheck = None

        Comp = False
        if usertypecheck.Role == "company":
            Comp = True



        appliedcandidates = appliedjob.objects.filter(applied_company_id=company_details(id=coid))

        print(appliedcandidates)

        try:
            companydata = company_details.objects.get(l_id=uid)
        except company_details.DoesNotExist:
            companydata = None

        details = {
            'Comp': Comp,
            'companydata': companydata,
            'appliedcandidates': appliedcandidates,
        }
        return render(request, 'viewcandidates.html', details)
    except:
        pass
    return render(request, 'viewcandidates.html')

def showinterest(request, siid):
    showi = appliedjob.objects.get(applied_job_id=requirement_jobs(id=siid))
    showi.applied_job_status = "Shown Interest"
    showi.show_interest_button = False
    showi.save(update_fields=['applied_job_status','show_interest_button'])
    print(showi.applied_job_id.job_type)
    print(showi.show_interest_button)
    stalen = len(showi.applied_job_status)
    print(stalen)
    return redirect(viewcandidates)

def rejectcandidate(request, rcid):
    rejectcandidate = appliedjob.objects.get(applied_job_id=requirement_jobs(id=rcid))
    rejectcandidate.applied_job_status = "Rejected"
    rejectcandidate.rejected = True
    rejectcandidate.save(update_fields=['applied_job_status','rejected'])
    print(rejectcandidate.applied_job_id.job_type)
    print(rejectcandidate.rejected)
    return redirect(viewcandidates)