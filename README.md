# NextEnergy Home Assistant Integration

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://hacs.xyz/)
[![Version](https://img.shields.io/github/v/release/clousberg/NextEnergyAPI)](https://github.com/clousberg/NextEnergyAPI/releases)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Issues](https://img.shields.io/github/issues/clousberg/NextEnergyAPI)](https://github.com/clousberg/NextEnergyAPI/issues)
[![Quality Scale](https://img.shields.io/badge/Quality-Silver-yellow)](https://developers.home-assistant.io/docs/quality_scale/)


# NextEnergy API (Home Assistant Integration)

Fetches and displays NextEnergy API data from the Customer Portal.

Currently supporting  Market and Market+ rates.

## Credentials

Provide via UI or in `secrets.yaml`:

```
nextenergy_username: "YOUR_USERNAME"
nextenergy_password: "YOUR_PASSWORD"
```

## Installation

1. Add this repo as a [custom repository in HACS](https://hacs.xyz/docs/faq/custom_repositories/).
2. Install via HACS.
3. Restart Home Assistant.
4. Add the integration via the UI and provide your credentials (or use `secrets.yaml`).

## Sensors

- `sensor.nextenergy_current_market`
- `sensor.nextenergy_current_market_plus`
- `sensor.nextenergy_next_market`
- `sensor.nextenergy_next_market_plus`

## Notes

- Market = raw exchange price.
- Market+ = all-in price (market + taxes + VAT).

## License

MIT

## THANKS

Big thansk to https://github.com/iacavd/NextEnergyPricesHA and https://github.com/ServError/NextEnergyPricesHA
for the analysis and coding!
