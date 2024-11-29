from django.shortcuts import render,HttpResponse,redirect
from pydantic import ValidationError
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from home.models import Book
from home.models import Author
def index(request):
    bk=Book.objects.all() 
    author = Author.objects.all()
    context={
        'bk':bk,
        'author':author
    }

    return render(request,'index.html',context)
def add_book(request):
  if request.method == 'POST':
    book_name = request.POST.get('book_name')
    author_id=request.POST.get('author_id')
    author_name = request.POST.get('author_name')
    ISBN = request.POST.get('ISBN')
    Publication_date = request.POST.get('Publication_date')

    try:
      print(f"Author_id={author_id}")
      author = Author.objects.get(pk=author_id)
      book = Book.objects.create(title=book_name, author=author, isbn=ISBN, publication_date=Publication_date)
      return redirect('/index')
    except (Author.DoesNotExist, ValidationError) as e:
      context = {'errors': e}
      import traceback
      traceback.print_exc()
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
def page_login(request):
   return render(request,'login.html')    
def login_view(request):
    if request.method == 'POST': 
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        print(username,password)
        if user is not None:
            login(request, user)
            return redirect('/index')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request,'signup.html')
def signup(request):
   return render(request,'signup.html')   

def sign_up(request):
    if request.method=="POST":
        Username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        print(f"all details {Username},{email},{password}")
    else:
         messages.error(request, 'Invalid username or password')
    if User.objects.filter(username=Username).exists():
        messages.error(request, 'Username is already taken.')
    elif User.objects.filter(email=email).exists():
        messages.error(request, 'Email is already registered.')
    else:
        user = User.objects.create_user(username=Username, email=email, password=password)
        user.save()
        messages.success(request, 'Account created successfully!')
        return redirect('/index')      
    return render(request,'signup.html')    