from django import forms
from .models import Movie_review

movie_detail = [('Published','Published'),('NotPublished','NotPublished')]
    
content = [('Horror','Horror'),('Comedy','comedy'),('Action','Action'),('Sci-Fi','Sci-Fi'),('Triller','Triller')]
class Movie_Review_Form(forms.ModelForm):
    class Meta:
        model = Movie_review
        fields = '__all__'
        
        widgets = {
            'id' :forms.TextInput(attrs={
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
            'genres': forms.Select(choices=content, attrs={
                'class': 'form-control bg-dark text-light',
            }),

            
            
            
            
                
                                            
        }