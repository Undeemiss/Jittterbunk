from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render

from .models import Bunk, User

def redirect_global_feed(request):
    return HttpResponseRedirect(reverse('bunk:global_feed'))

# List of all bunks
class GlobalFeed(generic.ListView):
    template_name = 'bunk/global_feed.html'
    context_object_name = 'bunk_list'

    def get_queryset(self):
        return Bunk.objects.order_by('-time')

# List of a user's received bunks
def user_feed(request, user_id, error=None):
    user = get_object_or_404(User, pk=user_id)
    bunk_list = user.bunks_received.order_by('-time');
    return render(request, 'bunk/user_feed.html', {'user': user, 'bunk_list': bunk_list, 'error': error})

# Handle Bunk submission
def bunk_submit(request, to_user_id):
    # Check if the submitted username is valid
    from_user_name = request.POST['from_username']
    try:
        from_user = User.objects.get(username = from_user_name)
    except (KeyError, User.DoesNotExist):
        err_msg = f'No user found with username "{from_user_name}"'
        return user_feed(request, to_user_id, err_msg)
    
    # Create the bunk if the username is valid
    to_user = get_object_or_404(User, pk=to_user_id)
    new_bunk = Bunk(to_user=to_user, from_user=from_user)
    new_bunk.save()

    return HttpResponseRedirect(reverse('bunk:user_feed', args=(to_user.id,)))
