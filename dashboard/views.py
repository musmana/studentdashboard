from django.shortcuts import render

def home(request):
    student = {
        "name": "Rahul Sharma",
        "class": "10th Grade",
        "roll_no": 24,
        "subjects": [
            {"name": "Math", "marks": 78},
            {"name": "Science", "marks": 92},
            {"name": "English", "marks": 65},
            {"name": "History", "marks": 48},
            {"name": "Computer", "marks": 88},
        ]
    }

    total_marks = sum(sub["marks"] for sub in student["subjects"])
    avg = total_marks / len(student["subjects"])
    progress = int(avg)  # for progress bar

    return render(request, 'dashboard/home.html', {
        "student": student,
        "progress": progress
    })
