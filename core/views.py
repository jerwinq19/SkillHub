from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views import generic
from . import forms
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Service, Transaction
from django.db.models import Count, Sum, Avg


class RegisterView(generic.FormView):
    form_class = forms.RegisterForm
    template_name = 'core/register.html'
    success_url = '/'
    
    def form_valid(self, form):
        try:
            data = form.cleaned_data

            User.objects.create_user(
                username=data['username'],
                password=data['password'],
                first_name=data['first_name'].title(),
                last_name=data['last_name'].title(),
            )
            print("register successfully.")
        except Exception as e:
            print(e)
        return super().form_valid(form)
    

class HomeView(LoginRequiredMixin,generic.TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['services_data'] = Service.objects.all()
        
        return context
    

class AddServiceView(LoginRequiredMixin, generic.CreateView):
    template_name = 'core/add_service.html'
    model = Service
    form_class = forms.ServiceForm
    
    def form_valid(self, form):
        form.instance.provider = self.request.user # the provider foreignkey
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.request.user.pk })

class UserProfileView(LoginRequiredMixin, generic.DetailView):
    template_name = 'core/profile.html'
    model = User
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        
        context['user_data'] = self.request.user
        context['your_services'] = Service.objects.filter(provider=self.request.user.pk)
        context['booked_services'] = Transaction.objects.filter(booking_owner=self.request.user.pk)
        
        return context

class ServiceDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'core/service_detail_view.html'
    model = Service
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['detail_service_data'] = Service.objects.filter(pk=self.kwargs['pk'], slug=self.kwargs['slug'])
        
        print("this run")
        return context

class DeleteServie(LoginRequiredMixin, generic.DeleteView):
    model = Service
    template_name = 'core/confirm_delete.html'

    
    # debug
    print("Delete run")
    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.request.user.pk })
    

class UpdateServiceView(LoginRequiredMixin, generic.UpdateView):
    model = Service
    form_class = forms.ServiceForm
    template_name = 'core/update_service.html'
    
    # debug
    print("update run")
    
    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.request.user.pk })
    

class BookServiceView(LoginRequiredMixin, generic.CreateView):
    model = Transaction
    template_name = 'core/booking_confirmation.html'
    fields = ['booking_status']
            
    def form_valid(self, form):
        form.instance.booking_owner = self.request.user
        serivice_instance = get_object_or_404(Service, pk=self.kwargs['pk'])
        form.instance.service = serivice_instance
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.request.user.id })
    

class ManageServiceView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'core/manage_services.html'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['total_booking'] = Transaction.objects.exclude(booking_owner=self.request.user).count()
        context['who_avail'] = Transaction.objects.exclude(booking_owner=self.request.user)
        context['total_money'] = Transaction.objects.exclude(booking_owner=self.request.user).aggregate(total=Sum('service__price'))
        
        return context


class View404(generic.TemplateView):
    template_name = '404.html'