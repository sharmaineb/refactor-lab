# by Kami Bigdely
# Docstrings and blank lines

class OnBoardTemperatureSensor:
    """Represents an onboard temperature sensor."""
    VOLTAGE_TO_TEMP_FACTOR = 5.6

    def __init__(self):
        """Initializes the temperature sensor."""
        pass

    def read_voltage(self):
        """Reads the voltage from the sensor."""
        return 2.7

    def get_temperature(self):
        """Calculates and returns the temperature in Celsius."""
        return self.read_voltage() * OnBoardTemperatureSensor.VOLTAGE_TO_TEMP_FACTOR # [celcius]
  
class CarbonMonoxideSensor:
    """Represents a carbon monoxide sensor."""
    VOLTAGE_TO_CO_FACTOR = 0.048

    def __init__(self, temperature_sensor):
        """Initializes the carbon monoxide sensor with a temperature sensor."""
        self.on_board_temp_sensor = temperature_sensor
        if not self.on_board_temp_sensor:
            self.on_board_temp_sensor = OnBoardTemperatureSensor()

    def get_carbon_monoxide_level(self):
        """Calculates and returns the carbon monoxide level."""
        sensor_voltage = self.read_sensor_voltage()
        self.carbon_monoxide = CarbonMonoxideSensor.convert_voltage_to_carbon_monoxide_level(sensor_voltage, self.on_board_temp_sensor.get_temperature())
        return self.carbon_monoxide

    def read_sensor_voltage(self):
        """Reads the sensor voltage (placeholder for real hardware interaction)."""
        # In real life, it should read from hardware.  
        return 2.3

    @staticmethod
    def convert_voltage_to_carbon_monoxide_level(voltage, temperature):
        """Converts voltage and temperature readings to a carbon monoxide level."""
        return voltage * CarbonMonoxideSensor.VOLTAGE_TO_CO_FACTOR * temperature
    
class DisplayUnit:
    """Represents a display unit."""
    def __init__(self):
        """Initializes the display unit."""
        self.string = ''

    def display(self, msg):
        """Displays a given message."""
        print(msg)

class CarbonMonoxideDevice:
    """Represents a carbon monoxide detection device."""
    def __init__(self, co_sensor, display_unit):
        """Initializes the device with a CO sensor and a display unit."""
        self.carbon_monoxide_sensor = co_sensor 
        self.display_unit = display_unit       

    def display(self):
        """Displays the carbon monoxide level."""
        msg = 'Carbon Monoxide Level is: ' + str(self.carbon_monoxide_sensor.get_carbon_monoxide_level())
        self.display_unit.display(msg)

if __name__ == "__main__":
    temp_sensor = OnBoardTemperatureSensor()
    co_sensor = CarbonMonoxideSensor(temp_sensor)
    display_unit = DisplayUnit()
    co_device = CarbonMonoxideDevice(co_sensor, display_unit)
    co_device.display()