from django import forms


class UserForm(forms.Form):
    username = forms.CharField(
            max_length=30,
            label='Username',
            widget=forms.TextInput(attrs={'placeholder': 'Username'})
        )
    email = forms.EmailField(max_length=50, widget=forms.EmailInput, label="Email")

    '''
    El Email field valida que lo que estas ingresando es un email,
    pero si quisieras agregar una validacion propia tendrias que cambiar el campo email:

        email = forms.EmailField(
            max_length=50, 
            widget=forms.EmailInput, 
            label="Email",
            validators=[is_email_validator])
    
    donde is_email_validator es una function quedeberia verificar que el email ingresado es correcto
    '''