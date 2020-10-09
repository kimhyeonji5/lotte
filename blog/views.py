from django.shortcuts import render

# Create your views here.
def child(request):
    return render(request, 'child.html')

def cor_main(request):
    return render(request, 'cor_main.html')    