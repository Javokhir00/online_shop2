from django import forms
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


class EmailForm(forms.Form):
    from_email = forms.EmailField(label='From Email')
    recipient_list = forms.CharField(
        label='Recipients (comma-separated)',
        help_text='Enter multiple emails separated by commas'
    )
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)

    def clean_recipient_list(self):
        data = self.cleaned_data['recipient_list']
        emails = [email.strip() for email in data.split(',') if email.strip()]
        if not emails:
            raise ValidationError("You must provide at least one recipient email.")


        for email in emails:
            try:
                validate_email(email)
            except ValidationError:
                raise ValidationError(f"Invalid email: {email}")

        return emails


