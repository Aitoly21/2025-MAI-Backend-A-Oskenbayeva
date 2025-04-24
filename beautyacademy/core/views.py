from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt
def profile_view(request):
    if request.method == 'GET':
        return JsonResponse({"username": "glam_girl", "role": "student"})
    elif request.method == 'POST':
        return JsonResponse({"status": "Профиль обновлён!"})
    return JsonResponse({"error": "Метод не поддерживается"}, status=405)

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt
def courses_list_view(request):
    if request.method == 'GET':
        return JsonResponse({
            "courses": [
                {"id": 1, "title": "Базовый курс по макияжу"},
                {"id": 2, "title": "Школа бровистов: от основ до идеала"},
                {"id": 3, "title": "Курс по вечернему макияжу"},
                {"id": 4, "title": "Секреты ухода за кожей лица"},
            ]
        }, json_dumps_params={'ensure_ascii': False})
    elif request.method == 'POST':
        return JsonResponse({"status": "courses updated"})
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)


@csrf_exempt
def categories_list_view(request):
    if request.method == 'GET':
        return JsonResponse({
            "categories": [
                {"id": 1, "name": "Косметика"},
                {"id": 2, "name": "Уход за кожей"},
                {"id": 3, "name": "Парфюмерия"}
            ]
        }, json_dumps_params={'ensure_ascii': False})  # ← вот эта часть
    elif request.method == 'POST':
        return JsonResponse({"status": "Категории обновлены!"})
    return JsonResponse({"error": "Метод не поддерживается"}, status=405)
