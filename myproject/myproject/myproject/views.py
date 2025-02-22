from django.shortcuts import render

def my_view(request):
    context = {"message": "Hello, Django!"}
    return render(request, "my_template.html", context)