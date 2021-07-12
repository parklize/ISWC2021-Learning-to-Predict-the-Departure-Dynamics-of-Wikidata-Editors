# ISWC2021-Learning-to-Predict-the-Departure-Dynamics-of-Wikidata-Editors
Repository for ISWC2021 paper - "Learning to Predict the Departure Dynamics of Wikidata Editors". 

The directory structure of our ISWC code is illustrated as below, where some main files include:

```python
baseline1 
+-- baseline1.ipynb # includes the implementations of GBT-Zh and kNN-Zh
baseline2
+-- baseline2.ipynb # contains the implementations of RF-Sa and LR-Sa
baseline3
+-- svm-ar-baseline.ipynb # includes the implentation of SVM-Ar
proposed
+-- proposed.ipynb # contains the implementation of our DeepFM-based approaches such as DeepFM-Stat, DeepFM-Pattern, and DeepFM-Stat+Pattern
data # contains data files (Python pickle files) for training and testing sets ready for each classification approach
requirements.txt  # packages to be installed using pip install -r requirements.txt
```



