import ReadFile as rd
import numpy as np
def getpointmatrix():
    a = np.array([[0 for i in range(501)]],dtype=float).T
    for i in range(500):
        vote ,content = rd.parsefilecontent("./web-search-files2/page%s"%(i))
        if len(vote) == 0:
            value = 0
        else: value = 1/len(vote)
        column = np.array([[0 for i in range(501)]],dtype=float)
        for i in vote:
            column[0][int(i)] = value
        a = np.concatenate((a,column.T),axis=1)
    a = np.delete(a,0,axis=1)
    a = np.concatenate((a,np.array([[0 for i in range(501)]]).T),axis=1)
    return a

