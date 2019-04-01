from scipy import stats
import numpy as np
arrEasy=np.array([[0,2],[2.5,4],[5,6],[7.5,9],[10,13],
                  [12.5,16],[15,19],[17.5,23],[20,27],
                    [22.5,31],[25,35],[27.5,40],[30,53],
                  [32.5,68],[35,90],[37.5,110],[40,130],
                    [42.5,148],[45,165],[47.5,182],[50,195],
                  [52.5,208],[55,217],[57.5,226],[60,334],
                   [62.5,342],[65,349],[67.5,500],[70,511],
                  [72.5,300],[75,200],[77.5,80],[80,20]])
arrDiff=np.array([[0,20],[2.5,30],[5,45],[7.5,70],[10,100],[12.5,135],[15,170],[17.5,205],[20,226],
                    [22.5,241],[25,251],[27.5,255],[30,256],[32.5,253],[35,249],[37.5,242],[40,234],
                    [42.5,226],[45,217],[47.5,208],[50,195],[52.5,182],[55,165],[57.5,148],[60,130],
                   [62.5,110],[65,40],[67.5,30],[70,20],[72.5,5],[75,5],[77.5,0],[80,0]])

def createScore(arr):
    score = []          #所有学员分数
    row = arr.shape[0]
    for i in np.arange(0,row):
        for j in np.arange(0,int(arr[i][1])):
            score.append(arr[i][1])
    score = np.array(score)
    return score

def calStatValue(score):
    #集中趋势度量
    print('均值')
    print(np.mean(score))
    print('中位数')
    print(np.median(score))
    print('众数')
    print(stats.mode(score)[0])
    #离散趋势度量
    print('极差')
    print(np.ptp(score))
    print('方差')
    print(np.var(score))
    print('标准差')
    print(np.std(score))
    print('变异系数')
    print(np.mean(score)/np.std(score))
    #偏度与峰度的度量
    print('偏度')
    print(stats.skew(score))
    print('峰度')
    print(stats.kurtosis(score))

score1=createScore(arrEasy)
score2=createScore(arrDiff)

calStatValue(score1)
calStatValue(score2)