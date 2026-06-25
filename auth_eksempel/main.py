import uvicorn
from auth_rest_api import Auth_rest_api

api = Auth_rest_api()
app = api.app

# Vi har fjernet "." fra importen, 
# fordi filerne nu ligger lige ved siden af hinanden!


# Kør i terminal/console med: 
# uvicorn .main:app --reload
#
# Kør i browser:
# http://127.0.0.1:8000/ 
#
# Documentation: 
# http://127.0.0.1:8000/docs