from django.forms import ModelForm, DateInput
from WeekSchedule.models import Event

class EventForm(ModelForm):
    class Meta:
        model = Event
        widgets = {
            'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        }
        exclude = ['status']

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)

        self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)