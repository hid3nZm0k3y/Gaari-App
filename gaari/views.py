from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from .forms import AutosForm, MakeForm, ReviewForm, MessageForm
from .models import Autos, Make, Review, Message

# Create your views here.

def index(request):
    return render(request, "gaari/index.html")

def thank_you(request):
    return render(request, "gaari/thank-you.html")

def view_favorite(request):

    favorites = request.session.get("stored_autos")
    autos = Autos.objects.all()
    return render(request, "gaari/favorite.html", {
        "favorites": favorites,
        "autos": autos
    })

def view_inbox(request):

    if(request.method == "GET"):
        user = request.user.username
        messages = Message.objects.filter(receiver=user)
        form = MessageForm()

        return render(request, "gaari/inbox.html", {
            "messages": messages,
            "user": user,
            "form": form
        })

    if(request.method == "POST"):
        form = MessageForm(request.POST)
        
        if(form.is_valid()):
            form.save()
            msg = form.save(commit=False)
            msg.user = request.user.username
            msg.save()
            return HttpResponseRedirect("/inbox")
        
        else:

            form = MessageForm()

            return render(request, "gaari/inbox.html", {
            "messages": messages,
            "user": user,
            "form": form
        })

def message_delete(request, pk):
    if(request.method == "GET"):
        message = Message.objects.get(id=pk)
        message.delete()
        return HttpResponseRedirect("/inbox")


# Automobile Logic

class AutosListView(LoginRequiredMixin, generic.ListView):
    model = Autos
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs["pk"]
        auto= Autos.objects.get(pk=id)
        user = self.request.user.username
        reviews = Review.objects.all()
        context["auto"] = auto
        context["reviews"] = reviews
        context["user"] = user,
        context["favorites"] = self.request.session.get("stored_autos")

        return context

class AutosCreateView(LoginRequiredMixin, CreateView):

    model = Autos
    form_class = AutosForm
    template_name = "gaari/autos.html"
    success_url = "/autos"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        autos_list = Autos.objects.all()
        search = self.request.GET.get("search", False)
        if(search):
            query = Q(nickname__contains=search)
            autos_list = Autos.objects.filter(query)

        context["autos_list"] = autos_list
        return context


class AutosUpdateView(LoginRequiredMixin, UpdateView):
    model = Autos
    fields = '__all__'
    success_url = reverse_lazy('gaari:autos')

class AutosDeleteView(LoginRequiredMixin, DeleteView):
    model = Autos
    fields = '__all__'
    success_url = reverse_lazy('gaari:autos')




# Reviews Logic
class ReviewCreateView(LoginRequiredMixin, CreateView):

    model = Review
    form_class = ReviewForm
    template_name = "gaari/review.html"

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('gaari:autos_list', args=[self.kwargs['pk']])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["id"] = self.kwargs["pk"]
        return context

    def form_valid(self, form, **kwargs):
        object = form.save(commit = False)
        object.username = self.request.user.username
        object.auto = Autos.objects.get(pk=self.kwargs["pk"])
        object.save()
        return super(ReviewCreateView, self).form_valid(form)

def ReviewDelete(request, pk, review_pk):
    if(request.method == "GET"):
        review = Review.objects.get(id=review_pk)
        review.delete()
        return HttpResponseRedirect("/autos")
    
# Favorite Logic
def favorite(request, pk):
    stored_autos = request.session.get("stored_autos")
    if(stored_autos is None or len(stored_autos) == 0):
        stored_autos = []

    favorite_id = int(pk)
    if(favorite_id in stored_autos):
        stored_autos.remove(favorite_id)
    
    else:
        stored_autos.append(favorite_id)

    request.session["stored_autos"] = stored_autos

    return HttpResponseRedirect("/autos")

# Brands Logic

class MakeCreateView(LoginRequiredMixin, CreateView):
    model = Make
    form_class = MakeForm
    template_name = "gaari/make.html"
    success_url = "/make"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        make_list = Make.objects.all()

        search = self.request.GET.get("search", False)
        if(search):
            query = Q(name__contains=search)
            make_list = Make.objects.filter(query)

        context["make_list"] = make_list
        return context
    

class MakeUpdateView(LoginRequiredMixin, UpdateView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('gaari:make')


class MakeDeleteView(LoginRequiredMixin, DeleteView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('gaari:make')


