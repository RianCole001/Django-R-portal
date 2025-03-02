from django.shortcuts import render
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')  # Rendering the dashboard template

def profile(request):
    # Your view logic for editing the profile
    return render(request, 'profile.html')
def add_student(request):
    # Your view logic for editing the profile
    return render(request, 'add-student.html')
def all_students(request):
    # Your view logic for editing the profile
    return render(request, 'all-students.html')
def departments(request):
    # Your view logic for editing the profile
    return render(request, 'departments.html')
def programs(request):
    # Your view logic for editing the profile
    return render(request, 'programs.html')
def logout(request):
    return render(request,'logout.html')