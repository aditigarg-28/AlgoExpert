#Average: o(nlogn) time | o(nlogn) space
#Worst: o(n) time | o(n) space
def closestValueInBST(tree,target):
    return findClosest(tree,target,float("inf"))

def findClosest(tree,target,closest):
    if tree is none:
        return closest
    if abs(target-closest)>abs(target-tree.value):
        closest=tree.value
    if target<tree.value:
        return findClosest(tree.left,target,closest)
    elif target>tree.value:
        return findClosest(tree.right,target,closest)
    else:
        return closest



#Average: o(nlogn) time | o(1) space
#Worst: o(n) time | o(1) space
def closestValueInBST(tree,target):
    return findClosest(tree,target,float("inf"))

def findClosest(tree,target,closest):
    curr=tree
    while curr is not None:
        if abs(target-closest)>abs(target-curr.value):
            closest=curr.value
        if target<curr.value:
            curr=curr.left
        elif target>curr.value:
            curr=curr.right
        else:
            break
    return closest

