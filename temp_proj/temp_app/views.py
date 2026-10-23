from django.shortcuts import render

# Create your views here.

def info(request):
    context = {
        'name': 'Ana',
        'surname': 'Kalandadze',
        'age': 20,
    }

    return render(request, 'info.html', context)




def hobbies(request):
    context = {
        'hobbies': ['Reading', 'Coding', 'Music', 'Traveling'],
        'grade': 11,
    }
    return render(request, 'hobbies.html', context)