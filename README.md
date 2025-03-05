 
# Arduino-Based Smoke Detection System

## Overview

This project is an **Arduino-based smoke detection system** developed in April 2023, utilizing an **MQ6 sensor** to monitor air quality and detect smoke levels in real-time. The system integrates an **ESP32** for Wi-Fi connectivity, enabling **SMTP-based email alerts** for remote monitoring. Visual feedback is provided via a green LED (no smoke) and a red LED with a buzzer (smoke detected), ensuring immediate user notification.

---

## Features

- **Smoke Detection**: Monitors air quality using the MQ6 sensor with real-time data processing.
- **Visual & Auditory Alerts**: Green LED for safe conditions, red LED and buzzer for smoke detection.
- **Email Notifications**: Sends alerts via SMTP protocol using ESP32’s Wi-Fi capabilities.
- **IoT Integration**: Remote monitoring through ESP32’s wireless communication.

---

## Prerequisites

### Hardware
- **Arduino Uno** (or compatible board)
- **ESP32 Module** (e.g., ESP32-WROOM-32)
- **MQ6 Gas Sensor** (for smoke detection)
- **LEDs**: Green and Red
- **Buzzer**: Active or passive
- **Breadboard & Jumper Wires**
- **Power Supply**: 5V USB or external source

### Software
- **Arduino IDE**: For programming and uploading code
- **ESP32 Board Support**: Install via Arduino IDE Boards Manager
- **Libraries**: 
  - `WiFi.h` (ESP32 Wi-Fi)
  - `ESP32_MailClient.h` (SMTP email)

 
