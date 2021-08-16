# mport the necessary classes
from flask import Flask
from flask_restful import Api
from resources.sensor import SensorListResource, SensorResource, SensorPublishResource

# Set up Flask and initialize flask_restful.API with our Flask app
app = Flask(__name__)
api = Api(app)

# Add resource routing by passing in the URL 
# so that it will route to our resources.
api.add_resource(SensorListResource, '/sensors')
api.add_resource(SensorResource, '/sensors/<int:sensor_id>')
api.add_resource(SensorPublishResource, '/sensors/<int:sensor_id>/publish')

if __name__ == '__main__':
    app.run(port=5001, debug=True)