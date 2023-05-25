import json

from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import RequirementSerializer
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import *
from django.http import HttpResponse



def test(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            # Обработка валидных данных формы
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Дополнительные действия
            print(f'name: {name}')
            print(f'email: {email}')
            print(f'message: {message}')
    else:
        form = MyForm()
    return render(request, 'main/structured/test.html', {'form': form})

def index(request):
    return render(request, 'main/structured/index.html')

def requirements(request):
    requirements = Requirement.objects.all()
    context = {'requirements': requirements}
    return render(request, 'main/structured/requirements.html', context)

def new_requirement(request):
    if request.method == 'POST':
        form = RequirementForm(request.POST)
        if form.is_valid():
            requirement = form.save(commit=False)
            requirement.save()
            # Преобразование в JSON
            data = {
                'id': requirement.id,
                'description': requirement.description,
                'type': requirement.type,
                'priority': requirement.priority,
                'status': requirement.status
            }
            json_data = json.dumps(data, indent=4)
            # Запись в файл
            with open('requirements.json', 'a') as f:
                f.write(json_data)
                f.write('\n')
            return HttpResponse('Требование успешно добавлено!')
    else:
        form = RequirementForm()
    return render(request, 'main/structured/new_requirement.html', {'form': form})

# -----------

def Reqsysman(request):
    return render(request, 'main/Reqsysman.html')


def github(request):
    return render(request, 'main/github.html' )


def requirements_list(request):
    requirements = Requirement.objects.all()
    print(requirements)
    context = {'requirements': requirements}
    return render(request, 'main/requirements_list.html', context)

# def admin(request):
#     return render(request, 'main/admin.html' )


# def requirement_list_view(request):
#     requirements = Requirement.objects.all()
#
#     # Логика для фильтрации и сортировки requirements
#
#     return render(request, 'requirement_list.html', {'requirements': requirements})
#
#
# def requirement_detail_view(request, requirement_id):
#     requirement = get_object_or_404(Requirement, pk=requirement_id)
#
#     # Логика для отображения связанных требований
#
#     return render(request, 'requirement_detail.html', {'requirement': requirement})


# def add_requirement(request):
#     if request.method == 'POST':
#         form = RequirementForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('requirements_list')
#     else:
#         form = RequirementForm()
#     return render(request, 'add_requirement.html', {'form': form})


def add_requirement(request):
    if request.method == 'POST':
        form = RequirementForm(request.POST)
        if form.is_valid():
            requirement = form.save(commit=False)
            requirement.save()
            # Преобразование в JSON
            data = {
                'id': requirement.id,
                'description': requirement.description,
                'type': requirement.type,
                'priority': requirement.priority,
                'status': requirement.status
            }
            json_data = json.dumps(data, indent=4)
            # Запись в файл
            with open('requirements.json', 'a') as f:
                f.write(json_data)
                f.write('\n')
            return HttpResponse('Требование успешно добавлено!')
    else:
        form = RequirementForm()
    return render(request, 'add_requirement.html', {'form': form})

class RequirementViewSet(viewsets.ModelViewSet):
    queryset = Requirement.objects.all()
    serializer_class = RequirementSerializer


class RequirementController:
    def create_requirement(request):
        # Получение данных из запроса
        type = request.POST.get('type')
        description = request.POST.get('description')

        # Создание нового объекта требования
        requirement = Requirement(type=type, description=description)
        requirement.save()

        # Возврат ответа с созданным объектом требования в JSON формате
        return JsonResponse({'id': requirement.id, 'type': requirement.type, 'description': requirement.description})

    def update_requirement(request, requirement_id):
        # Получение объекта требования по его идентификатору
        requirement = get_object_or_404(Requirement, pk=requirement_id)

        # Обновление данных требования
        requirement.type = request.POST.get('type')
        requirement.description = request.POST.get('description')
        requirement.save()

        # Возврат ответа с обновленным объектом требования в JSON формате
        return JsonResponse({'id': requirement.id, 'type': requirement.type, 'description': requirement.description})

    def delete_requirement(request, requirement_id):
        # Получение объекта требования по его идентификатору и удаление его из базы данных
        requirement = get_object_or_404(Requirement, pk=requirement_id)
        requirement.delete()

        # Возврат ответа с сообщением об успешном удалении
        return JsonResponse({'message': 'Requirement deleted successfully'})

    def get_requirement(request, requirement_id):
        # Получение объекта требования по его идентификатору
        requirement = get_object_or_404(Requirement, pk=requirement_id)

        # Возврат ответа с объектом требования в JSON формате
        return JsonResponse({'id': requirement.id, 'type': requirement.type, 'description': requirement.description})

    def get_requirements(request):
        # Получение всех объектов требований из базы данных
        requirements = Requirement.objects.all()

        # Создание списка объектов требований в формате JSON
        requirements_list = []
        for requirement in requirements:
            requirements_list.append({'id': requirement.id, 'type': requirement.type, 'description': requirement.description})

        # Возврат ответа со списком объектов требований в JSON формате
        return JsonResponse({'requirements': requirements_list})





class RequirementTypeController:

    def create_requirement_type(self, request):
        # Получение данных из запроса
        name = request.POST.get('name')
        description = request.POST.get('description')

        # Создание нового объекта типа требований
        requirement_type = RequirementType(name=name, description=description)
        requirement_type.save()

        # Возврат ответа с созданным объектом типа требований в JSON формате
        return JsonResponse(
            {'id': requirement_type.id, 'name': requirement_type.name, 'description': requirement_type.description})

    def get_requirement_type(self, request, type_id):
        # Получение объекта типа требований по его идентификатору
        requirement_type = RequirementType.objects.get(id=type_id)

        # Возврат ответа с данными объекта типа требований в JSON формате
        return JsonResponse(
            {'id': requirement_type.id, 'name': requirement_type.name, 'description': requirement_type.description})

    def update_requirement_type(self, request, type_id):
        # Получение объекта типа требований по его идентификатору
        requirement_type = RequirementType.objects.get(id=type_id)

        # Обновление данных объекта типа требований на основе данных из запроса
        requirement_type.name = request.POST.get('name')
        requirement_type.description = request.POST.get('description')
        requirement_type.save()

        # Возврат ответа с обновленными данными объекта типа требований в JSON формате
        return JsonResponse(
            {'id': requirement_type.id, 'name': requirement_type.name, 'description': requirement_type.description})

    def delete_requirement_type(self, request, type_id):
        # Получение объекта типа требований по его идентификатору
        requirement_type = RequirementType.objects.get(id=type_id)

        # Удаление объекта типа требований
        requirement_type.delete()

        # Возврат ответа об успешном удалении объекта типа требований
        return JsonResponse({'message': 'Requirement type has been deleted successfully.'})

