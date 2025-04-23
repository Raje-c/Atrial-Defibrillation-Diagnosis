# STEP 1: Install required libraries
!pip install wfdb --quiet
!pip install neurokit2 --quiet

# STEP 2: Import libraries
import numpy as np
import matplotlib.pyplot as plt
import neurokit2 as nk
from scipy.stats import variation  # For coefficient of variation

# STEP 3: Simulate ECG signal
fs = 250  # Sampling rate
ecg_signal = nk.ecg_simulate(duration=10, sampling_rate=fs)

# STEP 4: Process ECG signal
signals, info = nk.ecg_process(ecg_signal, sampling_rate=fs)
r_peaks = info["ECG_R_Peaks"]

# STEP 5: Plot ECG with R-peaks
nk.signal_plot(signals)  # Replaced ecg_plot() with signal_plot()

# STEP 6: Compute RR intervals
rr_intervals = np.diff(r_peaks) / fs  # in seconds
print("RR intervals (s):", rr_intervals)

# STEP 7: Detect AFib using Coefficient of Variation (CV)
cv = variation(rr_intervals)
print("Coefficient of Variation (RR):", round(cv, 3))

# STEP 8: Simple decision logic
if cv > 0.25:
    print("⚠️ Possible Atrial Fibrillation Detected")
else:
    print("✅ Normal Sinus Rhythm")