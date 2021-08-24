from django import forms
from django.contrib.auth.models import User




class UserCreationForm(forms.ModelForm):
   
    username= forms.CharField(label ="Nom d'utilisateur", max_length=40, help_text="Entrez un nom d'utilisateur valide. Cette valeur ne peut contenir que des lettres, des chiffres et des caractères @/./+/-/_.")
    email = forms.EmailField(label ='E-mail')
    first_name = forms.CharField(label = 'Prénom', max_length=40)
    last_name = forms.CharField(label = 'Nom', max_length=40)
    password1 = forms.CharField(label='Mot de passe', max_length=40, widget=forms.PasswordInput(), min_length=8)
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1')
    
    


    def clean_email(self):
        # Get the email
        email = self.cleaned_data.get('email')

        # Check to see if any users already exist with this email as a username.
        try:
            match = User.objects.get(email=email)
        except User.DoesNotExist:
            # Unable to find a user, this is fine
            return email

        # A user was found with this as a username, raise an error.
        raise forms.ValidationError('Cette adresse email est déjà utilisée.')
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            natch = User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("Ce nom d'utilisateur est déjà utilisé.")

        
            

    

        




class LoginForm(forms.ModelForm):
    username = forms.CharField(label="Nom d'utilusateur")
    password = forms.CharField(
        label='Mot de passe:', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields =('username', 'password')

    
    
    
   