import jobs
from app import app

jobs.get_tle_from_providers.run()
app.run(debug=True)
