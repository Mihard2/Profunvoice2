from django.contrib import admin
from blog.models import (Slider, 
                         LonggridTag, 
                         Longgrid,
                         NBATag,
                         NBA
                        )

# Register your models here.

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'public')

class PostPage(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}    
    list_display = ('title', 'public', 'date_pub')
    filter_horizontal = ['tags']
    fields = (('title', 'slug'),'public','date_pub','image','short_description','description','tags')

class TagModel(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}
    display = ('name')

@admin.register(Longgrid)
class LonggridAdmin(PostPage):
    pass
    
@admin.register(LonggridTag)
class LonggridTag(TagModel):
    pass

@admin.register(NBA)
class NBAAdmin(PostPage):
    pass

@admin.register(NBATag)
class NBATag(TagModel):
    pass

