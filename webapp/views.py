from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Student
import json

def read_data(request):
    students = Student.objects.all()
    result = []
    for s in students:
        result.append({
            'Stu_id': s.Stu_id,
            'Name': s.Name,
            'Age': s.Age,
            'Qualification': s.Qualification
        })
    return JsonResponse(result, safe=False)

@csrf_exempt
def create_data(request):
    if request.method == "POST":
        data = json.loads(request.body)
        Name = data.get("Name")
        Age = data.get("Age")
        Qualification = data.get("Qualification")
        if Name and Age and Qualification:
            student = Student.objects.create(
                Name=Name,
                Age=int(Age),
                Qualification=Qualification
            )
            return JsonResponse({"message": "Student created", "Stu_id": student.Stu_id})
        else:
            return JsonResponse({"error": "Missing required fields"}, status=400)
    return JsonResponse({"error": "Invalid method"}, status=405)

@csrf_exempt
def update_data(request, Stu_id):
    if request.method == "POST":
        student = Student.objects.get(Stu_id=Stu_id)
        data = json.loads(request.body)
        student.Name = data.get("Name", student.Name)
        student.Age = int(data.get("Age", student.Age))
        student.Qualification = data.get("Qualification", student.Qualification)
        student.save()
        return JsonResponse({"message": "Student Updated", "Stu_id": student.Stu_id})
    return JsonResponse({"error": "Invalid method"}, status=405)

@csrf_exempt
def delete_data(request, Stu_id):
    if request.method == "POST":
        student = Student.objects.get(Stu_id=Stu_id)
        student.delete()
        return JsonResponse({"message": "Student Deleted", "Stu_id": Stu_id})
    return JsonResponse({"error": "Invalid method"}, status=405)