# ISWC2021-Learning-to-Predict-the-Departure-Dynamics-of-Wikidata-Editors
Repository for ISWC2021 paper - "Learning to Predict the Departure Dynamics of Wikidata Editors". 

<br/>

### Folder structure

----------------------------------------------

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


### How to use

------------------------------------

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
