# Advanced-ML-ETHZ

## Arrhythmia Classification of ECG Signals
This project aims to classify the ECG signal of a patient (i.e. a series of consecutive heartbeats) into four different classes, which are illustrated in Figure 1. One of the classes contains healthy patients while the other three classes contain patients with different kinds of arrhythmia.

Figure 1: Average heartbeat per class.
![](ecg_classification/figures/ecg_classes.png)

The data processing pipeline is as follows. First, the series of heartbeats is split into single heartbeats (see Figure 2). From these, we engineer various kinds of features that are used in different boosting models. Eventually, we build an ensemble by averaging the predictions of all trained models.

Figure 2: ECG signal of a patient.
![](ecg_classification/figures/ecg_heartbeat_ts.png)

Feature engineering is a critical task to classify ECG signals correctly. By using the neurokit2 package and plain Python code we created various features that can be grouped into the categories of heart rate variability, frequency domain, higher-order statistics (skew and kurtosis), interval features (e.g. QP interval) and sample features (sample equally distant points from the mean and variance of the average heartbeat). Moreover, we want to emphasize that not all features could be calculated for every ECG. Therefore, we pushed the error handling down to the individual feature calculations to only have a few features with missing values.

Figure 3: Location of different peaks of a heartbeat.
![](ecg_classification/figures/ecg_peaks.png)

---

## Mitral Valve Segmentation
The segmentation of the mitral valve from an echocardiogram video is usually a key step in any automated pipeline for the diagnosis of diseases affecting the mitral valve. To tackle this task we relied on a convolutional neural network architecture often used for the segmentation of biomedical images called U-Net. One of the main challenges was the limited size of the training data that consisted of a few dozens of videos. To deal with this issue we used a network with pretrained weights (that we fine-tuned on our data) and multiple data-augmentation techniques (e.g. grid distortion). Finally, to gain some additional robustness, for the final model we opted for an ensemble of a handful of such networks.

Figure 4: Echocardiogram frame on the right and the corresponding mask on the left.
![](mitral_valve_segmentation/figures/heart_mitral_valve.png)

