from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Image
from myproject.forms import RegistrationForm


# ================= READ + IMAGE UPLOAD =================

def read_student(request):

    # IMAGE UPLOAD
    if request.method == "POST" and request.FILES.get("image"):

        pic = request.FILES.get("image")

        Image.objects.create(image=pic)

        return redirect("read")

    students = Student.objects.all()

    images = Image.objects.all()

    form = RegistrationForm()

    return render(request, 'home/Read.html', {

        'students': students,
        'form': form,
        'data': images

    })


# ================= CREATE =================

def create_student(request):

    if request.method == "POST":

        form = RegistrationForm(request.POST)

        if form.is_valid():

            Student.objects.create(

                name=form.cleaned_data['name'],
                age=form.cleaned_data['age'],
                city=form.cleaned_data['city']

            )

            return redirect('read')

        return render(request, 'home/Read.html', {

            'form': form,
            'students': Student.objects.all(),
            'data': Image.objects.all()

        })

    return redirect('read')


# ================= UPDATE =================

def update_student(request, id):

    student = get_object_or_404(Student, id=id)

    if request.method == "POST":

        form = RegistrationForm(request.POST)

        if form.is_valid():

            student.name = form.cleaned_data['name']
            student.age = form.cleaned_data['age']
            student.city = form.cleaned_data['city']

            student.save()

            return redirect('read')

    return render(request, 'home/update.html', {

        'student': student

    })


# ================= DELETE =================

def delete_student(request, id):

    student = get_object_or_404(Student, id=id)

    student.delete()

    return redirect('read')