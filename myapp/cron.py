from datetime import date
from django_cron import CronJobBase, Schedule

from myapp.models import PackageOrder

class UpdateFieldCronJob(CronJobBase):
    RUN_EVERY_MIDNIGHT = Schedule(run_at_times=['21:19'])

    def do(self):
        print("cron job done")
        if date.today() > date(2022, 1, 1):
            
            PackageOrder.objects.update(status='Expired')
