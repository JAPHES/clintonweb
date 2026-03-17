from django.http import HttpResponse


def health(request):
    # Lightweight health check that avoids touching the database or templates
    return HttpResponse("OK", content_type="text/plain")
