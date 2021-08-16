from flask import request
from flask_restful import Resource
from http import HTTPStatus
from models.sensor import Sensor, sensor_list

# we will define three subclasses: one for the collection of sensors, 
# one for a single sensor, and one for publishing the sensor. 

# SensorListResource - contains GET and POST methods
class SensorListResource(Resource):
    def get(self):
        data = []
        for sensor in sensor_list:
            if sensor.is_publish is True:
                data.append(sensor.data)
        return {'data': data}, HTTPStatus.OK

# POST method
    def post(self):
        data = request.get_json()
        sensor = Sensor(name=data['name'],
                        description=data['description'],
                        temperature=data['temperature'],
                        humidity=data['humidity'],
                        location=data['location'])
        sensor_list.append(sensor)
        return sensor.data, HTTPStatus.CREATED

# Exercise 8: Defining the Recipe Resource
# the GET method, for getting back a single recipe
class SensorResource(Resource):
    def get(self, sensor_id):
        sensor = next((sensor for sensor in sensor_list if sensor.id == sensor_id and 
                        sensor.is_publish == True), None)
        if sensor is None:
            return {'message': 'sensor not found'}, HTTPStatus.NOT_FOUND
        return sensor.data, HTTPStatus.OK

    # the PUT method, for updating the sensor
    def put(self, sensor_id):
        data = request.get_json()
        sensor = next((sensor for sensor in sensor_list if sensor.id == sensor_id), None)
        if sensor is None:
            return {'message': 'sensor not found'}, HTTPStatus.NOT_FOUND
        sensor.name = data['name']
        sensor.description = data['description']
        sensor.temperature = data['temperature']
        sensor.humidity = data['humidity']
        sensor.location = data['location']
        return sensor.data, HTTPStatus.OK
    
    # delete sensor method
    def delete(self, sensor_id):
        sensor = next((sensor for sensor in sensor_list if sensor.id == sensor_id), None)
        if sensor is None:
            return {'message': 'sensor not found'}, HTTPStatus.NOT_FOUND
        sensor_list.remove(sensor)
        return {}, HTTPStatus.NO_CONTENT

#  sensors should have two Statuses (unpublished and published)
# define the resource for publishing and unpublishing a sensor
class SensorPublishResource(Resource):
    def put(self, sensor_id):
        sensor = next((sensor for sensor in sensor_list if sensor.id == sensor_id), None)
        if sensor is None:
            return {'message': 'sensor not found'}, HTTPStatus.NOT_FOUND
        sensor.is_publish = True
        return {}, HTTPStatus.NO_CONTENT

    # implement the delete method
    def delete(self, sensor_id):
        sensor = next((sensor for sensor in sensor_list if sensor.id == sensor_id), None)
        if sensor is None:
            return {'message': 'sensor not found'}, HTTPStatus.NOT_FOUND
        sensor.is_publish = False # it dosen't delete it - sets if to false
        return {}, HTTPStatus.NO_CONTENT
