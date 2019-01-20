from django.contrib import admin
from .models import AmbassadorInfo


class StatusListFilter(admin.SimpleListFilter):
    """
    user choice or by a default value.
    """
    title = 'Application Status'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'status'

    default_value = None

    def lookups(self, request, model_admin):
        """
        """
        list_of_amb = []
        queryset = AmbassadorInfo.objects.all()
        for amb in queryset:
            list_of_amb.append(
                (str(amb.status).capitalize(), amb.status)
            )
        return sorted(list_of_amb, key=lambda tp: tp[1])

    def queryset(self, request, queryset):
        """
        """
        if self.value():
            return queryset.filter(status=self.value())
        return queryset

    def value(self):
        """
        """
        return str('on_hold')


class AmbassadorInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_number', 'status',)
    list_filter = (StatusListFilter,)

admin.site.register(AmbassadorInfo, AmbassadorInfoAdmin)