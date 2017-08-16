from django.views.generic import DetailView

from myapp.models import MyModel


class MyView(DetailView):
    model = MyModel
