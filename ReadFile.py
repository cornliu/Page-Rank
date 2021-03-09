def parsefilecontent(filename):
    content = open(filename).read().split('\n')
    for i in range(0,len(content)-2):
        content[i] = content[i][4:]
    vote = content[0:-3]
    pagecontent = content[-2].split(' ')[:-1]
    return vote, pagecontent  #list, list
def readsearchlist(filename):
    content = open(filename).read().split('\n')
    # print(content)



    
