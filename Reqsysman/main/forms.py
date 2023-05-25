from django import forms
from .models import Requirement
from django.shortcuts import render, redirect


# START TEST CODE
class MyForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
# END TEST CODE


class RequirementForm(forms.Form):
    id = forms.CharField(max_length=50, required=True)

    description = forms.CharField(widget=forms.Textarea, required=True)
    #type = forms.
    #type = forms.ForeignKey(RequirementType, \
    #    on_delete=models.CASCADE)

    priority_choices = (
        ('Low', 'Низкий'),
        ('Middle', 'Средний'),
        ('High', 'Высокий'),
    )
    priority = forms.ChoiceField(choices=priority_choices, required=True, initial='Middle')

    status_choices = (
        ('Approved', 'Подтверждено'),
        ('Not Approved', 'Не подтверждено'),
    )
    status = forms.ChoiceField(choices=status_choices, required=True, initial='Not Approved')

    def __init__(self, types, *args, **kwargs):
        super(RequirementForm, self).__init__(*args, **kwargs)
        self.fields['type'] = forms.ChoiceField(choices=types)

    field_order=['id', 'description', 'type', 'priority', 'status']

    # class Meta:
    #     model = Requirement
    #     fields = ['id', 'description', 'type', 'priority', 'status']
    #     labels = {
    #         'id': 'Идентификатор',
    #         'description': 'Описание',
    #         'type': 'Тип',
    #         'priority': 'Приоритет',
    #         'status': 'Статус',
    #     }

    # def __init__(self, *args, **kwargs):
    #     super(RequirementForm, self).__init__(*args, **kwargs)
    #     self.fields['type'].empty_label = 'Не выбрано'


# def requirement_create(request):
#     if request.method == 'POST':
#         form = RequirementForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('requirement_list')
#     else:
#         form = RequirementForm()
#     return render(request, 'requirement_create.html', {'form': form})
