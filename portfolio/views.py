from django.shortcuts import render

def home(request):
    return render(request, 'portfolio/home.html')

def about(request):
    return render(request, 'portfolio/about.html')

def projects(request):
    projects_list = [
        {
            'title': 'E-commerce Website',
            'description': 'A fully functional online shopping platform built with Django',
            'tech': 'Django, PostgreSQL, Bootstrap'
        },
        {
            'title': 'Weather App',
            'description': 'Real-time weather forecast application using API integration',
            'tech': 'Python, API, HTML/CSS'
        },
        {
            'title': 'Task Manager',
            'description': 'A todo list application with user authentication',
            'tech': 'Django, SQLite, JavaScript'
        },
    ]
    return render(request, 'portfolio/projects.html', {'projects': projects_list})

def contact(request):
    return render(request, 'portfolio/contact.html')
