# -*- coding: utf-8 -*-
import xadmin
from .models import Frank, EmailVR
from xadmin import views

class BaseSetting(object):
	enable_themes = True
	use_bootswatch = True
xadmin.site.register(views.BaseAdminView, BaseSetting)

class GlobalSettings(object):
	site_title = "Frank Studio"
	site_footer = "Frank Studio"
	menu_style = "accordion"
xadmin.site.register(views.CommAdminView, GlobalSettings)

class FrankAdmin(object):
    pass
xadmin.site.register(Frank, FrankAdmin)

class EmailVRAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
xadmin.site.register(EmailVR, EmailVRAdmin)
