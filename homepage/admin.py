from django.contrib import admin
# Register your models here.
from .models import *

class Projectdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published')  # Include 'is_published' in the list of displayed fields


# admin.site.register(Category)
# admin.site.register(Post)

admin.site.register(SiteInformation)
admin.site.register(Service)
admin.site.register(Project, Projectdmin)
# admin.site.register(Project)
admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Marketing)
admin.site.register(TeamMember)
admin.site.register(Testimonial)
admin.site.register(Feature)

admin.site.register(Contact)