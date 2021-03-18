from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Note


def index(request):
    if request.method == 'POST':
        ID = request.POST.get('id')
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')

        print(f'id = {ID}')
        print(f'título = {title}')
        print(f'content = {content}')

        if ID == '':
            Note(title=title, content=content).save()
            
        else:
            if title == None:
                Note.objects.filter(id=ID).delete()
            else:
                note = Note.objects.get(id=ID)
                note.title = title
                note.content = content
                note.save()

        
        return redirect('index')

    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})