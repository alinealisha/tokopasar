from django.shortcuts import render

def show_main(request):
    context = {
        'nama_toko' : 'Toko Pasar',
        'name': 'Alisha Aline Athiyyah',
        'class': 'PBP B',
        'rating' : '10'
    }

    return render(request, "main.html", context)
