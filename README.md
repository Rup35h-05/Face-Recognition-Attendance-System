# 👁️ Face Recognition Attendance System

## 🧠 Overview
The **Face Recognition Attendance Register** is a Python-based application that uses **dlib’s pre-trained face recognition model** to automatically mark attendance based on facial identification.  
It captures faces from a live camera feed, compares them with stored face encodings, and records attendance details (name, date, and time) in a **SQLite3 database**.

This system eliminates the need for manual attendance marking and ensures **accuracy**, **speed**, and **security** in tracking attendance.

---

## 💡 Features
- 👤 **Automatic Face Detection & Recognition** — Uses dlib’s pre-trained model for accurate recognition.  
- 🧾 **Attendance Logging** — Stores date and time for each recognized individual in a SQLite3 database.  
- 🗄️ **User Registration System** — Register new users with their facial data and name.  
- 🧩 **Offline Functionality** — Fully local; no internet connection required.  
- 🕵️ **Duplicate Prevention** — Ensures a person’s attendance is recorded only once per session.  
- 📸 **Real-Time Processing** — Detects and identifies faces from a webcam feed in real time.

---

## 🧩 Tech Stack

| Component | Technology Used |
|------------|-----------------|
| **Programming Language** | Python 3.x |
| **Face Recognition** | dlib (pre-trained `dlib_face_recognition_resnet_model_v1.dat`) |
| **Image Processing** | OpenCV |
| **Database** | SQLite3 |
| **Data Storage** | Local files for face encodings and database for attendance |
| **GUI (optional)** | Tkinter / Streamlit (if UI is added) |

---
