import ReadFile as rd
import Matrix as Matrix
import numpy as np
import os
import operator

def find_v_matrix(d,DIFF):
    N = 501
    v = np.array([[1/501 for i in range(501)]]).T
    matrix = Matrix.getpointmatrix()
    counter = 0
    diff = 0
    while True:
        v_before = v
        v = (1-d)/N + d*np.dot(matrix, v_before)
        if sum(abs(v_before-v)) < DIFF:
            break
    return v, matrix

if __name__ == '__main__':

    ##############  Page Rank list  ##############
    # d_list = [0.25,0.45,0.65,0.85]
    # DIFF_list = [0.1,0.01,0.001]
    # for d in d_list:
    #     for DIFF in DIFF_list:
    #         v ,matrix = find_v_matrix(d, DIFF)
    #         if DIFF == 0.1:
    #             f = open('pr_%i_100.txt'%(d*100), "w")
    #         elif DIFF == 0.01:
    #             f = open('pr_%i_010.txt'%(d*100), "w")
    #         else:
    #             f = open('pr_%i_001.txt'%(d*100), "w")
    #         sorted_index = np.argsort(v.T)[0][::-1]
    #         vote_num = 0
    #         filecontent = ''
    #         for i in sorted_index:
    #             vote_num = np.size(np.nonzero(matrix.T[i]))
    #             filecontent += 'page' + str(i).ljust(6,' ') + str(vote_num).ljust(6,' ') + str(v.T[0][i])[1:9] + '\n'
    #         f.write(filecontent)
    #         f.close()
    ##############  Page Rank list  ##############

    ##############  Reverse index  ##############
    # word_list = []
    # pagewordlist = dict()
    # for i in range(500):
    #     _ ,content = rd.parsefilecontent("./web-search-files2/page%s"%(i))  
    #     pagewordlist[i] = content
    #     word_list = word_list + content
    # # print(word_list)
    # word_list = list(set(word_list))
    # word_list.sort()
    # # print(word_list)
    
    # f = open('reverseindex.txt', 'w')
    # for word in word_list:
    #     filecontent = str(word).ljust(20," ")
    #     for i in range(500):
    #         if word in pagewordlist[i]:
    #             filecontent += 'page' + str(i) + ' '
    #     filecontent += '\n' 
    #     f.write(filecontent)
    # f.close() 
    ##############  Reverse index  ##############
    ##############  Search engine  ##############

    # d_list = [0.25,0.45,0.65,0.85]
    # DIFF_list = [0.1, 0.01, 0.001]
    # target = open('list.txt').read().split('\n')
    # pagewordlist = dict()
    # for i in range(500):
    #     _ ,content = rd.parsefilecontent("./web-search-files2/page%s"%(i))  
    #     # print(content)
    #     pagewordlist[i] = content
    # pagewordlist[500] = ['']
    # for d in d_list:
    #     for DIFF in DIFF_list:
    #         v ,matrix = find_v_matrix(d, DIFF)
    #         sorted_index = np.argsort(v.T)[0][::-1]
    #         if DIFF == 0.1:
    #             f = open('result_%i_100.txt'%(d*100), "w")
    #         elif DIFF == 0.01:
    #             f = open('result_%i_010.txt'%(d*100), "w")
    #         else:
    #             f = open('result_%i_001.txt'%(d*100), "w")
    #         for words in target:
    #             filecontent = ''#'Enter Word: ' + words + '\n'
    #             if ' ' not in words:
    #                 words = words.split(' ')
    #                 counter = 0
    #                 for i in sorted_index:
    #                     if words[0] in pagewordlist[i] and counter < 10:
    #                         filecontent += 'page ' + '%s'%(i) + ' '
    #                         counter += 1
    #                 if 'page' not in filecontent:
    #                     filecontent += 'none'
    #                 filecontent += '\n'
    #                 f.write(filecontent)
    #             else:
    #                 #AND_OR
    #                 filecontent += 'AND ' # (' + words + ') '
    #                 words_split = words.split(' ')
    #                 counter = 0
    #                 for i in sorted_index:
    #                     flag = True
    #                     for word in words_split:
    #                         if word not in pagewordlist[i]: 
    #                             flag = False
    #                             break
    #                     if flag == True and counter < 10:
    #                         filecontent += 'page ' + '%s'%(i) + ' '
    #                         counter += 1    
    #                 if 'page' not in filecontent:
    #                     filecontent += 'none'
    #                 filecontent += '\n'
    #                 filecontent += 'OR ' #+ words + ') '
    #                 counter = 0
    #                 for i in sorted_index:
    #                     for word in words_split:
    #                         if word in pagewordlist[i] and counter < 10:
    #                             filecontent += 'page ' + '%s'%(i) + ' '
    #                             counter += 1    
    #                 filecontent += '\n'
    #                 f.write(filecontent)
    ##############  Search engine  ##############


    
    