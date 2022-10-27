from django.contrib import admin
from embed_video.admin import AdminVideoMixin
# automobile app
from apps.automobile.models import CarCompany, Usedcars, Gifts, PositionCategory, Car, CarLikes

# calculator app
from apps.calculator.models import Payment, Cridet

# company app
from apps.company.model import AboutCompany, Filials, Address

# siteconfig
from apps.siteconfig.model import Banner, MenuBar

# blog app
from apps.blog.model import News, Comment

# user app
from apps.users.models import Customer, User

# Register your models here.
# automobile
admin.site.register(CarCompany)
admin.site.register(Car)
admin.site.register(PositionCategory)
admin.site.register(Gifts)
admin.site.register(Usedcars)
admin.site.register(CarLikes)

# calculator
admin.site.register(Cridet)
admin.site.register(Payment)

# company
admin.site.register(AboutCompany)
admin.site.register(Address)
admin.site.register(Filials)

# siteconfig
admin.site.register(Banner)
admin.site.register(MenuBar)


# blog
class AdminVideo(AdminVideoMixin, admin.ModelAdmin):
    pass


admin.site.register(News)
admin.site.register(Comment, AdminVideo)

# user
admin.site.register(Customer)
admin.site.register(User)
