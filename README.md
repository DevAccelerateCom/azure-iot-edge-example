# Azure IoT Edge Example 🚀

This repository contains an example of Edge Computing with Azure IoT.

## 📂 Project Structure
- `device-app/` → Docker application that simulates a temperature sensor and sends data to IoT Hub.
- `event-consumer/` → Consumer that reads messages from the Event Hub.

## 🚀 Quick Start
### 1️⃣ Configure Environment Variables
Create a `.env` file (DO NOT commit to GitHub) and add:

```sh
# For the device
export IOT_HUB_CONNECTION_STRING="HostName=..."
# For the consumer
export EVENT_HUB_CONNECTION_STRING="Endpoint=..."
export EVENT_HUB_NAME="..."
```

