# ISWC2021-Learning-to-Predict-the-Departure-Dynamics-of-Wikidata-Editors
Repository for ISWC2021 paper - "Learning to Predict the Departure Dynamics of Wikidata Editors". 

<br/>

## Abstract

Wikidata as one of the largest open collaborative knowledge bases has drawn much attention from researchers and practitioners since its launch in 2012. As it is collaboratively developed and maintained bya community of a great number of volunteer editors, understanding and predicting the departure dynamics of those editors are crucial but have not been studied extensively in previous works. In this paper, we inves-tigate the synergistic effect of two different types of features: statistical and pattern-based ones with DeepFM as our classification model which has not been explored in a similar context and problem for predicting whether a Wikidata editor will stayorleave the platform. Our experimental results show that using the two sets of features with DeepFM provides the best performance regarding *AUROC(0.9561)* and *F1-score(0.8843)*, and achieves substantial improvement compared to using either of the sets of features and over a wide range of baselines.

<br/>

## Folder structure

The directory structure of our ISWC code is illustrated as below, where some main files include:

```python
baseline1 
├── baseline1.ipynb # includes the implementations of GBT-Zh and kNN-Zh
baseline2
├── baseline2.ipynb # contains the implementations of RF-Sa and LR-Sa
baseline3
├── svm-ar-baseline.ipynb # includes the implentation of SVM-Ar
proposed
├── proposed.ipynb # contains the implementation of our DeepFM-based approaches such as DeepFM-Stat, DeepFM-Pattern, and DeepFM-Stat+Pattern
data # contains data files (Python pickle files) for training and testing sets ready for each classification approach
requirements.txt  # packages to be installed using pip install -r requirements.txt
```

<br/>


## How to use


We recommend you to install [Anaconda](https://www.anaconda.com/) as your basic Python library, here our code is running on ```Python 3.7.10```. You can use this code according to the following steps.

- Download our code (zip file) to your local machine
- Unzip the zip file. If you use Windows or Mac, you can double click the zip file. Otherwise, you can use the unzip command to unzip it.
- We recommend you to create one specific environment for this code, if you do not care about this issue, you can skip to step 5. The command is ```conda create -n ISWCTest python=3.7.10```
- Activate the python environment. The command is ```conda activate ISWCTest```
- Install all required python packages, we have provided the requirements file, so you can use the command: ```pip install -r requirements.txt```
- Set up kernel with the virtual environment for Jupyter Notebook: ```python -m ipykernel install --user --name ISWCTest --display-name "ISWCTest"```
- Launch Jupyter notebook: ```jupyter-notebook```
- Click a ```.ipynb``` notebook for a specific method. From menu, select ```ISWCTest``` as your kernel: ```Kernel → Change kernel```



You can choose any notebook (e.g., ```baseline1.ipynb```) for training or testing corresponding models. If you want to reproduce the experimental results, please load the pre-trained models for the paper for testing in each notebook. Owing to the randomness of the training phase, the experimental results have a little fluctuation, but from the overall perspective, the experimental results are stable.

<br/>

## Processed edit history

A processed edit history that is used to extract features for the experiments are available [here](https://drive.google.com/file/d/1BDvSKp2j8ZH4vBdSYgYjQEqUJMOAP4Ug/view?usp=sharing) (8.3GB zip file) where the unzipped csv file (67GB) contains edit history in the format of:
Entity  Time  Username  Comment

<br/>

## Citation

Guangyuan Piao, Weipeng Huang, "Learning to Predict the Departure Dynamics of Wikidata Editors", The 20th International Semantic Web Conference, 2021. [[PDF](https://parklize.github.io/publications/ISWC2021.pdf)] [[BibTex](https://parklize.github.io/bib/ISWC2021.bib)]
