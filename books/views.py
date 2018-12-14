from django.shortcuts import render, redirect
from django.http import HttpResponse,Http404
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.views import generic
from .models import Book, BookInstance, Author, Genre
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from books.forms import SignUpForm
import datetime


from django.shortcuts import get_object_or_404

def home_view( request, *args, **kwargs):


    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    bookList = Book.objects.all()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'book_list': bookList,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'home.html', context=context)


def about_view(request):



    context={}
    return render(request, "about.html", context)

@login_required
def borrow_view(request):
    book_instance_list= BookInstance.objects.filter(borrower=request.user).filter(status__exact='o').order_by('due_back')
    context= {'book_instance_list': book_instance_list}

    return render(request, 'borrowed.html', context=context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def issue_view(request):
    book_list= BookInstance.objects.filter(borrower=request.user).filter(status__exact='o').order_by('due_back')
    context= {'book_list': book_list}

    return render(request, 'issue.html', context=context)





class BookListView(generic.ListView):
    """
    Generic class-based view for a list of books.
    """
    model = Book



class BookDetailView(generic.DetailView):
    """
    Generic class-based detail view for a book.
    """
    model = Book


@login_required
def issue_request_view(request, pk):
    book_inst = get_object_or_404(BookInstance, pk=pk)
    print(book_inst.id)
    book_inst.borrower = request.user
    print(book_inst.borrower)
    book_inst.due_back= datetime.date.today() + datetime.timedelta(weeks=3)
    book_inst.status = 'o'
    book_inst.save()
    return render(request, 'issuechange.html', {})


def return_request_view(request, pk):
    book_inst = get_object_or_404(BookInstance, pk=pk)

    book_inst.borrower = None
    print(book_inst.borrower)
    book_inst.due_back = None
    book_inst.status = 'a'
    book_inst.save()
    return render(request, 'returned.html', {})