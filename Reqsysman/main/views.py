import json

from django.shortcuts import render
from .adapters.api_relationship_adapter import ApiRelationShipsAdapter
from .adapters.api_requirements_adapter import ApiRequirementsAdapter
from rest_framework import viewsets
from .models import *
from .serializers import RequirementSerializer
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import *
from django.http import HttpResponse


class RequirementViewSet(viewsets.ModelViewSet):
    queryset = Requirement.objects.all()
    serializer_class = RequirementSerializer


class RequirementController:
    adapter = ApiRequirementsAdapter()

    @staticmethod
    def create_requirement(request):
        # Получение данных из запроса
        type = request.POST.get('type')
        description = request.POST.get('description')


        created_requirement = RequirementController.adapter.create_requirement(new_requirement)

        # Возврат ответа с созданным объектом требования
        return JsonResponse(created_requirement)

    @staticmethod
    def update_requirement(request, requirement_id):
        # Получение данных из запроса
        type = request.POST.get('type')
        description = request.POST.get('description')

        # Получение существующего требования через API адаптер
        existing_requirement = RequirementController.adapter.get_requirement_by_id(requirement_id)

        # Обновление данных требования
        existing_requirement['type'] = type
        existing_requirement['description'] = description

        # Обновление требования через API адаптер
        updated_requirement = RequirementController.adapter.update_requirement(requirement_id, existing_requirement)

        # Возврат ответа с обновленным объектом требования
        return JsonResponse(updated_requirement)

    @staticmethod
    def delete_requirement(request, requirement_id):
        # Удаление требования через API адаптер
        RequirementController.adapter.delete_requirement(requirement_id)

        # Возврат ответа с сообщением об успешном удалении
        return JsonResponse({'message': 'Requirement deleted successfully'})

    @staticmethod
    def get_requirement(request, requirement_id):
        # Получение требования через API адаптер
        requirement = RequirementController.adapter.get_requirement_by_id(requirement_id)

        # Возврат ответа с объектом требования
        return JsonResponse(requirement)

    @staticmethod
    def get_requirements(request):
        # Получение всех требований через API адаптер
        requirements = RequirementController.adapter.get_all_requirements()

        # Возврат ответа со списком объектов требований
        return render(request, 'main/structured/requirements.html', {'requirements': requirements})
        # return JsonResponse({'requirements': requirements})





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
    
    
class RelationshipController:
    adapter = ApiRelationShipsAdapter()

    @staticmethod
    def create_relationship(request):
        # Получение данных из запроса
        source_requirement = request.POST.get('source_requirement')
        target_requirement = request.POST.get('target_requirement')
        relationship_type = request.POST.get('relationship_type')
        branch = request.POST.get('branch')
        commit_hash = request.POST.get('commit_hash')

        # Создание связи между требованиями через адаптер
        response = RelationshipController.adapter.create_relationship(source_requirement, target_requirement,
                                                                     relationship_type, branch, commit_hash)

        # Возврат ответа от адаптера в формате JSON
        return JsonResponse(response)

    @staticmethod
    def update_relationship(request, relationship_id):
        # Получение данных из запроса
        source_requirement = request.POST.get('source_requirement')
        target_requirement = request.POST.get('target_requirement')
        relationship_type = request.POST.get('relationship_type')
        branch = request.POST.get('branch')
        new_commit_hash = request.POST.get('new_commit_hash')

        # Обновление связи между требованиями через адаптер
        response = RelationshipController.adapter.update_relationship(relationship_id, source_requirement,
                                                                      target_requirement, relationship_type,
                                                                      branch, new_commit_hash)

        # Возврат ответа от адаптера в формате JSON
        return JsonResponse(response)

    @staticmethod
    def delete_relationship(request, relationship_id):
        # Получение данных из запроса
        branch = request.POST.get('branch')
        commit_hash = request.POST.get('commit_hash')

        # Удаление связи между требованиями через адаптер
        response = RelationshipController.adapter.delete_relationship(relationship_id, branch, commit_hash)

        # Возврат ответа от адаптера в формате JSON
        return JsonResponse(response)

    @staticmethod
    def get_relationship(request, relationship_id):
        # Получение данных из запроса
        branch = request.GET.get('branch')
        commit_hash = request.GET.get('commit_hash')

        # Получение информации о связи между требованиями через адаптер
        response = RelationshipController.adapter.get_relationship(relationship_id, branch, commit_hash)

        # Возврат ответа от адаптера в формате JSON
        return JsonResponse(response)

    @staticmethod
    def get_relationships(request):
        # Получение данных из запроса
        branch = request.GET.get('branch')
        commit_hash = request.GET.get('commit_hash')

        # Получение связей между требованиями через адаптер
        response = RelationshipController.adapter.get_relationships(branch, commit_hash)

        # Возврат ответа от адаптера в формате JSON
        return JsonResponse(response)



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
    return render(request, 'main/structured/requirements.html', {'requirements': requirements})

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
    return render(request, 'main/requirements_list.html', {'requirements': requirements})

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
