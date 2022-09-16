from Car.Battery.spindler_battery import SpindlerBattery
from engine.capulet_engine import CapuletEngine


class Calliope(CapuletEngine, SpindlerBattery):
    def needs_service(self):
        return self.engine_should_be_serviced() or self.battery_should_be_serviced()
