# gymcam-sdk

Official Python SDK for [GymCam Analytics](https://gymcamanalytics.com) — camera-based gym attendance and trainer-performance analytics.

## Install

```bash
pip install gymcam-sdk
```

## Quick start

```python
from gymcam_sdk import GymCamClient

client = GymCamClient(api_key="your-api-key")

client.summary()                 # today's summary
client.trainer_attendance("Alex") # trainer fill rate + no-shows
client.class_performance()        # classes ranked by fill rate
client.revenue_insights()         # most profitable vs. dead classes
```

## Sandbox mode

```python
client = GymCamClient(sandbox=True)
```

## Requirements

- Python 3.9+
- [`httpx`](https://www.python-httpx.dev/) (installed automatically)

## License

MIT
