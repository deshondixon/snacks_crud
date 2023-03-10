from django.views.generic import DetailView, ListView
from .models import Snack


# Create your views here.
class SnackListView(ListView):
    template_name = 'snack_list.html'
    model = Snack


class SnackDetailView(DetailView):
    template_name = 'snack_detail.html'
    model = Snack
