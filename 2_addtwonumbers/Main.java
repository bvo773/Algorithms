import java.util.List;

public class Main {

    public static void main(String args[]) {
        System.out.println("Hello World");

        // 243
        ListNode node2 = new ListNode(2);
        ListNode node1 = new ListNode(4);
        ListNode node3 = new ListNode(3);
        
        node2.next = node1;
        node1.next = node3;
        ListNode L1 = node2;

        // 564
        ListNode node4 = new ListNode(5);
        ListNode node5 = new ListNode(6);
        ListNode node6 = new ListNode(4);

        node4.next = node5;
        node5.next = node6;
        ListNode L2  = node4;

        
        int[] arr2 = putReverseNodeValueToArray(getListNodeLength(L2), L2);
        int[] arr1 = putReverseNodeValueToArray(getListNodeLength(L1), L1);

        int x = arrayToInteger(arr1);
        int y = arrayToInteger(arr2); 

        int z = x + y;
        String zS = Integer.toString(z);
        
        System.out.println(zS);
        System.out.println();
        

        System.out.println();
        printListtNode(putValueIntoNode(zS));



    }


    public static ListNode putValueIntoNode(String s) {
        ListNode listNode = new ListNode();

         for(int i = s.length()-1; i >= 0; i--) {
             if (listNode.next == null && listNode.val == 0 ) {
                 int val = Character.getNumericValue(s.charAt(i));
                 ListNode firstNode = new ListNode(val);
                 listNode = firstNode;
             }
             else {
                 ListNode curr = listNode;
                 while (curr != null) {
                    if (curr.next == null) {
                        int val = Character.getNumericValue(s.charAt(i));
                        curr.next = new ListNode(val);
                        break;
                    }
                    else{
                        curr = curr.next;
                    }
                 }
             }
         }
        return listNode;
    }

    public static void printListtNode(ListNode listNode) {
        ListNode curr = listNode;
        while (curr != null) {
            System.out.println("Node Address: " + curr);
            System.out.println("Node Value: "  + curr.val);
            System.out.println("Next Node Addresss:  " + curr.next);
            curr = curr.next;
            System.out.println();
        }
        
    
    }
    public static int getListNodeLength(ListNode listNode) {
        ListNode curr = listNode;
        int length = 0;
        while (curr != null) {
            length+=1;
            curr = curr.next;
        }
        return length;
    }

    public static int[] putReverseNodeValueToArray(int length, ListNode listNode) {
        ListNode curr = listNode;
        int[] arr = new int[length];
        while (curr != null) {
            arr[length-1] = curr.val;
            curr = curr.next;
            length -= 1;
        }
        return arr;
    }

    public static int arrayToInteger(int[] arr){
        StringBuilder s = new StringBuilder();
        for (int i : arr) {
            s.append(i);
        }
        return Integer.parseInt(s.toString());
    }

}

class ListNode {
    int val;
    ListNode next;

    public ListNode(){}
    public ListNode(int val) {this.val = val;}
    public ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}


