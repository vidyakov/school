from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import SchoolUserCreationForm
from .models import SchoolUser


class SchoolUserCreateView(FormView):
    model = SchoolUser
    form_class = SchoolUserCreationForm
    success_url = reverse_lazy('main:index')
    template_name = 'authapp/schooluser_form.html'

