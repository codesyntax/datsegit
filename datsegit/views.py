from django.views.generic import ListView, DetailView
from twhst.models import Status, Hashtag, Dictionary

class StatusFilteredList(ListView):
    def get_context_data(self, **kwargs):
        context = super(StatusFilteredList, self).get_context_data(**kwargs)
        context['object'] = Hashtag.objects.get(name=self.kwargs.get('slug'))
        context['dictionary'] = Dictionary.objects.filter(slug__startswith=self.kwargs.get('letter'), hashtag=context['object']).order_by('title')
        return context
    
    def get_queryset(self):
        self.hashtag = Hashtag.objects.get(name=self.kwargs.get('slug'))
        self.filter = self.kwargs.get('letter')
        return Status.objects.filter(hashtag=self.hashtag, text__istartswith=self.filter).order_by('text')[:3]

class HashtagDetailView(DetailView):
    model=Hashtag
    def get_context_data(self, **kwargs):
        context = super(HashtagDetailView, self).get_context_data(**kwargs)
        hashtag = Hashtag.objects.get(name=self.kwargs.get('slug'))        
        context['dictionary'] = Dictionary.objects.filter(hashtag=hashtag).order_by('-added')[:30]
        return context

class DictionaryListView(ListView):
    model = Dictionary
    def get_context_data(self, **kwargs):
        context = super(DictionaryListView, self).get_context_data(**kwargs)
        context['word'] = self.kwargs.get('word')
        context['object'] = Hashtag.objects.get(name=self.kwargs.get('slug'))        
        return context
    
    def get_queryset(self):
        hashtag = Hashtag.objects.get(name=self.kwargs.get('slug'))
        word = self.kwargs.get('word')
        return Dictionary.objects.filter(slug=word, hashtag=hashtag).order_by('title')
    
