from django import forms
from .models import Requirement
from django.shortcuts import render, redirect


class RequirementForm(forms.ModelForm):
    class Meta:
        model = Requirement
        fields = ['id', 'description', 'type', 'priority', 'status']


# def requirement_create(request):
#     if request.method == 'POST':
#         form = RequirementForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('requirement_list')
#     else:
#         form = RequirementForm()
#     return render(request, 'requirement_create.html', {'form': form})
