from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
scheduler = BackgroundScheduler()
inner_scheduler = BackgroundScheduler()
#page_number = 0
def start_scheduler(func_Scheduler, time):
    try:
        scheduler.start()
        scheduler.add_job(func_Scheduler, trigger=CronTrigger(second=f'*/{time}'))
    except Exception as e:
        print ('Exception from scheduler cron', str(e) )
def start_scheduler_nested(func_Scheduler, time):
    inner_scheduler.start()
    
    inner_scheduler.add_job(func_Scheduler, trigger=CronTrigger(second=f'*/{time}'))
    