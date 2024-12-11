from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404

from .forms import BookRecommendationForm
from .models import BookRecommendation


def book_recommendation_view(request):
    if request.method == 'POST':
        form = BookRecommendationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recommendation_list')
    else:
        form = BookRecommendationForm()
    return render(request, 'recommendations_book/book_recommendation.html', {'form': form})


def like_recommendation_view(request, pk):
    recommendation = BookRecommendation.objects.get(pk=pk)
    recommendation.likes += 1
    recommendation.save()
    return redirect('recommendation_list')


def recommendation_list_view(request):
    recommendations = BookRecommendation.objects.all().order_by('-likes')
    return render(request, 'recommendations_book/recommendations_list.html', {'recommendations': recommendations})


def delete_recommendation_view(request, pk):
    recommendation = get_object_or_404(BookRecommendation, pk=pk)
    if recommendation.hiker != request.user:
        return HttpResponseForbidden("You are not allowed to delete this recommendation.")
    if request.method == 'POST':
        recommendation.delete()
        return redirect('recommendation_list')
    return render(request, 'recommendations_book/delete_recommendation.html', {'recommendation': recommendation})
