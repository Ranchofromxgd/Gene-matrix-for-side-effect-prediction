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


# STEP 2 Train a classifier using resnet 
The result shows we cannot depend merely on drug-targets information to predict the polyphormacy side-effect

![Arstmt.png](https://s2.ax1x.com/2019/03/31/Arstmt.png)
