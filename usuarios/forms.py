from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
   
    class Meta:
        model = Usuario

        fields = ('first_name','username','password','email','estado','municipio','foto')
        widgets = {
            'password': forms.PasswordInput(attrs={'class':'forms-control', 'placeholder':'Contraseña'}),
            'estado': forms.Select(attrs={'class':'forms-control'})
        }

    def save(self, commit=True):
        user = super(UsuarioForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user