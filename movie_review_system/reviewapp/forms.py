from django import forms
from .models import Movie_review,Genre

movie_detail = [('Published','Published'),('NotPublished','NotPublished')]
    
CONTENT = [('Horror','Horror'),('Comedy','Comedy'),('Action','Action'),('Sci-Fi','Sci-Fi'),('Thriller','Thriller')]
class Movie_Review_Form(forms.ModelForm):
    genres = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required = True
    )
    class Meta:
        model = Movie_review
        fields = '__all__'
        widgets = {
            'id' : forms.TextInput(attrs={
                'class': 'form-control bg-dark text-light',
            }),
            'movieTitle': forms.TextInput(attrs={
                'class': 'form-control bg-dark text-light',
            }),
            'director': forms.TextInput(attrs={
                'class': 'form-control bg-dark text-light',
            }),
            'reviewContent': forms.TextInput(attrs={
                'class': 'form-control bg-dark text-light',
            }),
            'rating': forms.NumberInput(attrs={
                'class': 'form-control bg-dark text-light',
            }),
            'created_At': forms.DateInput(attrs={
                'class': 'form-control bg-dark text-light',
            }),
            'rewiever_emil_Id': forms.EmailInput(attrs={
                'class': 'form-control bg-dark text-light',
            }),
            'status': forms.Select(choices=movie_detail, attrs={
                'class': 'form-control bg-dark text-light',
            }),
            'genres': forms.CheckboxSelectMultiple(attrs={
                'class': 'form-control bg-dark text-light',
            }),
        }
        
        