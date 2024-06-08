import json
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.db.models import Q

from django.shortcuts import render, redirect
from .models import VehicleInspection
from .forms import UploadFileForm


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return redirect('upload_file')
    else:
        form = UploadFileForm()

    # Fetch all records to display in the table
    inspections = VehicleInspection.objects.all()[:50]
    return render(request, 'inspections/upload.html', {'form': form, 'inspections': inspections})


def handle_uploaded_file(file):
    data = json.load(file)
    for item in data:
        VehicleInspection.objects.update_or_create(
            model_year=item['model_year'],
            make=item['make'],
            model=item['model'],
            defaults={
                'rejection_percentage': item['rejection_percentage'],
                'reason_1': item.get('reason_1', ''),
                'reason_2': item.get('reason_2', ''),
                'reason_3': item.get('reason_3', '')
            }
        )


def live_search(request):
    query = request.GET.get('query', '')
    results = VehicleInspection.objects.filter(
        Q(model_year__icontains=query) |
        Q(make__icontains=query) |
        Q(model__icontains=query) |
        Q(rejection_percentage__icontains=query) |
        Q(reason_1__icontains=query) |
        Q(reason_2__icontains=query) |
        Q(reason_3__icontains=query)
    )[:50]
    html = render_to_string('inspections/results.html', {'results': results})
    return JsonResponse({'html': html})
