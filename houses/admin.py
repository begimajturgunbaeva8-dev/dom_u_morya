from django.contrib import admin
from houses.models import House


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ["name", "price"]
    list_display_links = ["name"]

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["photo"].label = "Фотография дома"
        return form
