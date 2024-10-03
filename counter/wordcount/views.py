from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .models import WordCounter


word_counter = WordCounter()

def home(request):
    count = None

    if request.method == 'POST':

        if 'upload_file' in request.POST and request.FILES['file']:
            file = request.FILES['file']
            text = file.read().decode('utf-8')
            word_counter.load(text)

        # Подсчет слов
        elif 'wordcount' in request.POST:
            word = request.POST.get('word', '')
            count = word_counter.wordcount(word)


        elif 'clear_memory' in request.POST:
            word_counter.clear_memory()
            count = None


    return render(request, 'wordcount/home.html', {
        'word_counter': word_counter,
        'count': count,
    })
