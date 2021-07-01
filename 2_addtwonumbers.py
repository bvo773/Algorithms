class ListNode(object):
    def __init__(self, val=0,next = None):
        self.val = val
        self.next = next

def main():

    
    node1 = ListNode(val=1)
    node2 = ListNode(val=2)
    node3 = ListNode(val=3) 

    node1.next = node2
    node2.next = node3
    
    
    
    # while (curr != None):
    #     print('val:{} node:{}'.format(curr.val,curr.next))
    #     curr = curr.next
    curr = node1
    length = 0
    while (curr != None):
        length += 1
        curr = curr.next
    
    curr = node1
    list1 = [None]*length
    i =  length - 1
    while (curr != None):
        list1[i] = curr.val
        i -= 1
        curr = curr.next
        print(list1)

    strnum = ''
    for num in list1:
        strnum += str(num)
    
    print (strnum)


    




    # print('node1 val:{} next:{} | node2:{}'.format(node1.val,node1.next,node2))

    return 
if __name__ == '__main__':
    main()
