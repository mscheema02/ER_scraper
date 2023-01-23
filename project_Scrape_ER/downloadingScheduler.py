from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler()

@scheduler.scheduled_job('interval', hours=1)
def download_job():
    downloader.download()

scheduler.start()
