from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Note


def index(request):
    if request.method == 'POST':
        Note.objects.all().delete()

        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')

        if request.POST.get('tag') == None:
            tag = request.POST.get('tag')
        else:
            if request.POST.get('tag')[0] == '#':
                tag = request.POST.get('tag').lower()
            else:
                tag = '#'+request.POST.get('tag').lower()

        print(f'título = {title}')
        print(f'content = {content}')
        print(f'tag = {tag}')

        Note(title=title, content=content, tag=tag).save()

        all_notes = Note.objects.all()
            
        return redirect('index')

    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})