import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
wine = load_wine() 
df = pd.DataFrame(wine.data, columns=wine.feature_names)
df = StandardScaler().fit_transform(df) 
df=pd.DataFrame(df,columns=wine.feature_names)
tsne = TSNE(random_state=0)
tsne_results = tsne.fit_transform(df)
tsne_results=pd.DataFrame(tsne_results, columns=['tsne1', 'tsne2'])
plt.scatter(tsne_results['tsne1'], tsne_results['tsne2'], c=wine.target)
plt.show()
enc_out=[[0,1,0],
         [1,2,3]
         ]
from sklearn.manifold import TSNE
enc_out_his+=enc_out[0]
tsne = TSNE(random_state=0)
tsne_results = tsne.fit_transform(df)
tsne_results=pd.DataFrame(tsne_results, columns=['tsne1', 'tsne2'])
plt.scatter(tsne_results['tsne1'], tsne_results['tsne2'], c=wine.target)
plt.show()
TSNE(n_components=2,perplexity=)