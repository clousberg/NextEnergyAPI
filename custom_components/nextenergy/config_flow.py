from homeassistant import config_entries
import voluptuous as vol
from .const import DOMAIN
from .api import NextEnergyAPI
import logging

_LOGGER = logging.getLogger(__name__)

class NextEnergyConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}

        if user_input is not None:
            # Prevent duplicate setup
            await self.async_set_unique_id(user_input["username"])
            self._abort_if_unique_id_configured()

            # Optional: test credentials
            try:
                api = NextEnergyAPI(
                    self.hass,
                    user_input["username"],
                    user_input["password"]
                )
                await api.test_connection()
            except Exception as err:
                _LOGGER.error("NextEnergy connection failed: %s", err, exc_info=True)
                errors["base"] = "cannot_connect"
                return self.async_show_form(step_id="user", data_schema=self._get_data_schema(), errors=errors)
            else:
                return self.async_create_entry(
                    title="NextEnergy",
                    data=user_input,
                )

        schema = vol.Schema({
            vol.Required("username"): str,
            vol.Required("password"): str,
        })

        return self.async_show_form(
            step_id="user",
            data_schema=schema,
            errors=errors,
        )
