from django.db import models


class Requirement(models.Model):
    name = models.CharField(max_length=100)
    identifier = models.CharField(max_length=100)
    version = models.CharField(max_length=100)

    def __str__(self):
        return self.name


    def update_version(self, *args, **kwargs):
        # проверяем, существует ли требование в базе данных. Если да, увеличиваем версию на 1
        if self.pk:
            original = Requirement.objects.get(pk=self.pk)
            if original.version != self.version:
                raise ValueError('Нельзя изменять номер версии уже существующего требования')
            self.version = f"{int(self.version) + 1}"
        super().update_version(*args, **kwargs)


 def update_requirement(self, name=None, identifier=None, version=None):
        # обновляем данные требования
        if name is not None:
            self.name = name
        if identifier is not None:
            self.identifier = identifier
        if version is not None:
            self.version = version
        # сохраняем изменения в базе данных
        self.update_version()


class RequirementLink(models.Model):
    # source_requirement - это требование-источник, от которого исходит связь.
    source_requirement = models.ForeignKey(Requirement, related_name='source_links', on_delete=models.CASCADE)
    # target_requirement - это требование-цель, которое связывается с требованием-источником.
    target_requirement = models.ForeignKey(Requirement, related_name='target_links', on_delete=models.CASCADE)
    source_version = models.CharField(max_length=100)
    target_version = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.source_requirement} -> {self.target_requirement}"


    # Методы сначала проверяюь, существуют ли требования с заданными идентификаторами, и если они существуют,
    # создает новый объект связи RequirementLink с заданными значениями и сохраняет его в базе данных.
    # В случае, если требование с заданным идентификатором не существует, метод возвращает None.

    # метод добавления связи
    @staticmethod
    def add_link(source_req_id, target_req_id, source_version, target_version):
        try:
            source_req = Requirement.objects.get(id=source_req_id)
            target_req = Requirement.objects.get(id=target_req_id)
            link = RequirementLink(source_requirement=source_req, target_requirement=target_req,
                                   source_version=source_version, target_version=target_version)
            link.save()
            return link
        except Requirement.DoesNotExist:
            return None

    # метод для удаления связи между требованиями
    @staticmethod
    def delete_link(source_req_id, target_req_id):
        try:
            link = RequirementLink.objects.get(source_requirement_id=source_req_id, target_requirement_id=target_req_id)
            link.delete()
            return True
        except RequirementLink.DoesNotExist:
            return False

    # метод для обновления версий связи между требованиями
    @staticmethod
    def update_link_versions(source_req_id, target_req_id, source_version, target_version):
        try:
            link = RequirementLink.objects.get(source_requirement_id=source_req_id, target_requirement_id=target_req_id)
            link.source_version = source_version
            link.target_version = target_version
            link.save()
            return True
        except RequirementLink.DoesNotExist:
            return False

    # метод для проверки на валидность операций
    @staticmethod
    def is_valid_operation(source_req_id, target_req_id):
        return Requirement.objects.filter(id__in=[source_req_id, target_req_id]).count() == 2
