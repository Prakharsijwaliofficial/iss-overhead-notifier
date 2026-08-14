# 🚀 ISS Overhead Notifier

A Python automation project that tracks the **International Space Station (ISS)** and sends an email notification when the ISS is close to my location and it is currently dark.

The project uses the ISS position API, the Sunrise-Sunset API, Python SMTP, and GitHub Actions for automated execution.

---

## 🌍 Project Overview

The program continuously checks:

1. 📡 The current position of the ISS.
2. 📍 Whether the ISS is within ±5° of my location.
3. 🌅 The local sunrise and sunset times.
4. 🌙 Whether it is currently dark.
5. 📧 If both conditions are satisfied, an email alert is sent.

The automated version runs through **GitHub Actions**, allowing the program to perform these checks without my computer needing to stay switched on.

---

## ✨ Features

- 🌍 Real-time ISS location tracking
- 📍 Latitude and longitude comparison
- 🌅 Sunrise and sunset detection
- 🌙 Nighttime detection
- 📧 Automated email notifications
- 🔐 Secure email credentials using GitHub Secrets
- ⚙️ Automated execution using GitHub Actions
- 🌐 API-based Python application

---

## 🛠️ Technologies Used

- Python
- `requests`
- `datetime`
- `smtplib`
- GitHub Actions
- GitHub Secrets

---

## 🌐 APIs Used

### ISS Location API

Used to retrieve the current latitude and longitude of the International Space Station.

### Sunrise-Sunset API

Used to retrieve sunrise and sunset times for my location.

---

## 📂 Project Structure

```text
iss-overhead-notifier/
│
├── main.py
│
├── README.md
│
└── .github/
    └── workflows/
        └── iss.yml
