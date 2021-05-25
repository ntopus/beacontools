class MinewS1Frame(object):
    """Eddystone TLM frame."""
    def __init__(self, data):
        self._battery_level = data['battery_level']
        self._temperature = data['temperature'] / float(256)
        self._humidity = data['humidity']

    @property
    def battery_level(self):
        """Battery voltage measured in mV."""
        return self._battery_level

    @property
    def temperature(self):
        """Temperature in degree Celsius."""
        return self._temperature

    @property
    def humidity(self):
        """Humidity percentage"""
        return self._humidity

    @property
    def properties(self):
        """Get beacon properties."""
        return {
            'battery_level': self.battery_level,
            'temperature': self.temperature,
            'humidity': self.humidity,
        }

    def __str__(self):
        return "MinewS1Frame<battery level: %d\%, temperature: %f Celsius, humidity: %f\%>" % (self.voltage, self.temperature, \
                self.humidity)
