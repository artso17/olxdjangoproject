from .forms import PredictForm
from django.views.generic.edit import FormView

class PredictFormView(FormView):
    template_name = 'index.html'
    form_class = PredictForm
    success_url = '/thanks/'



predict_form_view=PredictFormView.as_view()