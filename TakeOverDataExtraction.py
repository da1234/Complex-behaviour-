import numpy as np
import matplotlib.pyplot as plt 



def extract():

        for size in range(1,18,1):

          prob_array = np.zeros(20)

          cnt = 0
        
          with open('/Users/darrelladjei/python/bsc/mesaStuff/SystemSizeData/nineway/'+str(size)+'.txt','r') as f: 
        

            while cnt < 20:
                prob = float(f.readline())
                prob_array[cnt] = prob
                cnt+=1

          mean = np.mean(prob_array)
          std = np.std(prob_array)
          both = np.array([mean,std])
          np.savetxt('/Users/darrelladjei/python/bsc/mesaStuff/SystemSizePlottingData/nineway/' + str(size)+'.txt',both)



def plotTakeOverProb():
        
        cnt = 0
        mean_prob_array = np.zeros(16)
        std_array = np.zeros(16)
        sizes = np.arange(1,17)

        for size in range(1,17,1):
       
          with open('/Users/darrelladjei/python/bsc/mesaStuff/SystemSizePlottingData/threeway/'+str(size)+'.txt','r') as f: 
        

                mean = float(f.readline())
                std = float(f.readline())
                mean_prob_array[cnt] = mean
                std_array[cnt] = std
                
          cnt+=1

          #print(mean_prob_array.shape,std_array.shape)

        plt.errorbar(x=sizes**2,y=mean_prob_array,yerr=std_array)
        plt.grid()
        plt.xlabel("grid size")
        plt.ylabel("Takeover probability")
        plt.title("Graph of takeover versus grid size for single strat")
        plt.show()

#extract()
plotTakeOverProb()
        



