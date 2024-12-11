# RasPiDets: A Real-Time Defect Detection Method with End-Edge-Cloud Collaboration

# **Contents**
- [1.Introductiion](#1.Introductiion)
- [2.RasPiDets](#2.RasPiDets)
- [3.An easy starting instance](#3.starting_instance)
- [4.ACDO algorithm for End-Edge-Could Collaboration](#4.ACDO)
- [5.PDD System Implementation](#5.System)
- [6.Datasets](#6.Datasets)
- [7.STE for Audio Extraction](#7.STE_Audio)
- [8.Loss Function](#8.Loss)
- [9.Experiments](#9.Experiments)
- [10.Performance](#10.Performance)
- [11.Visualization of detection results](#11.Vis_Results)
- [12.Citation](#12.Cite)

<a name="1.Introductiion"></a>
## 1. Introductiion

Product Defect Detection (PDD) exists in many processes of industrial product production, which is an important workflow to sort out unqualified products. We focus on the PDD problem at multiple production stages, each of which produces specific data types and requires strict product quality control. 
In this work, we developed a lightweight PDD (RasPiDets) method with end-edge-cloud collaboration to defect the detection of product in industrial scenarios. 

<div align=center><img src="figs/PDD_Video.gif" width="800"></div>

Specifically, Audio Anomaly Detection (AAD) existed in Air Conditioner (AC) internal units and Appearance Defect Detection (ADD) raised in AC external units are a very important and time-consuming quality control process. 
This greatly restricts the beat of the assembly line, which in turn leads to a reduction in production efficiency. 
To solve this problem, we developed a lightweight PDD (RasPiDets) method with End-Edge-Cloud (EEC) collaboration to accelerate the detection speed of edge nodes.

![FFPDD System](figs/PDD_Arch.jpg)

**The main contributions are summarized as follows:**
  - An lightweight defect detection Network (RasPiDets) with cascaded U-Net architecture is proposed that can solve the different detection problems in a unified model.
  - A lightweight PDD (RasPiDets) method system with end-edge-cloud collaboration are proposed to accelerate the detection speed of edge nodes, which realizes the plug-and-play of edge nodes while improving the detection speed.
  - FFPDD offers a **1.2%** improvement in detection accuracy over current state-of-the-art (SOTA) models and an average **64%** reduction in detection time.
  - Two PDD datasets of AC manufacturing (SDU-Haier-AQD and SDU-Haier-ND) are open sourced to accelerate related research progress.

<a name="2.RasPiDets"></a>
## 2. RasPiDets

Considering together with the \``where are the defects'' problem existing in image type, we propose a Easy-to-Deploy defect detection Network (RasPiDets) that can solve the \``what'' and \``where'' detection problems in a unified network. 

<div align=center><img src="figs/RasPiDets_Arch.png", width="800"></div>

**The innovations of RasPiDets include:** 
- A cascaded U-Net architecture is designed to quickly obtain feature maps of various sizes; 
- The lightweight deep architecture can be easily obtained by stacking U-Nets;
- Numerous shortcut path is added between the feature maps in U-Nets to reduce model over-fitting；
- RasPiDets is a lightweight network architecture that can be deployed on Raspberry Pi.

<div align=center><img src="figs/compares.png", width="800"></div>

In the following list, symbol $\checkmark$ represents advantages, and symbol $\times$ represents disadvantages.

  1. **DETR**: This model is an encoder-decoder structure that adopts Transformer as its backbone.
  - $\checkmark$ It transforms the problem into a set prediction problem, simplifying the detection process.
  - $\times$ Its prediction performance suffers from inadequate utilization of multiscale features. For example, it has a lower mAP in small object recognition. In addition, it requires a longer training process. 

  2. **MobileNetv3**: The model is a mobile network obtained via a neural architecture search (NAS) algorithm.
  - $\checkmark$ It searches for the optimal number of channels and filters. Moreover, it adds many effective modules, such as Squeeze-and-Excitation module (SE) and hard-swish activation function. 
  - $\times$ The absence of multiscale (MC) features and dense connections (DC), coupled with the heavy reliance on numerous deepwise convolutions, renders it inadequate in extracting multi-resolution features, consequently leading to a degraded performance in detecting small objects.

  3. **YOLO v3, v4 and v7**: The design of the one-stage detection method enables faster detection speed, and larger resolution input improves its detection performance.
  - $\checkmark$ These are single-stage detection algorithms, and all have specially designed network structures and activation functions, e.g., DarkNet-53 and SiLU activation function.
  - $\times$ The network structure design is complex and there are numerous redundant features, which hinders its detection speed. In addition, the transfer of high-resolution features to later layers occurs at a slow pace, consequently leading to diminished detection accuracy for small target objects.

  4. **RasPiDets**: A lightweight model that can run smoothly on Raspberry Pi (RasPiDets) is good at solving the audio and image detection problems. 
  - $\checkmark$  RasPiDets contains many efficient components, such as multiscale (MS), dense connections (DC), inverted modules (IM), MB Cascade and Adaptive MS. 
  These components are crucial for enhancing performance and speed.
  - $\times$ The mAP of RasPiDets in specific categories is not uniformly optimal, such as in the categories of cyclone net.


<a name="3.starting_instance"></a>
## 3. An easy starting instance

1) Configure Darknet environment to accelerate RasPiDets, the details of the configuration can refer to [this](https://github.com/AlexeyAB/darknet).
  
2) Make dataset directory like this:
    - train (directory)
      - xx1.jpg (image sample)
      - xx1.txt (description file)
      - xx2.jpg (image sample)
      - xx2.txt (description file)
      - ......

3) Run the following code for training,

```
   cd RasPiDets
```
```python
./darknet detector train ./dataconfigs/ok.data ./configs/RasPiDets.cfg ./configs/RasPiDets_best.weights
```
4) Run the following code for validation
```
./darknet detector valid ./dataconfigs/ok.data ./configs/RasPiDets.cfg ./configs/RasPiDets_best.weights
```

5) Run the following code for testing
```python
./darknet detector test ./dataconfigs/ok.data ./configs/RasPiDets.cfg ./configs/RasPiDets_best.weights
```

6) Visualization of network architecture (Zoom Out)

<div align=center><img src="figs/RasPiDetsV1-H-Simple.png" width=""></div>

<a name="4.ACDO"></a>
## 4. ACDO algorithm for End-Edge-Could Collaboration

An Actor-Critic based Dynamic Offloading (ACDO) is designed to reduce the overall delay of RasPiDets on end devices.
Ultrasonic sensors, scanners and cameras are used to obtain the location, type and appearance of AC, respectively. 
They are connected with Raspberry Pi, an end device deployed with RasPiDets, to form a closed-loop process of perception, decision-making and control. 
In this end-edge-cloud collaboration scenario, the cloud has abundant computing capabilities but is far away from the end devices, and the edge servers are relatively close to the end devices but need to be connected to the end device via 5G network. 

<div align=center><img src="figs/EEC_System.jpg" width="600"></div>


<a name="5.System"></a>
## 5. PDD System Implementation

We built an assembly line for industrial production detection to implement the PDD system with end-edge-cloud collaboration. In this PDD system, Raspberry Pi (4B) is used as the edge node to connect end devices such as ultrasonic sensors, scanners and cameras to realize low-cost and flexible deployment of the PDD algorithm.
Subsequently, the edge nodes are connected to the cloud via 5G to offload and schedule PDD tasks to further improve the speed of the detection algorithm. 
This makes the deployment of PDD detection units in complex industrial scenarios with high convenience and low cost.
Finally, the negative detection results are sent to PLC to sort out the unqualified products. 

![Hardware System](figs/Hardware_System.jpg)

<a name="6.Datasets"></a>
## 6. Open Source Datasets

### 1) AAD Dataset
The initially sampled AAD data in AC internal unit is saved as `wav' files, and the sampling frequency of the audio signal is 48kHz. To efficiently utilize these audio files, the long piece of audio is splited into many frames and each of them is converted into the 2D spectrogram by SG-Gram algorithm. Therefore, the AAD dataset is a multi-label image detection dataset, which includes 562 training samples and 142 test samples. 

- We open-sourced the audio dataset with annotation files [here](https://ieee-dataport.org/documents/sdu-haier-nd-dataset-noise-detection).
- Alternatively, you can easily get the dataset by this [link](https://pan.baidu.com/s/1PPypTxRKZRpl3xOXghz-8A?pwd=f8ig).
- The detailed introduction document can be found [here](files/SDU-Haier-AAD-Dataset-Introduction.pdf).
<div align=center><img src="figs/AAD_Dataset_Fig.jpg" width="600"></div>



### 2) ADD Dataset
The ADD dataset includes 9401 training samples and 1408 testing samples.
There are totally 11 types of this dataset, each type has about 1000 images. 
This dataset contains 16 classes of objects to be detected, and each type contains a different number of classes. 
The number of categories of the 16 detected objects is shown in the following table. 

<div align=center><img src="figs/ADD_Dataset.jpg" width="600"></div>

- We open-sourced 10,449 samples with annotation files [here](https://ieee-dataport.org/documents/sdu-haier-aqd-dataset-appearance-quality-detection).
- Alternatively, you can easily get the dataset by this [link](https://pan.baidu.com/s/11FO1P-MZ52RuBgwWM7pOQw?pwd=zxp1).
- The detailed introduction document can be found [here](files/SDU-Haier-ADD-Dataset-Introduction.pdf).

<div align=center><img src="figs/ADD_Dataset_Fig.png" width="600"></div>

### 3) Statistics of Datasets
<div align=center><img src="figs/Datasets.jpg" width="600"></div>

<a name="7.STE_Audio"></a>
## 7. STE for Audio Extraction

### 1) STE 
We utilize the short-time energy method (STE) [18] to quickly extract effective audio signals, which can be formulated as
$$
    S(n) = \sum_{i=-\infty}^{\infty} x^2(n) \omega(n-i) = \sum_{i=n-M+1}^{n} x^2(i) \omega(n-1),
$$
where $n$ is the size of the window, $x(n)$ is input signals, $\omega(n)$ is a rectangular window function.

<div align=center><img src="figs/ExAAD.jpg" width=""></div>
*Short-Term Energy method (STE) for extracting valid audio clips. The solid red line in the waveform of audio indicates where a valid segment begins, and the solid blue line indicates where it ends.*

### 2) Other Audio Anomaly Detection Algorithms

Comparisons of different anomaly detection methods for extracting valid audio clips.
<div align=center><img src="figs/ExAAD_Other.jpg" width=""></div>

<a name="8.Loss"></a>
## 8. Loss Function

<div align=center><img src="figs/Class_Loss.jpg" width="400"></div>

<div align=center><img src="figs/Ressgion.jpg" width="400"></div>

<div align=center><img src="figs/LossCIoU.jpg" width="400"></div>

<a name="9.Experiments"></a>
## 9. Experiments 

### 1) AAD Tasks
RasPiDets achieves the best performance and fast runing speed compared to other SOTA models, realizing
the best trade-off between performance and speed. 
As shown in following figure, the performance (mAP), runing speed (FLOPs) and model size (parameters, indicated by bubble size) comparisons of different SOTA models on AAD tasks. 

<div align=center><img src="figs/mAP_AAD.jpg" width="600"></div>

### 2) ADD Tasks

The average mAP of RasPiDets is much better than that of other lightweight object detection models. 
As shown in following figure,  mAP of different models when IoU ≥ 0.75.

<div align=center><img src="figs/mAP75_ADD.jpg" width="600"></div>

<div align=center><img src="figs/mAP_11_ADD.jpg" width="600"></div>

<a name="10.Performance"></a>
## 10. Performance of ACDO Algorithms

AAD and ADD tasks with 3 priorities reach the lowest delay at different time intervals when ACDO is adopted. 

<div align=center><img src="figs/EEC_Perform.jpg"></div>

<a name="11.Vis_Results"></a>
## 11. Visualization of detection results

<div align=center><img src="figs/Results.jpg" width="600"></div>

<a name="12.Cite"></a>
## 12. Citation

Welcome to cite our paper. The infos of the paper will coming soon!