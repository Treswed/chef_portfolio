from django import forms
from django.contrib import admin
from .models import ChefProfile, Testimonial, Visit
from .models import Statistic


class StatisticForm(forms.ModelForm):
    class Meta:
        model = Statistic
        fields = ['key', 'label', 'value', 'icon', 'order']

    def clean_value(self):
        raw = self.cleaned_data.get('value')
        # If the admin provided a string with commas in a custom admin widget,
        # Django will already coerce to int for BigIntegerField. But to be robust
        # (and if some admin interfaces send strings), accept strings and strip
        # non-digits.
        if isinstance(raw, str):
            cleaned = ''.join(ch for ch in raw if ch.isdigit() or ch == '-')
            try:
                val = int(cleaned)
            except Exception:
                raise forms.ValidationError('Please enter a valid integer (commas allowed).')
        else:
            val = int(raw or 0)

        if val < 0:
            raise forms.ValidationError('Value must be zero or greater.')
        return val

@admin.register(ChefProfile)
class ChefProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'years_experience']
    
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'is_featured', 'created_at']
    list_filter = ['rating', 'is_featured']
    search_fields = ['name', 'content']


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ['timestamp', 'path', 'user', 'ip_address', 'status_code']
    list_filter = ['method', 'status_code']
    search_fields = ['path', 'user_agent', 'referrer', 'ip_address']
    readonly_fields = ['timestamp', 'path', 'method', 'status_code', 'ip_address', 'user_agent', 'referrer', 'session_key']
    ordering = ['-timestamp']


@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    form = StatisticForm
    list_display = ['label', 'key', 'value', 'icon', 'order']
    list_editable = ['value', 'order']
    ordering = ['order']