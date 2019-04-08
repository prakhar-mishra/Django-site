from django.shortcuts import render
from .assignment_service import perform_twitter_analysis

def week1(request):
    return render(request, 'data_science/week1_form.html')

def twitter_analysis(request):
    query = request.POST['query']
    feed_analysis = perform_twitter_analysis(query)
    context = {'feed_analysis': feed_analysis}
    return render(request, 'data_science/analysis.html', context)

