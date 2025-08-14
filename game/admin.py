from django.contrib import admin
from .models import Question

# Esta línea le dice a Django que muestre el modelo Question en el panel de administración.
admin.site.register(Question)