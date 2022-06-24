from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Bunk

def redirect_global_feed(request):
    return HttpResponseRedirect(reverse('bunk:global_feed'))

class GlobalFeed(generic.ListView):
    template_name = 'bunk/global_feed.html'
    context_object_name = 'bunk_list'

    def get_queryset(self):
        return Bunk.objects.order_by('time')