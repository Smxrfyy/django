from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Review

# Create your views here.
def home(request):
    return render(request, 'itreporting/home.html', {'title': 'Welcome Page'})

def about(request):
    return render(request, 'itreporting/about.html', {'title': 'About Us'})

def report(request):
    daily_report = {
        'reviews': Review.objects.all(),
        'title': 'Daily Reports'
    }

    return render(request, 'itreporting/products.html', daily_report)

def contact(request):
    return render(request, 'itreporting/contact.html', {'title': 'Contact Us'})

class PostListView(ListView):
    model = Review
    template_name = 'itreporting/products.html'
    context_object_name = 'reviews'
    ordering = ['-date_submitted']
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context.update({'title': 'List of Reviews'})
        return context

class PostDetailView(DetailView):
    model = Review

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ['type', 'room', 'details']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    fields = ['type', 'room', 'details']

    def test_func(self):
        review = self.get_object()
        return self.request.user == review.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    success_url = '/products'

    def test_func(self):
        review = self.get_object()
        return self.request.user == review.author

class UserPostListView(ListView):
    model = Review
    template_name = 'itreporting/user_review.html'
    context_object_name = 'reviews'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User,
        username = self.kwargs.get('username'))
        return Review.objects.filter(author = user).order_by('-date_submitted')

