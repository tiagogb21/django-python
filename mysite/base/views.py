from django.shortcuts import render


rooms = [
    {'id': 1, 'name': 'django'},
    {'id': 2, 'name': 'Design with me'},
    {'id': 3, 'name': 'Frontend'},
]


def home(request):
    return render(request, 'home.html')


def room(request):
    return render(request, 'room.html', {'rooms': rooms})
