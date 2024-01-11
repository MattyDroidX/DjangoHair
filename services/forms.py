from django import forms

class ConfirmDeleteForm(forms.Form):
    confirmation = forms.BooleanField(help_text="Confirmo que deseo eliminar las OpeningHours pasadas.")