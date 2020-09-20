from django.forms import ModelForm, DateInput, ValidationError, IntegerField, NumberInput
from WeekSchedule.models import Event
import datetime

class EventForm(ModelForm):
    class Meta:
        model = Event

        widgets = {
            'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'clock': NumberInput(attrs={'type': 'number'}),
        }
        exclude = ['status', 'end_time']

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)

        self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)

    def clean_start_time(self, *args, **kwargs):
        start_time = self.cleaned_data["start_time"]
        clock = self.data['clock']
        minute = int(clock) * 30
        end_time = start_time + datetime.timedelta(minutes = minute)

        check_event = Event.objects.filter(start_time__contains = start_time.date())
        print(check_event)
        for event in check_event:
            if start_time.time() > event.start_time.time() or end_time.time() > event.start_time.time():
                raise ValidationError("Error !!")

        return start_time
