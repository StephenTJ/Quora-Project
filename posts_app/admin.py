from django.contrib import admin
from .models import Question_Table,Answer_Table,Like_Table

admin.site.register(Question_Table)

admin.site.register(Answer_Table)

admin.site.register(Like_Table)
# Register your models here.
