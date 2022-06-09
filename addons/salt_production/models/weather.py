from odoo import models, fields, api
from datetime import datetime


class WeatherPost(models.Model):
    _name = 'weather.post'
    _description = 'weather post data'
    _rec_name = 'date'


    date = fields.Date(string="Date", default=fields.Date.context_today)
    time = fields.Datetime(string="Time")
    # check_in_date = Datetime.strptime(string="checkin",  '%Y-%m-%d %H:%M:%S').date()
    # time = datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S")

    tempC = fields.Integer(string="Temprature C")
    humidity = fields.Integer(string="Humidity %")
    windspeed = fields.Integer(string="Windspeed km/h")
    windDirection = fields.Char(string="Wind Direction")
    rainfall = fields.Integer(string="Rain Fall (mm)")
    beaufort = fields.Integer(string="Beaufort 1to12")
    evaporation = fields.Integer(string="Evaporation")

