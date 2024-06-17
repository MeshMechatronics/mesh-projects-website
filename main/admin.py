from django.contrib import admin
from .models import User, Material, Company, Project, Quote

admin.site.register(User)
admin.site.register(Material)
admin.site.register(Company)
admin.site.register(Project)
admin.site.register(Quote)