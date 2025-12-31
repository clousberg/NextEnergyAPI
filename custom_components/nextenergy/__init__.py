from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
from .const import DOMAIN
from .coordinator import NextEnergyDataUpdateCoordinator

PLATFORMS: list[Platform] = [Platform.SENSOR]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    # Maak coordinator
    coordinator = NextEnergyDataUpdateCoordinator(hass, entry)

    # Eerste data ophalen (belangrijk!)
    await coordinator.async_config_entry_first_refresh()

    # Opslaan zodat sensor.py erbij kan
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = coordinator

    # Platforms laden
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    hass.data[DOMAIN].pop(entry.entry_id, None)
    return True
