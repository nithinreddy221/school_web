from django.shortcuts import render

def landing_page(request):
    return render(request, 'welcom_page.html')  # Ensure the correct filename
