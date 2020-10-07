from django.forms import ModelForm, DateInput, ValidationError, IntegerField, NumberInput
from WeekSchedule.models import Event

import datetime

class EventForm(ModelForm):
    class Meta:
        model = Event

        widgets = {
            'start_time': DateInput(attrs={'type': 'datetime-local', 'placeholder': "yyyy-mm-dd", 'onChange': ''}, format='%Y-%m-%dT%H:%M'),
            'clock': NumberInput(attrs={'type': 'number'}),
        }
        exclude = ['user', 'status', 'end_time']

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)

        self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)

    def clean_start_time(self, *args, **kwargs):
        print('hi')
        start_time = self.cleaned_data["start_time"]
        clock = int(self.data["clock"])
        minute = clock * 30
        end_time = start_time + datetime.timedelta(minutes = minute)

        check_event = Event.objects.filter(start_time__contains = start_time.date())

        for event in check_event:
            event_start_time = event.start_time + datetime.timedelta(hours = 8)
            event_end_time = event.end_time + datetime.timedelta(hours = 8)

            if start_time.time() < event_start_time.time():
                if end_time.time() > event_start_time.time():
                    print(start_time, event_start_time, event_end_time)
                    raise ValidationError("Your time has conflicted!!")
            elif start_time.time() < event_end_time.time():
                print(start_time, event_start_time, event_end_time)
                raise ValidationError("Your time has conflicted!!")

        return start_time
