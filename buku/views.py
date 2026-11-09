from django.shortcuts import render
from django.http import Http404

DATA_BUKU = [
    {"id": 1, "judul": "Belajar PHP"},
    {"id": 2, "judul": "Apa Aja"},
]

def daftar_buku(request):
    return render(request, "buku/daftar_buku.html", {
        "daftar_buku": DATA_BUKU
    })

def detail_buku(request, id):
    buku = next(
        (item for item in DATA_BUKU if item["id"] == id),
        None
    )

    if buku is None:
        raise Http404("Buku tidak ditemukan")

    return render(request, "buku/detail_buku.html", {
        "buku": buku
    })
