from django.shortcuts import render

def show_main(request):
    context = {
        'nama_toko' : 'Toko Pasar',
        'name': 'Alisha Aline Athiyyah',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
