from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView, UpdateView, DeleteView
from django.shortcuts import redirect
from . import models
from . import forms
from django.urls import reverse, reverse_lazy

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'
    
@login_required  
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


class HomeTimesheetView(LoginRequiredMixin, ListView):
    context_object_name = 'timesheets'
    model = models.HomeTimesheet
    template_name = 'basic_app/timesheet.html'
    
    def get_queryset(self):
        return models.HomeTimesheet.objects.filter(user=self.request.user)
    
    def post(self, request, *args, **kwargs):
        if 'action' in request.POST:
            action = request.POST['action']
            
            if action == 'chore_submit':
                form = forms.HomeTimesheetForm(request.POST)
                if form.is_valid():
                    # Set the current user before saving the form
                    timesheet = form.save(commit=False)
                    timesheet.user = request.user  # Set the user attribute
                    timesheet.save()
                    return redirect(reverse('basic_app:timesheet'))
                
                
            elif action == 'submit_salary':
                # Calculate the total salary only when the 'submit' button is pressed
                timesheets = self.get_queryset()
                total_sum = sum(timesheet.calculate_salary() for timesheet in timesheets)
                
                return render(request, self.template_name, {'timesheets': timesheets, 'total_sum': total_sum})
                
                
                
            elif action == 'update':
                # Handle update action here if needed
                pass
        
        # Redirect to the timesheet page
        return redirect(reverse('basic_app:timesheet'))
            
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = forms.HomeTimesheetForm()  # Instantiate your form
    
        # Filter timesheets by the current logged-in user
        timesheets = models.HomeTimesheet.objects.filter(user=self.request.user)
    
        # Calculate the total sum of salaries for the filtered timesheets
        total_sum = sum(timesheet.calculate_salary() for timesheet in timesheets)
    
        context['total_sum'] = total_sum
        
        
        # Getting words for timesheet entry
        words = []
        for timesheet in timesheets:
            words.extend(timesheet.chore_name.split())
            
        context['words'] = words
        
        return context
      
      
class HomeTimesheetDetailView(DetailView):
    context_object_name = 'hometimesheet_detail'
    model = models.HomeTimesheet
    template_name = 'basic_app/timesheet_detail.html'
    
            
class HomeTimesheetUpdate(UpdateView):
    fields = ('chore_name', 'day')
    model = models.HomeTimesheet
  
  
class HomeTimesheetDeleteView(DeleteView):
    model = models.HomeTimesheet
    success_url = reverse_lazy('basic_app:timesheet')


def register(request):
    
    registered = False
    
    if request.method == 'POST':
        user_form = forms.UserForm(data=request.POST) 
        profile_form = forms.UserProfileInfoForm(data=request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            
            profile.save()
            
            registered = True
            
        else:
            print(user_form.errors, profile_form.errors)
            
    else:
        user_form = forms.UserForm()
        profile_form = forms.UserProfileInfoForm()
        
    return render(request, 'basic_app/registration.html', 
                  {'user_form': user_form,
                   'profile_form':profile_form,
                   'registered':registered})
          
def user_login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            
            else:
                return HttpResponse('Account not active')
    
        else:
            print('Someone tried to login and failed')
            print('Username:', username, 'Password:', password)
            return HttpResponse('Invalid login details supplied')
        
        
    else:
        return render(request, 'basic_app/login.html')
    

#def post(self, request, *args, **kwargs):
#        form = forms.HomeTimesheetForm(request.POST)
#        if form.is_valid():
#            # Custom form validation logic
#            # Save form data to the model
#            form.save()
#            return redirect(reverse('basic_app:timesheet'))
 #       
  #      else:
   #         return self.get(request, *args, **kwargs)
   
# reset timesheet
def reset_timesheets(request):
    models.HomeTimesheet.objects.all().delete()
    return redirect('basic_app:timesheet')