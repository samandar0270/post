from django.shortcuts import render

def contacting(request):
    return render(request, 'contact.html', {})
