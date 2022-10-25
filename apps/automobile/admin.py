from django.contrib import admin
from embed_video.admin import AdminVideoMixin
# automobile app
from apps.automobile.models.car import Car
from apps.automobile.models.position_category import PositionCategory
from apps.automobile.models.gifts import Gifts
from apps.automobile.models.company import CarCompany

# calculator app
from apps.calculator.models.cridet import Cridet
from apps.calculator.models.payment import Payment

# company app
from apps.company.model.about import AboutCompany, Filials
from apps.company.model.address import Address

# siteconfig
from apps.siteconfig.model.banner import Banner
from apps.siteconfig.model.menubar import MenuBar

# blog app
from apps.blog.model.news import News
from apps.blog.model.comments import Comment

# user app
from apps.users.models.customer import Customer
from apps.users.models.user import User

# Register your models here.
# automobile
admin.site.register(CarCompany)
admin.site.register(Car)
admin.site.register(PositionCategory)
admin.site.register(Gifts)

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
