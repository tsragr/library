from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.dateparse import parse_date
from .models import CSV, Author, Book
import csv
from django.views.generic import TemplateView
from .filters import BookFilter
from django.core.paginator import Paginator


@login_required
def home_view(request):
    order = request.GET.get('sort')
    if order is not None:
        books = Book.objects.order_by(order)
    else:
        books = Book.objects.all()
    myFilter = BookFilter(request.GET, queryset=books)
    books = myFilter.qs
    paginator = Paginator(books, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'filter': myFilter
    }
    return render(request, 'library/home.html', context)


class UploadTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'library/from_file.html'


@login_required
def csv_upload_view(request):
    if request.method == 'POST':
        csv_file_name = request.FILES.get('file').name
        csv_file = request.FILES.get('file')
        obj = CSV.objects.create(file_name=csv_file_name)
        obj.csv_file = csv_file
        obj.save()
        with open(obj.csv_file.path, 'r') as f:
            reader = csv.reader(f)
            reader.__next__()
            for row in reader:
                birthday = int(row[0])
                name = row[1]
                title = row[2]
                date = int(row[3])
                try:
                    author = Author.objects.get(name__iexact=name)
                except Author.DoesNotExist:
                    author = Author.objects.create(name=name, birthday=birthday)
                    author.save()
                Book.objects.get_or_create(author=author, title=title, date=date)
    return HttpResponse()
