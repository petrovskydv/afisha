from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from django.contrib import admin
from django.utils.html import format_html

from places.models import Place, Image


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    extra = 1
    readonly_fields = ('image_preview',)
    fields = ('number', 'image', 'image_preview',)

    def image_preview(self, obj):
        return format_html('<img src="{url}" height={height} />',
                           url=obj.image.url,
                           height=200,
                           )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
    ordering = ['title']
    search_fields = ['title']


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    raw_id_fields = ('place',)
    autocomplete_fields = ['place']
