from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User
from datetime import datetime as dt

class SiteInformation(models.Model):
	# Site Information Fields
	site_name = models.CharField(max_length=100)
	company_name = models.CharField(max_length=100)
	site_description = models.TextField(blank=True, null=True)
	site_keywords = models.CharField(max_length=200, blank=True, null=True)
	tagline = models.CharField(max_length=256, blank=True, null=True)
	logo = models.ImageField(upload_to='uploads/')

	# Contact Information Fields
	address = models.TextField(blank=True, null=True)
	telephone = models.CharField(blank=True, null=True, max_length=20)
	mobile = models.CharField(blank=True, null=True, max_length=20)
	fax = models.CharField(blank=True, null=True, max_length=20)
	email = models.EmailField(blank=True, null=True)
	website = models.URLField(blank=True, null=True)
	sales_email = models.EmailField(blank=True, null=True)
	technical_email = models.EmailField(blank=True, null=True)
	accounts_email = models.EmailField(blank=True, null=True)

	# Social Media URLs
	facebook_url = models.URLField(blank=True, null=True)
	twitter_url = models.URLField(blank=True, null=True)
	instagram_url = models.URLField(blank=True, null=True)
	linkedin_url = models.URLField(blank=True, null=True)
	whatsapp_url = models.URLField(blank=True, null=True)
	googlemap_url = models.URLField(blank=True, null=True)

	# Additional Site Information Fields (You can add more as needed)
	about_us = models.TextField(blank=True, null=True)
	privacy_policy = models.TextField(blank=True, null=True)
	terms_of_service = models.TextField(blank=True, null=True)

	def __str__(self):
		return str(self.site_name)


class Marketing(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True, null=True)
	image = models.ImageField(upload_to='uploads/')
	action = models.CharField(max_length=25, blank=True, null=True)
	action_url = models.URLField(blank=True, null=True)
	
	def __str__(self):
		return str(self.name)


class Service(models.Model):
	name = models.CharField(max_length=256)
	discriptions = models.TextField()
	image = models.ImageField(upload_to='service/', blank=True, null=True)
	icon = models.CharField(max_length=100, blank=True, null=True)

	def __str__(self) -> str:
		return self.name

class Feature(models.Model):
	name = models.CharField(max_length=256)
	discriptions = models.TextField()
	image = models.ImageField(upload_to='feature/', blank=True, null=True)
	icon = models.CharField(max_length=100, blank=True, null=True)

	def __str__(self) -> str:
		return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category-detail', args=[str(self.slug)])


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category, related_name='posts')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']


class ProductCategory(models.Model):
	name = models.CharField(max_length=100)
	description_short = models.CharField(max_length=255, blank=True, null=True)
	description = models.TextField(blank=True, null=True)
	image = models.ImageField(upload_to='products/', blank=True, null=True)
	# slug = models.SlugField(unique=True)

	def __str__(self):
		return str(self.name)


class Product(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True, null=True)
	category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.name)


class Project(models.Model):
	# category = models.ManyToManyField(Category)
	category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
	name = models.CharField(max_length=256)
	client = models.CharField(max_length=256)
	discriptions = models.TextField()
	file = models.FileField()
	image = models.ImageField(upload_to='uploads/')
	icon = models.CharField(max_length=100, blank=True, null=True)
	is_published = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self) -> str:
		return self.name




class TeamMember(models.Model):
	# Personal Information
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	job_title = models.CharField(max_length=100)
	email = models.EmailField()
	phone_number = models.CharField(max_length=20, blank=True, null=True)
	bio = models.TextField(blank=True, null=True)

	# Social Media Profiles (optional)
	linkedin_url = models.URLField(blank=True, null=True)
	twitter_url = models.URLField(blank=True, null=True)
	facebook_url = models.URLField(blank=True, null=True)
	instagram_url = models.URLField(blank=True, null=True)

	# Profile Image (optional)
	profile_image = models.ImageField(upload_to='team/', blank=True, null=True)

	def __str__(self):
		return f"{self.first_name} {self.last_name} - {self.job_title}"
	

class Testimonial(models.Model):
	name = models.CharField(max_length=100)
	company = models.CharField(max_length=100, blank=True, null=True)
	content = models.TextField()

	def __str__(self):
		return self.name


class Contact(models.Model):
	name = models.CharField(max_length=250)
	email = models.EmailField()
	phone = models.CharField(max_length=30)
	subject = models.CharField(max_length=250)
	message = models.TextField()
	action = models.BooleanField(default=False)
	submission_date = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.email




