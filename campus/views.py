from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import CampusBlock, Classroom, Course, Faculty, Student
from .forms import BlockForm, ClassroomForm, CourseForm, LoginForm
from django.contrib.auth.decorators import login_required



def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, 'campus/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    blocks = CampusBlock.objects.all()
    selected_block_id = request.GET.get('block')
    selected_block = None

    if selected_block_id:
        try:
            selected_block = CampusBlock.objects.get(id=selected_block_id)
        except CampusBlock.DoesNotExist:
            selected_block = None

    # Filter classrooms by selected block
    if selected_block:
        classrooms = Classroom.objects.filter(block=selected_block)
        courses = Course.objects.filter(block=selected_block)
    else:
        classrooms = Classroom.objects.all()
        courses = Course.objects.all()

    # Calculate faculty workload
    faculty_workload = {}
    for faculty in Faculty.objects.all():
        # Count only courses in this block
        assigned_courses = faculty.courses.filter(id__in=courses.values_list('id', flat=True)).count()
        faculty_workload[faculty.user.get_full_name()] = assigned_courses

    context = {
        'blocks': blocks,
        'selected_block': selected_block,
        'classrooms': classrooms,
        'courses': courses,
        'faculty_workload': faculty_workload,
    }
    return render(request, 'campus/dashboard.html', context)

@login_required
def blocks(request):
    if request.method == 'POST':
        form = BlockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = BlockForm()
    return render(request, 'campus/blocks.html', {'form': form})

@login_required
def classrooms(request):
    if request.method == 'POST':
        form = ClassroomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ClassroomForm()
    return render(request, 'campus/classrooms.html', {'form': form})

@login_required
def courses(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CourseForm()
    return render(request, 'campus/courses.html', {'form': form})


# def blocks_view(request):
#     blocks = CampusBlock.objects.all()
#     return render(request, 'campus/blocks.html', {'blocks': blocks})

# def classrooms_view(request):
#     classrooms = Classroom.objects.all()
#     return render(request, 'campus/classrooms.html', {'classrooms': classrooms})

# def courses_view(request):
#     courses = Course.objects.all()
#     return render(request, 'campus/courses.html', {'courses': courses})