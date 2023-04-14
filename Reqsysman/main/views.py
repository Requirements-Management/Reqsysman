from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import RequirementSerializer
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


def index(request):
    return render(request, 'main/index.html')


def Reqsysman(request):
    return render(request, 'main/Reqsysman.html' )


def github(request):
    return render(request, 'main/github.html' )



def requirement_list_view(request):
    requirements = Requirement.objects.all()

    # Логика для фильтрации и сортировки requirements

    return render(request, 'requirement_list.html', {'requirements': requirements})




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

