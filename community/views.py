from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from accounts.models import Account
from .models import Review, Comment
from .forms import ReviewForm, CommentForm

# Create your views here.
def index(request):
    reviews = Review.objects.order_by('-pk')
    context = {
        'reviews': reviews,
    }
    return render(request, 'index.html', context)

@login_required
def new(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            user = Account.objects.get(username=request.user)
            review.creator = user
            review.save()
            return redirect('community:detail', review.pk)
    # invalid
    form = ReviewForm()
    context = {
        'form': form,
    }
    return render(request, 'new.html', context)

def detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comments = review.comments.all()
    form = CommentForm()
    context = {
        'review': review,
        'comments': comments,
        'form': form,
    }
    return render(request, 'detail.html', context)

@login_required
def delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.user == review.creator:
        review.delete()
    return redirect('community:index')

@login_required
def update(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.user == review.creator:
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.creator = request.user
            review.save()
            return redirect('community:detail', review.pk)
    # invalid
    form = ReviewForm(instance=review)
    context = {
        'form': form,
    }
    return render(request, 'new.html', context=context)

@require_POST
@login_required
def comments(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.creator = request.user
        comment.review = review
        comment.save()
    return redirect('community:detail', review.pk)

