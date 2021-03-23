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
                tag = request.POST.get('tag').lower()
            else:
                tag = '#'+request.POST.get('tag').lower()

        print(f'id = {ID}')
        print(f'título = {title}')
        print(f'content = {content}')
        print(f'tag = {tag}')

        if ID == '':
            Note(title=title, content=content, tag=tag).save()
            
        else:
            if tag == None:
                Note.objects.filter(id=ID).delete()

            elif ID == None:
                all_notes = Note.objects.all()
                tag_notes = []

                for note in all_notes:
                    if note.tag == tag:
                        tag_notes.append(note)
                
                print(tag_notes)

                return tags(request, tag_notes)

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
    

def tags(request, notes):
    return render(request, 'notes/tags.html', {'notes': notes})

