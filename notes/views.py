from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Note


def index(request):
    if request.method == 'POST':
        ID = request.POST.get('id')
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')

        if request.POST.get('tag') == None:
            tag = request.POST.get('tag')
        else:
            if request.POST.get('tag')[0] == '#':
                tag = request.POST.get('tag')
            else:
                tag = '#'+request.POST.get('tag')

        print(f'id = {ID}')
        print(f'título = {title}')
        print(f'content = {content}')
        print(f'tag = {tag}')

        if ID == '':
            Note(title=title, content=content, tag=tag).save()
            
        else:
            if title == None:
                Note.objects.filter(id=ID).delete()
            else:
                note = Note.objects.get(id=ID)
                note.title = title
                note.content = content
                note.tag = tag
                note.save()

        
        return redirect('index')

    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})