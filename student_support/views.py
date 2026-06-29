from django.shortcuts import render, redirect
from .forms import ComplaintForm
from .models import Complaint


def home(request):
    return render(request, 'home.html')

def complaint(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('complaint')  # 🔥 important change

    else:
        form = ComplaintForm()

    complaints = Complaint.objects.all().order_by('-id')  # 🔥 fetch data

    return render(request, 'complaint.html', {
        'form': form,
        'complaints': complaints
    })

def complaint_list(request):
    complaints = Complaint.objects.all()
    return render(request, 'complaint_list.html', {'complaints': complaints})