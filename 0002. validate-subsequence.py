#o(n) time | o(1) space
def validateSubsequence(array,sequence):
    aindex=0
    sindex=0
    while aindex<len(array) and sindex<len(sequence):
        if array[aindex]==sequence[sindex]:
            sindex+=1
        aindex+=1
    return sindex==len(sequence)
array=[1,2,3,4,5,6,7,8,9]
sequence=[2,4,6,8]
print(validateSubsequence(array,sequence))
                
