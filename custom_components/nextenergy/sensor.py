from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from .const import DOMAIN


async def async_setup_entry(hass, entry, async_add_entities):
    """Set up NextEnergy sensors."""
    coordinator = hass.data[DOMAIN][entry.entry_id]

    async_add_entities([
        NextEnergyPriceSensor(coordinator, "current_market", entry),
        NextEnergyPriceSensor(coordinator, "current_market_plus", entry),
        NextEnergyPriceSensor(coordinator, "next_market", entry),
        NextEnergyPriceSensor(coordinator, "next_market_plus", entry),
    ])


class NextEnergyPriceSensor(CoordinatorEntity, SensorEntity):
    """Representation of a NextEnergy price sensor."""

    def __init__(self, coordinator, key, entry):
        super().__init__(coordinator)
        self.key = key
        self.entry = entry
        self._attr_name = f"NextEnergy {key.replace('_', ' ').title()}"
        self._attr_unique_id = f"nextenergy_{key}"

    @property
    def native_value(self):
        return round(self.coordinator.data.get(self.key, 0), 4)

    @property
    def native_unit_of_measurement(self):
        return "€/kWh"

    @property
    def device_info(self):
        """Return device information for grouping sensors."""
        return {
            "identifiers": {(DOMAIN, self.entry.entry_id)},
            "name": "NextEnergy",
            "manufacturer": "NextEnergy",
            "model": "NextEnergy API",
            "sw_version": self.entry.version,
            "entry_type": "service",
        }
