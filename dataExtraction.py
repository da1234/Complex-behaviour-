import numpy as np



def extract():

        for size in range(1,18,1):
          prob_array = np.zeros(20)
          cnt = 0        
          with open('/Users/darrelladjei/python/bsc/mesaStuff/SystemSizeData/'+str(size)+'.txt','r') as f:         
            while cnt < 20:
                prob = float(f.readline())
                prob_array[cnt] = prob
                cnt+=1
          mean = np.mean(prob_array)
          std = np.std(prob_array)
          both = np.array([mean,std])
          np.savetxt('/Users/darrelladjei/python/bsc/mesaStuff/SystemSizePlottingData/' + str(size)+'.txt',both)                
extract()
