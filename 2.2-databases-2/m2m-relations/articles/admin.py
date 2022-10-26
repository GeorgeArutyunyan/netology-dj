from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tag, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        counter = 0
        for form in self.forms:
            if 'is_main' in form.cleaned_data:
                counter += 1
        if counter == 0:
            raise ValidationError('Отсутсвует тег основного раздела')
        elif counter >= 2:
            raise ValidationError('Может быть только один основной тег')

        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]


@admin.register(Tag)
class Tag(admin.ModelAdmin):
    pass
