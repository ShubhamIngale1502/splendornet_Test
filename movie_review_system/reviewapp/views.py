from django.shortcuts import render,redirect
from .forms import Movie_Review_Form
from .models import Movie_review,Genre
from django.db.models import Q

def create(request):
    template_name = 'reviewapp/insert.html'
    form = Movie_Review_Form()
    if request.method == 'POST':
        form = Movie_Review_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show')
    context = {'forms':form}
    return render(request,template_name,context)

def show_details(request):
    template_name = 'reviewapp/show.html'
    query = request.GET.get('q')
    status_filter = request.GET.get('status')
    genre_filter = request.GET.getlist('genres')

    reviews = Movie_review.objects.all()

    if query:
        reviews = reviews.filter(Q(movieTitle__icontains=query) | Q(director__icontains=query))
    
    if status_filter:
        reviews = reviews.filter(status=status_filter)
    
    if genre_filter:
        reviews = reviews.filter(genres__id__in=genre_filter).distinct()
    genres = Genre.objects.all()
    context = {'reviews':reviews,'genres':genres}   
    return render(request,template_name,context)

def update_details(request,pk):
    template_name = 'reviewapp/insert.html'
    data = Movie_review.objects.get(pk=pk)
    form = Movie_Review_Form(instance=data)
    if request.method == 'POST':
        form = Movie_Review_Form(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('show')
    context = {'forms':form}
    return render(request,template_name,context)

def delete_details(request,pk):
    template_name = 'reviewapp/delete.html'
    data = Movie_review.objects.get(pk=pk)
    if request.method == 'GET':
        context = {'movies':data}
        return render(request,template_name,context)
    data.delete()
    return redirect('show')

