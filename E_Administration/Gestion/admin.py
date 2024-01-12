from django.contrib import admin

from Gestion.models import ActeCivil
from Gestion.models import ActeMariage
from Gestion.models import ActeDeces
from Gestion.models import Bureau
from Gestion.models import Officier
from Gestion.models import Registre

admin.site.register(ActeCivil)
admin.site.register(ActeMariage)
admin.site.register(ActeDeces)
admin.site.register(Bureau)
admin.site.register(Officier)
admin.site.register(Registre)
