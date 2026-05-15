from django.shortcuts import render
from .models import Journal, Categorie
from django.db.models import Count, Q
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import JournalForm
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages


@login_required(login_url='login')

def dashboard(request):

    # BASE QUERYSET
    activities = Journal.objects.all().order_by('-datecreation')

   
    search = request.GET.get('search')
    if search:
        activities = activities.filter(titre__icontains=search)

 
    categorie = request.GET.get('categorie')
    if categorie:
        activities = activities.filter(categorie_id=categorie)

  
    statut = request.GET.get('statut')
    if statut:
        activities = activities.filter(statut=statut)

  
    paginator = Paginator(activities, 5)  # 10 lignes par page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'recent_activities': page_obj,
        'page_obj': page_obj,
        'categories': Categorie.objects.all(),

      
        'total_activities': Journal.objects.count(),
        'resolved_activities': Journal.objects.filter(statut='publie').count(),
        'reported_bugs': Journal.objects.filter(statut='brouillon').count(),
        'categories_count': Categorie.objects.count(),
    }

    return render(request, 'dashboard.html', context)

class ConnexionView(LoginView):
    template_name = "registration/login.html"
    success_url = reverse_lazy('dashboard')
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('dashboard')




# Vues pour les journaux
class JournalListView(LoginRequiredMixin, ListView):
    model = Journal
    template_name = 'activities/journal_list.html'
    context_object_name = 'journals'
    paginate_by = 3

    def get_queryset(self):
        queryset = Journal.objects.select_related('auteur', 'categorie').order_by('-datecreation')
        categorie = self.request.GET.get('categorie')
        statut = self.request.GET.get('statut')
        search = self.request.GET.get('search')

        if categorie:
            queryset = queryset.filter(categorie_id=categorie)
        if statut:
            queryset = queryset.filter(statut=statut)
        if search:
            queryset = queryset.filter(Q(titre__icontains=search) | Q(contenu__icontains=search))

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Categorie.objects.all()
        context['statuts'] = Journal.STATUTS
        context['page_title'] = 'Toutes les activités'
        return context


class MyJournalListView(LoginRequiredMixin, ListView):
    model = Journal
    template_name = 'activities/journal_list.html'
    context_object_name = 'journals'
    paginate_by = 3

    def get_queryset(self):
        queryset = Journal.objects.select_related('auteur', 'categorie').filter(auteur=self.request.user).order_by('-datecreation')
        categorie = self.request.GET.get('categorie')
        statut = self.request.GET.get('statut')
        search = self.request.GET.get('search')

        if categorie:
            queryset = queryset.filter(categorie_id=categorie)
        if statut:
            queryset = queryset.filter(statut=statut)
        if search:
            queryset = queryset.filter(Q(titre__icontains=search) | Q(contenu__icontains=search))

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Categorie.objects.all()
        context['statuts'] = Journal.STATUTS
        context['page_title'] = 'Mes activités'
        return context


class JournalDetailView(LoginRequiredMixin, DetailView):
    model = Journal
    template_name = 'activities/journal_detail.html'
    context_object_name = 'journal'


class JournalCreateView(LoginRequiredMixin, CreateView):
    model = Journal
    form_class = JournalForm
    template_name = 'activities/journal_form.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.auteur = self.request.user

        # MESSAGE SUCCESS
        messages.success(
            self.request,
            "Le journal a été créé avec succès !"
        )

        return super().form_valid(form)


class JournalUpdateView(LoginRequiredMixin, UpdateView):
    model = Journal
    form_class = JournalForm
    template_name = 'activities/journal_form.html'
    success_url = reverse_lazy('dashboard')

    
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)   


class JournalDeleteView(LoginRequiredMixin, DeleteView):
    model = Journal
    template_name = 'activities/journal_confirm_delete.html'
    success_url = reverse_lazy('journal_list')

   
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)   



def register_view(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {
        'form': form
    })