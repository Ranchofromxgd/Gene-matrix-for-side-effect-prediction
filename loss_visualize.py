import matplotlib.pyplot as plt
import pickle

f = open('loss2.pkl','rb')
d = pickle.load(f)

plt.figure()
plt.title('batchsize')
plt.subplot(121)
plt.plot(d['top1'][:20000])
plt.plot(d['top5'][:20000])
plt.xlabel('batches')
plt.ylabel('accuracy (%)')
plt.legend(['top1','top5'])
plt.subplot(122)
plt.plot(d['loss'][:5000])
plt.legend(['loss'])
plt.xlabel('batches')
plt.ylabel('loss')
plt.show()
