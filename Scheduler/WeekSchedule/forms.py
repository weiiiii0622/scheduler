from django.forms import ModelForm, DateInput, ValidationError, IntegerField, NumberInput
from WeekSchedule.models import Event

class EventForm(ModelForm):
    class Meta:
        model = Event

        widgets = {
            'start_time': DateInput(attrs={'type': 'datetime-local', 'placeholder': "yyyy-mm-dd", 'onChange': ''}, format='%Y-%m-%dT%H:%M'),
            'clock': NumberInput(attrs={'type': 'number'}),
        }
        exclude = ['status', 'end_time']

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)

        self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)

    def clean_start_time(self, *args, **kwargs):
        start_time = self.cleaned_data["start_time"]

        check_event = Event.objects.filter(start_time__contains = start_time.date())

        for event in check_event:
            if start_time.time() < event.end_time.time():
                raise ValidationError("Error !!")
        

        return start_time
