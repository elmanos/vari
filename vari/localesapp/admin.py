# -*- encoding: utf-8 -*-
from django.contrib import admin
from models import Owner, Group, Premise, Gallery, Setting, Room, Material, ExcludedDays


# @admin.register(Owner, Group, Premise, Gallery, Setting, Room, Material, ExcludedDays)

#####################
#    OWNER          #
#####################
class OwnerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Owner, OwnerAdmin)


#####################
#    GROUP          #
#####################
class GroupAdmin(admin.ModelAdmin):
    pass
admin.site.register(Group, GroupAdmin)


#####################
#    PREMISE        #
#####################
class PremiseAdmin(admin.ModelAdmin):
    pass
admin.site.register(Premise, PremiseAdmin)


#####################
#    GALLERY        #
#####################
class GalleryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Gallery, GalleryAdmin)


#####################
#    SETTING        #
#####################
class SettingAdmin(admin.ModelAdmin):
    pass
admin.site.register(Setting, SettingAdmin)


#####################
#    ROOM           #
#####################
class RoomAdmin(admin.ModelAdmin):
    pass
admin.site.register(Room, RoomAdmin)


#####################
#    MATERIAL       #
#####################
class MaterialAdmin(admin.ModelAdmin):
    pass
admin.site.register(Material, MaterialAdmin)


#####################
#    EXCLUDED_DAYS  #
#####################
class ExcludedDaysAdmin(admin.ModelAdmin):
    pass
admin.site.register(ExcludedDays, ExcludedDaysAdmin)


