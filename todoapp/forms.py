from django import forms

from .models import Todo


class TodoCreationForm(forms.ModelForm):
    class Meta:
        model = Todo
        CHOICES = (
            ("In Progress", "In Progress"),
            ("Completed", "Completed"),
            ("Pending", "Pending"),
        )
        fields = ("title", "description", "due_date", "status")
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "due_date": forms.SelectDateWidget(),
            "status": forms.RadioSelect(attrs={"choices": CHOICES}),
        }
