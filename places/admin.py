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
        return format_html('<img src="{url}" width="{width}" height={height} />',
                           url=obj.image.url,
                           width=(200 / obj.image.height) * obj.image.width,
                           height=200,
                           )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    # fields = ('image', 'number')
    pass
