import logging
from aiohttp import ClientTimeout
from homeassistant.helpers import aiohttp_client
from .const import API_URL

_LOGGER = logging.getLogger(__name__)
_LOGGER.debug("Fetched %d prices", len(prices))

class NextEnergyAPI:
    def __init__(self, hass, username, password):
        self.hass = hass
        self.username = username
        self.password = password

    async def test_connection(self):
        """Test if credentials are valid."""
        await self.fetch_prices()

    async def fetch_prices(self):
        timeout = ClientTimeout(total=20)
        session = aiohttp_client.async_get_clientsession(
            self.hass, timeout=timeout
        )

        payload = {
            "username": self.username,
            "password": self.password,
        }

        try:
            async with session.post(API_URL, json=payload) as resp:
                if resp.status != 200:
                    text = await resp.text()
                    _LOGGER.error("API error %s: %s", resp.status, text)
                    raise Exception(f"API error {resp.status}")

                data = await resp.json()

        except Exception as err:
            _LOGGER.error("Failed to fetch NextEnergy data: %s", err)
            raise

        prices = data.get("prices")
        if not prices:
            raise Exception("No price data returned from API")

        return prices
