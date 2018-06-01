from django.contrib import admin
from .models import MemInfo, MemMchInfo, PreDistAnalysis, AfterDistAnalysis, WantnessAnalysis, MchResult

admin.site.register(MemInfo)
admin.site.register(MemMchInfo)
admin.site.register(PreDistAnalysis)
admin.site.register(AfterDistAnalysis)
admin.site.register(WantnessAnalysis)
admin.site.register(MchResult)

