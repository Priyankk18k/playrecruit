from django.shortcuts import render

# Create your views here.
def vw_index(request):
    return render(request, 'admin/index.html')