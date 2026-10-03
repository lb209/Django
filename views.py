from django.shortcuts import render, redirect
from .models import Student


def home(request):

    if request.method == "POST":

        name = request.POST.get("name")

        roll_number = request.POST.get("roll_number")

        course = request.POST.get("course")

        image = request.FILES.get("image")

        Student.objects.create(
            name=name,
            roll_number=roll_number,
            course=course,
            image=image
        )

        return redirect("home")

    student = Student.objects.all()

    return render(request, "index.html", {
        "student": student
    })


def delete_student(request, id):

    student = Student.objects.get(id=id)

    student.delete()

    return redirect("home")


def edit_student(request, id):

    student = Student.objects.get(id=id)

    if request.method == "POST":

        student.name = request.POST.get("name")

        student.roll_number = request.POST.get("roll_number")

        student.course = request.POST.get("course")

        image = request.FILES.get("image")

        if image:
            student.image = image

        student.save()

        return redirect("home")

    return render(request, "index.html", {
        "student": Student.objects.all(),
        "edit_student": student
    })