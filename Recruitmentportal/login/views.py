from django.shortcuts import render
 
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from.models import Profile
from django.contrib.auth.forms import PasswordResetForm



def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Log the user in
            login(request, user)
            messages.success(request, "You have successfully logged in!")
            return redirect('home')  # Redirect to a home or dashboard page after successful login
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, 'login/login.html')  # Reload the login page with an error message

    return render(request, 'login/login.html')
def register_view(request):
    return render(request, 'login/register.html')

#view for the register formd


def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_repeat = request.POST['repeat_password']

        # Check if passwords match
        if password != password_repeat:
            messages.error(request, "Passwords do not match.")
            return render(request, 'login/register.html')

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return render(request, 'login/register.html')

        # Check if the email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return render(request, 'login/register.html')

        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        # Create a Profile instance for the new user
        profile = Profile(user=user)
        profile.save()

        # Save additional information such as phone number and job type if provided
        phone = request.POST.get('phone')  # Assuming you have a 'phone' field in your form
        if phone:
            profile.phone = phone
            profile.save()  # Save the phone number to the profile

        job = request.POST.get('job')  # Assuming you have a 'job' field in your form
        if job:
            profile.job = job
            profile.save()  # Save the job type to the profile

        # Redirect to the login page with a success message
        messages.success(request, "Registration successful! You can now log in.")
        return redirect('login')  # Replace 'login' with the name of your login page URL

    return render(request, 'login/register.html')
def forgot_password(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Password reset email has been sent.")
            return redirect('login')  # Redirect to login page
    else:
        form = PasswordResetForm()
    return render(request, 'login/forgot_password.html', {'form': form})
