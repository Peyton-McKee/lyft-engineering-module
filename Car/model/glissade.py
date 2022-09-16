from Car.Battery.spindler_battery import SpindlerBattery
from engine.willoughby_engine import WilloughbyEngine


class Glissade(WilloughbyEngine, SpindlerBattery):
    def needs_service(self):
        return self.engine_should_be_serviced() or self.battery_should_be_serviced()