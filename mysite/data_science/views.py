from django.shortcuts import render
from .assignment_service import perform_twitter_analysis
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

def week1(request):
    return render(request, 'data_science/week1_form.html')

@cache_page(CACHE_TTL)
def twitter_analysis(request):
    query = request.POST['query']
    feed_analysis = perform_twitter_analysis(query)
    context = {'feed_analysis': feed_analysis}
    return render(request, 'data_science/analysis.html', context)

