# @gymcam/sdk

Official JavaScript/TypeScript SDK for [GymCam Analytics](https://gymcamanalytics.com) — camera-based gym attendance and trainer-performance analytics.

## Install

```bash
npm install @gymcam/sdk
```

## Quick start

```js
const { GymCamClient } = require("@gymcam/sdk");

const client = new GymCamClient({ apiKey: "your-api-key" });

await client.summary();               // today's summary
await client.trainerAttendance("Alex"); // trainer fill rate + no-shows
await client.classPerformance();      // classes ranked by fill rate
await client.revenueInsights();       // most profitable vs. dead classes
```

## Sandbox mode

```js
const client = new GymCamClient({ sandbox: true });
```

## Requirements

- Node.js 18+ (uses the built-in `fetch`)

## License

MIT
