from django.shortcuts import render, get_object_or_404

# Create your views here.
def profile(request):
    """ Display the user's profile. """
    # profile = get_object_or_404(UserProfile, user=request.user)
    
    # orders = profile.orders.all()

    template = 'profiles/profile.html'

    # context = {
    #     'orders': orders,
    # }

    return render(request, template)