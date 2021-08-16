# store sensor data
sensor_list = []
# get the ID of the last sensor
def get_last_id():
    if sensor_list:
        last_sensor = sensor_list[-1]
    else:
        return 1
    return last_sensor.id + 1

# define the sensor class
class Sensor:
    # the __init constructor methode with the parameters
    def __init__(self, name, description, temperature, humidity, location):
        self.id = get_last_id()
        self.name = name
        self.description = description
        self.temperature = temperature
        self.humidity = humidity
        self.location = location
        self.is_publish = False # do not publish

        # data method for returning the data as a dictionary object
    @property
    def data(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'temperature': self.temperature,
            'humidity': self.humidity,
            'location': self.location
        }

# next we build the API nedpoint