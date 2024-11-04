from django.shortcuts import render,HttpResponse,redirect
from pydantic import ValidationError
from home.models import Book
from home.models import Author
def index(request):
    bk=Book.objects.all()
    context={
        'bk':bk,
    }
    return render(request,'index.html',context)
def add_book(request):
  if request.method == 'POST':
    book_name = request.POST.get('book_name')
    author_name = request.POST.get('author_name')
    ISBN = request.POST.get('ISBN')
    Publication_date = request.POST.get('Publication_date')

    try:
      author = Author.objects.get(name=author_name)
      book = Book(title=book_name, author=author, isbn=ISBN, publication_date=Publication_date)
      book.full_clean()
      book.save()
      return redirect('/index')
    except (Author.DoesNotExist, ValidationError) as e:
      context = {'errors': e}
      print("hello ")
      return redirect('/index')
  else:
    return redirect('/index')


def add_author(request):
    if request.method=='POST':
        Author_name=request.POST.get('Author_name')
        Email=request.POST.get('Email')
        auth=Author(name=Author_name,email=Email)
        auth.save()
    return redirect('/index')    

def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/create_book.html', {'form': form})
