from app import app
import jobs
jobs.get_tle_from_providers.run()
app.run()
