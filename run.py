from app import app
import jobs
jobs.gettlefromproviders.run()
app.run(debug = False)
