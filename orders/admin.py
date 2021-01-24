from django.contrib import admin
from .models import Order,Order_Detail

# Register your models here.

admin.site.register(Order)


class OrderdetailAdmin(admin.ModelAdmin):
    list_display = ('id','item_name','email','firstname','phone','city','message','status')
    search_fields=('item_name','email','firstname','city','phone','status')


admin.site.register(Order_Detail,OrderdetailAdmin)

