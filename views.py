from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Book


# ================= READ =================
def read(request):
    students = Student.objects.all()
    return render(request, "read.html", {"students": students})


# ================= CREATE =================
def create(request):

    if request.method == "POST":

        # Create student
        student = Student.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
        )

        # Create books
        book1 = Book.objects.create(
            book_name=request.POST.get("book1"),
            author=request.POST.get("author1"),
            price=request.POST.get("price1")
        )

        book2 = Book.objects.create(
            book_name=request.POST.get("book2"),
            author=request.POST.get("author2"),
            price=request.POST.get("price2")
        )

        # ✅ FIXED MANY-TO-MANY RELATION
        book1.students.add(student)
        book2.students.add(student)

        return redirect("read")

    return render(request, "create.html")


# ================= PROFILE =================
def profile(request, id):
    student = get_object_or_404(Student, id=id)
    books = student.books.all()

    return render(request, "profile.html", {
        "student": student,
        "books": books
    })


# ================= DELETE =================
def delete(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect("read")