from django.contrib import admin

# Register your models here.
from .models import Question,Choice

# 你需要遵循以下流程——创建一个模型后台类，
# # 接着将其作为第二个参数传给 admin.site.register() ——在你需要修改模型的后台管理选项时这么做。
# 说到拥有数十个字段的表单，你可能更期望将表单分为几个字段集：
# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ("Question information",               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date']}),
#     ]
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
