from django.shortcuts import render

def adding(request):
    return render(request, 'post-ads.html',{})
