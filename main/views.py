from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        "nama_apps": "Exercise sport",
        "nama_ceo": "dery andreas",
        'umur': 'PBP D'
    }
    return render(request, "main.html", context)

