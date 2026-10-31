import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler

def test_job():
    print("Test job executed")

async def start_scheduler():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(test_job, 'interval', seconds=60)
    scheduler.start()
    print("Scheduler started. Waiting for jobs...")
    while True:
        await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(start_scheduler())
