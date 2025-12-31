from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from .const import DOMAIN

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data[DOMAIN][entry.entry_id]

    async_add_entities([
        NextEnergyPriceSensor(coordinator, "current_market"),
        NextEnergyPriceSensor(coordinator, "current_market_plus"),
        NextEnergyPriceSensor(coordinator, "next_market"),
        NextEnergyPriceSensor(coordinator, "next_market_plus"),
    ])


class NextEnergyPriceSensor(CoordinatorEntity, SensorEntity):
    def __init__(self, coordinator, key):
        super().__init__(coordinator)
        self.key = key
        self._attr_name = f"NextEnergy {key.replace('_', ' ').title()}"
        self._attr_unique_id = f"nextenergy_{key}"

    @property
    def native_value(self):
        return round(self.coordinator.data.get(self.key, 0), 4)

    @property
    def native_unit_of_measurement(self):
        return "€/kWh"
