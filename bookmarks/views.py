from django.shortcuts import render, redirect, get_object_or_404
from .models import Bookmark
from .forms import BookmarkForm

def bookmark_list(request):
    if request.method == 'POST':
        form = BookmarkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bookmark_list')
    else:
        form = BookmarkForm()

    bookmarks = Bookmark.objects.all().order_by('-created_at')
    return render(request, 'bookmarks/bookmark_list.html', {
        'bookmarks': bookmarks,
        'form': form,
    })

def add_bookmark(request):
    if request.method == 'POST':
        form = BookmarkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bookmark_list')  # Adjust to your list view name
    else:
        form = BookmarkForm()
    return render(request, 'bookmarks/add_bookmark.html', {'form': form})

def delete_bookmark(request, pk):
    bookmark = get_object_or_404(Bookmark, pk=pk)
    if request.method == 'POST':
        bookmark.delete()
    return redirect('bookmark_list')

def edit_bookmark(request, pk):
    bookmark = get_object_or_404(Bookmark, pk=pk)
    if request.method == 'POST':
        form = BookmarkForm(request.POST, instance=bookmark)
        if form.is_valid():
            form.save()
            return redirect('bookmark_list')
    else:
        form = BookmarkForm(instance=bookmark)
    return render(request, 'bookmarks/edit_bookmark.html', {'form': form})
