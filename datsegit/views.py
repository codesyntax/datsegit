from django.views.generic import ListView
from twhst.models import Status, Hashtag

class StatusFilteredList(ListView):
    def get_context_data(self, **kwargs):
        context = super(StatusFilteredList, self).get_context_data(**kwargs)
        context['object'] = Hashtag.objects.get(name=self.kwargs.get('slug'))
        return context
    
    def get_queryset(self):
        self.hashtag = Hashtag.objects.get(name=self.kwargs.get('slug'))
        self.filter = self.kwargs.get('letter')
        return Status.objects.filter(hashtag=self.hashtag, text__istartswith=self.filter)
