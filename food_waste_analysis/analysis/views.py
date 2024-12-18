from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseBadRequest

# Ana sayfa
def index(request):
    """Ana sayfa görünümü."""
    return render(request, 'analysis/index.html')

# Resim yükleme
def upload(request):
    """Resim yükleme görünümü."""
    if request.method == "POST":
        images = request.FILES.getlist("images")  # Yüklenen dosyaları al
        if not images:  # Eğer dosya yüklenmediyse hata döndür
            return HttpResponseBadRequest("Lütfen en az bir dosya yükleyin.")

        fs = FileSystemStorage()
        uploaded_files = []

        for image in images:
            try:
                filename = fs.save(image.name, image)  # Dosyayı kaydet
                uploaded_files.append(fs.url(filename))  # URL'yi listeye ekle
            except Exception as e:  # Hata yakalama
                return HttpResponseBadRequest(f"Dosya yüklenirken hata oluştu: {e}")

        # Dosyalar başarıyla yüklendiyse, kullanıcıyı başarı mesajıyla yeniden yönlendir
        return render(request, 'analysis/upload.html', {'images': uploaded_files, 'message': "Dosyalar başarıyla yüklendi."})

    # GET isteği durumunda boş bir şablon döndür
    return render(request, 'analysis/upload.html')

# Grafikler
def graphs(request):
    """Grafikler görünümü."""
    return render(request, 'analysis/graphs.html')

# Sonuçlar
def results(request):
    """Sonuçlar görünümü."""
    return render(request, 'analysis/results.html')

# Rapor oluşturma
def report(request):
    """Rapor oluşturma görünümü."""
    return render(request, 'analysis/report.html')
