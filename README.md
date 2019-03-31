# Gene-matrix-for-side-effect-prediction
Dataset we use:
>http://snap.stanford.edu/decagon/

Reference: realization of basic Resnet model
>https://github.com/bearpaw/pytorch-classification

This primitive experiment use CNN to extract the gene-data-feature for each kind of Polypharmacy side effect.

So that to find out whether we can use gene data of two drugs to predict possible side effect.

# STEP 1 Visulization
  # 1.1
We totally have 7795 genes and 1317 Side effect,so firstly we set 7795 genes with id range from 0 to 7794 ,
and similarly 1317 side effects were assigned with id  from    0 to 1316(easy to compute and visualize)

  # 1.2
We count the frequency of 7795 genes show up in each Side effect(Corresponding to a group of drug pairs) 
and draw these figures :

**Click the iamge to play fig.1:**

[![Ar2CRS.md.gif](https://s2.ax1x.com/2019/03/31/Ar2CRS.md.gif)](https://imgchr.com/i/Ar2CRS)

fig.1 There are some common genes in each side effect

At first, we assume the least frequent genes in this figure are the main factor to determine 
the type of side effect may appear

**Click the iamge to play fig.2:**

[![Ar2BsH.md.gif](https://s2.ax1x.com/2019/03/31/Ar2BsH.md.gif)](https://imgchr.com/i/Ar2BsH)

fig.2 Each pixel stand for a specific gene(0~7794),this is a 100*80 matrix
We can found that some genes appear frequently, so we filted them out in next gif as below:

After filtering out the common genes,**click the picture to play gif**:

[![Ar2dzD.md.gif](https://s2.ax1x.com/2019/03/31/Ar2dzD.md.gif)](https://imgchr.com/i/Ar2dzD)

# STEP 2 Train a classifier using resnet 
Take the 100*80 filtered gene matrix as image and do a 1317 classes classification
However, The result shows we cannot depend merely on drug-targets information 
to predict the polyphormacy side-effect

![Arstmt.png](https://s2.ax1x.com/2019/03/31/Arstmt.png)

# Limitation of these dataset
Firstly,some drugs (about 10~20%) are lack of genes targets data, which makes our model unstable 
and hard to reach a convergence.

Secondly,the genes data in each drug-drug transaction is limited and mostly common gene,thus too 
similar for classifier to distinguish,which also detrimental for our training session.

# Conclusion
May be we cannot rely on gene-gene relations to predict side effect due to the limited info we have
and other unexpected factors.

# Other approaches
We also use Apriori algorithm to mine patterns inside this dataset, however the time complexcity 
doesn't allow us to do so.So is FP-growth algorithm, the memory exceed easily. 
