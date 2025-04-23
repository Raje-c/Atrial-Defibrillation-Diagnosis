## 📌 Overview

Atrial Fibrillation (AFib) is one of the most common cardiac arrhythmias and is associated with an increased risk of stroke, heart failure, and other heart-related complications. It is typically characterized by an irregular and often rapid heart rate, which results in inconsistent intervals between heartbeats (RR intervals) in an ECG signal.

This project aims to provide a simple, interpretable, and beginner-friendly approach to detecting possible Atrial Fibrillation events using Python. The program processes ECG data — either simulated or real-world — and identifies irregularities in heart rhythms through RR interval analysis.

### 🔍 Key Functionalities

- **ECG Signal Simulation or Import**: You can simulate synthetic ECG signals using NeuroKit2 or import real patient ECG data from external files such as CSV, MIT-BIH databases, etc.
  
- **R-Peak Detection**: Using NeuroKit2's advanced signal processing capabilities, the tool detects R-peaks — the prominent upward spikes in an ECG corresponding to each heartbeat.
  
- **RR Interval Computation**: Once R-peaks are identified, the time differences between successive peaks (RR intervals) are computed to analyze heart rhythm consistency.
  
- **Atrial Fibrillation Detection**: The tool calculates the **coefficient of variation (CV)** of the RR intervals. If the CV exceeds a certain threshold (commonly > 0.25), the signal is flagged as potentially indicative of AFib.
  
- **ECG Visualization**: The ECG waveform is plotted along with detected R-peaks, giving a clear visual representation of the heart's electrical activity.

### 🎯 Goals

This project serves as:
- A foundational framework for ECG signal analysis.
- A simple model to understand how arrhythmia and irregular heart rhythms can be detected computationally.
- A starting point for building more complex machine learning or deep learning-based arrhythmia detection systems.
