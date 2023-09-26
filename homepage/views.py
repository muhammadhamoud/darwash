from django.http import Http404
from django.shortcuts import render
from datetime import datetime as dt
from .models import *
# Create your views here.

def index(request):
    # info = SiteInformation.objects.all()
    # if len(info) != 1:
    #     raise Http404('Information for this site is not posted.')
    # info = info[0]
    
    services = Service.objects.all()
    projects = Project.objects.filter(is_published=True).order_by('-updated_at')
    features = Feature.objects.all()
    products = Product.objects.all()
    marketings = Marketing.objects.all()
    teammembers = TeamMember.objects.all()
    testimonials = Testimonial.objects.all()

    context = {
        # 'site_information': info,
        'services': services,
        'projects': projects,
        'features': features,
        'products': products,
        'marketings': marketings,
        'teammembers': teammembers,
        'testimonials': testimonials,
        'copyright': f'2000-{dt.now().year}',	
    }
    return render(request, 'main.html', context)



from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Category, Post


# def blog(request):
#     categories = Category.objects.all()
#     posts = Post.objects.all()

#     context = {
#         'categories': categories,
#         'posts': posts,
#     }
#     return render(request, 'blog/blogs.html', context)



# class PostListView(ListView):
#     model = Post
#     template_name = 'blog/post_list.html'  # Create this template
#     context_object_name = 'posts'
#     ordering = ['-created_at']
#     paginate_by = 10  # Adjust as needed


# class PostDetailView(DetailView):
#     model = Post
#     template_name = 'blog/post_detail.html'  # Create this template
#     context_object_name = 'post'


# class CategoryListView(ListView):
#     model = Category
#     template_name = 'blog/category_list.html'  # Create this template
#     context_object_name = 'categories'


# class CategoryDetailView(ListView):
#     template_name = 'blog/category_detail.html'  # Create this template
#     context_object_name = 'category_posts'
#     paginate_by = 10  # Adjust as needed

#     def get_queryset(self):
#         category = Category.objects.get(slug=self.kwargs['slug'])
#         return Post.objects.filter(categories=category).order_by('-created_at')


# def bootstrap(request):
# 	context = {
# 	}
# 	return render(request, 'bootstrap.html', context)


from django.shortcuts import render, redirect
from .forms import ContactForm
from .send_emails import EmailTemplates, EmailSender

def contact_view(request):


    if request.method == 'POST':
        form = ContactForm(request.POST)
      
        if form.is_valid():
            form.save()
            # You can add code here to send an email notification if needed

            email_body_html = EmailTemplates.email_confirmation(form.cleaned_data['name'])
            
            email = form.cleaned_data['email']
            email_subject = form.cleaned_data['subject']
            # email_body_html = form.cleaned_data['message']

            data = {'email': email, 'body': email_body_html, 'subject': email_subject}
            
            EmailSender.send_email(data)

            return redirect('contact_success')  # Redirect to a success page
        
        else:
            print('Form is not valid:', form.errors)

    else:
        form = ContactForm()
        print('GET request received')

    
    return render(request, 'contact.html', {'form': form})

def contact_success(request):
    return render(request, 'contact_success.html')


