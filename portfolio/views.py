from django.shortcuts import render

def home(request):
    projects_list = [
        {
            'title': 'Tourism Website',
            'description': 'Coming this project very soon ',
            'tech': 'Python, Django, Javascript',
            'github':"https://github.com/Shaid30/Tourism-website-.git"
        },
        {
            'title': 'Weather App',
            'description': 'Real-time weather forecast application using API integration',
            'tech': 'Python, API, HTML/CSS',
            
        },
        {
            'title': 'Todo App',
            'description': 'A  simple todo app only add and delete',
            'tech': 'Django, Bootstrap, JavaScript',
            'github':"https://github.com/Shaid30/todo-app.git"
        },
    ]
    return render(request, 'portfolio/home.html', {'projects': projects_list})

def about(request):
    return render(request, 'portfolio/about.html')

def projects(request):
    return render(request, 'portfolio/projects.html')

def contact(request):
    return render(request, 'portfolio/contact.html')
