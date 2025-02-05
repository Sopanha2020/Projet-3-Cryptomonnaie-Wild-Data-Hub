from django.contrib import admin
from django import forms
from crypto.models import Crypto, CryptoData, CryptoPurchases, Alert

# Admin form for Crypto model to use a radio select for 'signal' field
class CryptoAdminForm(forms.ModelForm):
    class Meta:
        model = Crypto
        fields = '__all__'
        widgets = {
            'signal': forms.RadioSelect(),
        }

@admin.register(Crypto)  # Ensure that Crypto is only registered once
class CryptoAdmin(admin.ModelAdmin):
    form = CryptoAdminForm
    list_display = ('symbol', 'display_name', 'signal', 'updated', 'enabled')
    list_filter = ('signal', 'enabled', 'updated')
    search_fields = ('symbol', 'display_name')
    ordering = ('symbol',)  # Ensures the order of display in Django Admin

    fieldsets = (
        (None, {
            'fields': ('symbol', 'display_name', 'image', 'enabled', 'order')
        }),
        ('Trading Signals', {
            'fields': ('signal', 'signal_description'),
            'classes': ('wide',)
        }),
        ('Display Options', {
            'fields': ('show_overall', 'show_chart'),
        }),
    )

    class Media:
        css = {
            'all': ('admin/css/crypto_admin.css',)  # Custom CSS for admin panel
        }

@admin.register(CryptoData)
class CryptoDataAdmin(admin.ModelAdmin):
    list_display = ('crypto', 'price', 'percent', 'timestamp')
    ordering = ('-timestamp', 'crypto')
    readonly_fields = ('timestamp',)
    search_fields = ('crypto__symbol', 'crypto__display_name')

@admin.register(CryptoPurchases)
class CryptoPurchasesAdmin(admin.ModelAdmin):
    list_display = ('crypto', 'amount', 'buy_price', 'total_price', 'bought_at')
    ordering = ('-bought_at',)
    search_fields = ('crypto__symbol', 'crypto__display_name')

@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ('crypto', 'price', 'is_above', 'active', 'send_discord', 'last_triggered')
    list_filter = ('active', 'send_discord', 'crypto', 'timestamp')
    search_fields = ('crypto__symbol', 'crypto__display_name')
    fieldsets = (
        (None, {
            'fields': ('crypto', 'price', 'is_above')
        }),
        ('Notification Settings', {
            'fields': ('send_discord', 'active'),
        }),
    )
