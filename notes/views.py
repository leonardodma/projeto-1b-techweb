from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Note

def tags(request, notes):
    return render(request, 'notes/tags.html', {'notes': notes})

def tags_list(request, notes):
    if request.method == 'POST':
        redirect_tag = request.POST.get('redirect_tag')
        print(f'redirect to tag: {redirect_tag}')

    return render(request, 'notes/tags_list.html', {'notes': notes})

def index(request):
    if request.method == 'POST':
        ID = request.POST.get('id')
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        mostrar_tags = request.POST.get('mostrar_tags')

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
        print(f'Mostrar Tags = {mostrar_tags}')

        all_notes = Note.objects.all()


        if mostrar_tags == 'true':
            all_tags = []
            notes = []
            for note in all_notes:
                if note.tag in all_tags:
                    pass
                else:
                    all_tags.append(note.tag)
                    notes.append(note)

            print(all_tags)
            return tags_list(request, notes)
            
        else:
            if ID == '':
                Note(title=title, content=content, tag=tag).save()
                
            else:
                if tag == None:
                    Note.objects.filter(id=ID).delete()

                elif ID == None:
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