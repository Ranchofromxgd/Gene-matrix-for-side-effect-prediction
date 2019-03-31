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

Click the picture to play gif:
![Ar2CRS.gif](https://s2.ax1x.com/2019/03/31/Ar2CRS.gif)
fig.1 There are some common genes

Click the picture to play gif:
[![Arc27t.md.gif](https://s2.ax1x.com/2019/03/31/Arc27t.md.gif)](https://imgchr.com/i/Arc27t)
fig.2 Each pixel stand for a specific gene(0~7794),this is a 100*80 matrix

After filtering out the common genes,click the picture to play gif:
![Argtgg.gif](https://s2.ax1x.com/2019/03/31/Argtgg.gif)

# STEP 2 Train a classifier using resnet 
Take the 100*80 gene matrix as image and do a 1317 classes classification
However, The result shows we cannot depend merely on drug-targets information 
to predict the polyphormacy side-effect

![Arstmt.png](https://s2.ax1x.com/2019/03/31/Arstmt.png)
