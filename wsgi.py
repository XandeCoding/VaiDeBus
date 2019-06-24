from app import create_app
import os

app = application = create_app ()

#port = int (os.environ.get ("PORT", 5000))
#app.run (port=port)