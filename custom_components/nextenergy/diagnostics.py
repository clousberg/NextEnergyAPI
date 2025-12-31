from __future__ import annotations

from typing import Any

from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

from .const import DOMAIN


async def async_get_config_entry_diagnostics(
    hass: HomeAssistant,
    entry: ConfigEntry,
) -> dict[str, Any]:
    """Return diagnostics for a config entry."""

    coordinator: DataUpdateCoordinator = hass.data[DOMAIN][entry.entry_id]

    diagnostics_data = {
        "entry": {
            "entry_id": entry.entry_id,
            "title": entry.title,
            "version": entry.version,
            "data": _redact_sensitive(entry.data),
            "options": entry.options,
        },
        "coordinator": {
            "last_update_success": coordinator.last_update_success,
            "update_interval": str(coordinator.update_interval),
            "data_available": coordinator.data is not None,
        },
        "data_sample": _safe_sample_data(coordinator.data),
    }

    return diagnostics_data


def _redact_sensitive(data: dict) -> dict:
    """Remove sensitive fields."""
    redacted = {}
    for key, value in data.items():
        if key.lower() in {"password", "token", "api_key", "secret"}:
            redacted[key] = "***REDACTED***"
        else:
            redacted[key] = value
    return redacted


def _safe_sample_data(data: Any) -> Any:
    """Return safe subset of coordinator data."""
    if not isinstance(data, dict):
        return None

    return {
        key: value
        for key, value in data.items()
        if key not in {"prices", "raw", "all_prices"}
    }
