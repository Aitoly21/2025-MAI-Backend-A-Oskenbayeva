from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST
from django.http import JsonResponse
from core.models import Course, Category, Profile
from django.db.models import Q
import json

# ===== PROFILE =====

@require_GET
def profile_list_view(request):
    profiles = Profile.objects.select_related("user").all()
    data = [
        {
            "id": p.id,
            "user_id": p.user.id,
            "username": p.user.username,
            "role": p.role,
            "bio": p.bio,
            "phone": p.phone,
            "date_of_birth": p.date_of_birth,
            "address": p.address
        }
        for p in profiles
    ]
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})

@csrf_exempt
@require_POST
def profile_create_view(request):
    data = json.loads(request.body)
    user = Profile.user.field.related_model.objects.create_user(
        username=data.get("username", ""),
        password=data.get("password", "")
    )
    profile = Profile.objects.create(
        user=user,
        role=data.get("role", ""),
        bio=data.get("bio", ""),
        phone=data.get("phone", ""),
        date_of_birth=data.get("date_of_birth", None),
        address=data.get("address", "")
    )
    return JsonResponse({"id": profile.id, "status": "created"}, json_dumps_params={'ensure_ascii': False})

@require_GET
def profile_search_view(request):
    query = request.GET.get("q", "")
    results = Profile.objects.filter(
        Q(user__username__icontains=query) |
        Q(role__icontains=query) |
        Q(bio__icontains=query)
    ).select_related("user")
    data = [
        {
            "id": p.id,
            "username": p.user.username,
            "role": p.role,
            "bio": p.bio
        }
        for p in results
    ]
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})

# ===== COURSE =====

@require_GET
def course_list_view(request):
    courses = Course.objects.all()
    data = [
        {
            "id": c.id,
            "title": c.title,
            "description": c.description,
            "delivery_mode": c.delivery_mode,
            "category_id": c.category_id,
            "duration": c.duration
        }
        for c in courses
    ]
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})

@csrf_exempt
@require_POST
def course_create_view(request):
    data = json.loads(request.body)
    course = Course.objects.create(
        title=data.get("title", ""),
        description=data.get("description", ""),
        delivery_mode=data.get("delivery_mode", ""),
        category_id=data.get("category_id"),
        duration=data.get("duration", "")
    )
    return JsonResponse({"id": course.id, "status": "created"}, json_dumps_params={'ensure_ascii': False})

@require_GET
def course_search_view(request):
    query = request.GET.get("q", "")
    results = Course.objects.filter(
        Q(title__icontains=query) | Q(description__icontains=query)
    )
    data = [{"id": c.id, "title": c.title, "description": c.description} for c in results]
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})

# ===== CATEGORY =====

@require_GET
def category_list_view(request):
    categories = Category.objects.all()
    data = [{"id": c.id, "name": c.name, "description": c.description} for c in categories]
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})

@csrf_exempt
@require_POST
def category_create_view(request):
    data = json.loads(request.body)
    category = Category.objects.create(
        name=data.get("name", ""),
        description=data.get("description", "")
    )
    return JsonResponse({"id": category.id, "status": "created"}, json_dumps_params={'ensure_ascii': False})

@require_GET
def category_search_view(request):
    query = request.GET.get("q", "")
    results = Category.objects.filter(
        Q(name__icontains=query) | Q(description__icontains=query)
    )
    data = [{"id": c.id, "name": c.name} for c in results]
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})
