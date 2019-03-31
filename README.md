# Gene-matrix-for-side-effect-prediction
Dataset we use:
>http://snap.stanford.edu/decagon/

Reference: realization of basic Resnet model
>https://github.com/bearpaw/pytorch-classification

# STEP 1 Visulization
  # 1.1
We totally have 7795 genes and 1317 Side effect,so firstly we set 7795 genes with id range from 0 to 7794 ,
and similarly 1317 side effects were assigned with id  from    0 to 1316

  # 1.2
We count the frequency of 7795 genes show up in each Side effect(Corresponding to a group of drug pairs) 
and draw these two figures as below:


fig.1 There are some common genes
[![Arcx9U.th.gif](https://s2.ax1x.com/2019/03/31/Arcx9U.th.gif)](https://imgchr.com/i/Arcx9U)
fig.2 Also some common genes
[![Arc27t.md.gif](https://s2.ax1x.com/2019/03/31/Arc27t.md.gif)](https://imgchr.com/i/Arc27t)
Filt out the common genes:


# STEP 2 Train a classifier using resnet 
Take the 100*80 gene matrix as image and do a 1317 classes classification
However, The result shows we cannot depend merely on drug-targets information 
to predict the polyphormacy side-effect

![Arstmt.png](https://s2.ax1x.com/2019/03/31/Arstmt.png)
