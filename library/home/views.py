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
def add_book(request,author_id):
  if request.method == 'POST':
    book_name = request.POST.get('book_name')
    author_id=request.POST.get('author_id')
    author_name = request.POST.get('author_name')
    ISBN = request.POST.get('ISBN')
    Publication_date = request.POST.get('Publication_date')

    try:
      print(f"Author_id={author_id}")
      author = Author.objects.get(pk=author_id)
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
        author_id=request.POST.get('author_id')
        auth=Author(name=Author_name,email=Email,author_id=author_id)
        auth.save()
    return redirect('/index')    
def update(request, id):
  if request.method == 'POST':
    book_name = request.POST.get('book_name')
    ISBN = request.POST.get('ISBN')
    Publication_date = request.POST.get('Publication_date')

    try:
      book = Book.objects.get(pk=id)
      book.title = book_name
      book.isbn = ISBN
      book.publication_date = Publication_date
      book.full_clean()  
      book.save()
      return redirect('/index') 
    except (Book.DoesNotExist, ValidationError) as e:
      context = {'errors': e}
      return redirect(request, '/index', context)
  else:
    book = Book.objects.get(pk=id)
    context = {'book': book}
    return redirect(request, '/index', context)
  
from django.shortcuts import render, redirect

def delete_book(request, id):
    if request.method == 'POST':
        book = Book.objects.get(pk=id)
        book.delete()
        return redirect('/index')
    else:
        book = Book.objects.get(pk=id)
        context = {'book': book}
        return redirect(request, '/index', context)