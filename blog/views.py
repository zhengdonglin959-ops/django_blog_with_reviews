from django.shortcuts import render, redirect
from .models import Post, Review
from .forms import ReviewForm


def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})


def about(request):
    return render(request, 'about.html')


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post.html', {'post': post})


def reviews(request):
    """Страница с отзывами и формой добавления.
    На странице отображаются только отзывы, прошедшие проверку администратором
    (is_checked = True).
    """
    approved_reviews = Review.objects.filter(is_checked=True)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reviews')
    else:
        form = ReviewForm()

    return render(request, 'reviews.html', {
        'reviews': approved_reviews,
        'form': form,
    })
