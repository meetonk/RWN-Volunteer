# forms.py
from django import forms
from django.db.models import Q

from . import models
from .models import JobApplication, ApplicationStatus

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['company', 'position', 'notes']
        #   fields = ['company', 'position', 'location', 'status', 'job_link', 'notes']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        # if user is not None:
        #     self.fields['status'].queryset = ApplicationStatus.objects.filter(user=user)


# forms.py

class ApplicationStatusForm(forms.ModelForm):
    class Meta:
        model = ApplicationStatus
        fields = ['name']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)



from django import forms
from .models import ApplicationStatusUpdate

class ApplicationStatusUpdateForm(forms.ModelForm):
    class Meta:
        model = ApplicationStatusUpdate
        fields = ['status', 'date', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            DEFAULT_STATUSES = ['Applied', '1st Interview', 'Rejected', 'Offer']

            self.fields['status'].queryset = ApplicationStatus.objects.filter(
                Q(user=user) | Q(name__in=DEFAULT_STATUSES)
            )
