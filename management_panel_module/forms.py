from datetime import datetime

from django import forms
from django.core.exceptions import ValidationError
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime
from jdatetime import datetime as jalali_date_time

from lesson_module.models import SetHomeWork, Lesson
from utils.time import end_time_calculator

now_year = datetime.now().year
now_year_jalali = jalali_date_time.now().year
YEAR_CHOICES = {
    (now_year, now_year_jalali),
    (now_year + 2, now_year_jalali + 2),
    (now_year + 1, now_year_jalali + 1),
}


class SetHomeWorkForm(forms.Form):
    title = forms.CharField(label='عنوان تکلیف')
    end_at = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'id': 'datepicker', 'class': 'form-control', 'type': 'datetime-local'}),
        label="زمان پایان مهلت")
    # end_at = SplitJalaliDateTimeField(widget=AdminSplitJalaliDateTime,
    #                          label="زمان پایان مهلت")
    # end_at = JalaliDateField(widget=AdminJalaliDateWidget(attrs={'id': 'datepicker'}),
    #                                   label="زمان پایان مهلت")
    lesson = forms.ModelChoiceField(label='مربوط به درس', widget=forms.Select(attrs={'class': 'custom-select'}),
                                    queryset=Lesson.objects.all())
    description = forms.CharField(widget=forms.Textarea, label='توضیحات تکلیف')
    #
    # year = forms.ChoiceField(choices=YEAR_CHOICES, widget=forms.Select(attrs={'class': 'custom-select form-control'}),
    #                          label="سال")


class EditHomeWorkForm(forms.ModelForm):
    class Meta:
        model = SetHomeWork
        fields = ['title', 'end_at', 'description']
        widgets = {
            'end_at': forms.DateTimeInput(
                attrs={'id': 'datepicker', 'class': 'form-control', 'type': 'datetime-local'}),
            'description': forms.Textarea
        }
