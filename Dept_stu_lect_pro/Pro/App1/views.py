from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from.models import Department,Student,Lecturer
from.forms import DepartmentForm,StudentForm,LecturerForm
from django.contrib.auth.decorators import login_required


def homeView(request):
    template_name = 'App1/base.html'
    context = {}
    return render(request, template_name, context)

@login_required(login_url='login')
def addView(request):
    form=DepartmentForm
    if request.method == 'POST':
        form =DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showdpt')
            # return HttpResponse('order Placed')
    template_name = 'App1/add_dept.html'
    context = {'form': form}
    return render(request, template_name, context)

@login_required(login_url='login')
def showdeptView(request):
    dp = Department.objects.all()
    template_name = 'App1/show_dept.html'
    context = {'dp': dp}
    return render(request, template_name, context)

def updateView(request,id1):
    dp =Department.objects.get(id=id1)
    form=DepartmentForm(instance=dp)
    if request.method=='POST':
        form=DepartmentForm(request.POST,instance=dp)
        if form.is_valid():
            form.save()
            return redirect('showdpt')
    template_name='App1/add_dept.html'
    context={'form':form}
    return render(request,template_name,context)



def deleteView(request,id1):
    dp=Department.objects.get(id=id1)
    dp.delete()
    return redirect('showdpt')

#--------------------------------------------------------------------------------------------------------------------

@login_required(login_url='login')
def add_Stu_View(request):
    form=StudentForm
    if request.method == 'POST':
        form =StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_stu')
            # return HttpResponse('order Placed')
    template_name = 'App1/add_stu.html'
    context = {'form': form}
    return render(request, template_name, context)

@login_required(login_url='login')
def show_Stu_View(request):
    template_name = 'App1/show_stu.html'
    st = Student.objects.all()
    context = {'st': st}
    return render(request, template_name, context)

def update_Stu_View(request,id1):
    st = Student.objects.get(id=id1)
    form=StudentForm(instance= st)
    if request.method=='POST':
        form=StudentForm(request.POST,instance=st)
        if form.is_valid():
            form.save()
            return redirect('show_stu')
    template_name='App1/add_stu.html'
    context={'form':form}
    return render(request,template_name,context)



def delete_Stu_View(request,id1):
    st =Student.objects.get(id=id1)
    st.delete()
    return redirect('show_stu')

#------------------------------------------------------------------------------------------------------------------------------
@login_required(login_url='login')
def add_Lec_View(request):
    form=LecturerForm
    if request.method == 'POST':
        form =LecturerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_lec')
            # return HttpResponse('order Placed')
    template_name = 'App1/add_lec.html'
    context = {'form': form}
    return render(request, template_name, context)

@login_required(login_url='login')
def show_lec_View(request):
    template_name = 'App1/show_lec.html'
    lc = Lecturer.objects.all()
    context = {'lc':lc }
    return render(request, template_name, context)


def update_Lec_View(request,id1):
    lc = Lecturer.objects.get(id=id1)
    form=LecturerForm(instance=lc)
    if request.method =='POST':
        form=LecturerForm(request.POST,instance=lc)
        if form.is_valid():
            form.save()
            return redirect('show_lec')
    template_name='App1/add_lec.html'
    context={'form':form}
    return render(request,template_name,context)



def delete_Lec_View(request,id1):
    lc=Lecturer.objects.get(id=id1)
    lc.delete()
    return redirect('show_lec')

#-------------------------------------------------------------------------------------------------------------------------------


def search(request):
    if request.method=='POST':
        srch=request.POST.get('searchkey')
        st=Student.objects.all()
        # if srch not in st:
        #     return HttpResponse('record not found!!')
        record=Student.objects.filter(stu_name=srch)

        recordlect=Lecturer.objects.filter(name=srch)
        template_name='App1/showresult.html'
        context={'record':record,'recordlect':recordlect}
        return render(request, template_name,context)

    template_name='App1/search.html'
    context={}
    return render(request, template_name, context)


# def search_dept_stu(request,id1):
#     data=Department.objects.get(id=id1)
#     record=Student.objects.filter(Dept_stud=data)
#     template_name='App1/showdeptstudent.html'
#     context={'record':record}
#     return render(request, template_name, context)
#
# def search_dept_lect(request,id1):
#     data = Department.objects.get(id=id1)
#     record = Lecturer.objects.filter(dept_lec=data)
#     template_name = 'App1/showdeptlect.html'
#     context = {'record': record}
#     return render(request, template_name, context)

