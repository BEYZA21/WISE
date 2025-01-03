from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def upload_image(request):
    return render(request, 'upload_image.html')

@login_required
def view_graphs(request):
    return render(request, 'view_graphs.html')

@login_required
def view_results(request):
    return render(request, 'view_results.html')

@login_required
def generate_reports(request):
    return render(request, 'generate_reports.html')
