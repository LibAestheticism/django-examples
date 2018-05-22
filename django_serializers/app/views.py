import json
from .models import Book
from django.http import JsonResponse
from django.core.serializers import serialize


# Create your views here.
def get_books(request):
    book = Book.objects.all()
    json_str = serialize('json', book, use_natural_foreign_keys=True)
    return JsonResponse({'books': json.loads(json_str)})


