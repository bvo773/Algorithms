import java.util.List;

public class Main {

    public static void main(String args[]) {
        System.out.println("Hello World");
            //21 -> 12
        ListNode node2 = new ListNode(2);
        ListNode node1 = new ListNode(1);
        
        node2.next = node1;
        ListNode L1 = node2;

        //43 -> 34
        ListNode node4 = new ListNode(4);
        ListNode node3 = new ListNode(3);

        node4.next = node3;
        ListNode L2  = node4;

        
        int[] arr2 = putNodeValueToArray(getListNodeLength(L2), L2);
        //System.out.println(arrayToInteger(arr2));

        int[] arr1 = putNodeValueToArray(getListNodeLength(L1), L1);

        int x = arrayToInteger(arr1);
        int y = arrayToInteger(arr2); 

        int z = x + y;
        String zS = Integer.toString(z);
        
        System.out.println(z);
        System.out.println();
        ListNode answer = putValueIntoNode(zS);

        System.out.println();
        //printListtNode(answer);

    }
    public static ListNode putValueIntoNode(String s) {
        ListNode curr = new ListNode();
        
        for(int i = s.length()-1; i >= 0; i--) {
        
            //System.out.println(s.charAt(0));
            //System.out.println(s.charAt(1));
            int val = Character.getNumericValue(s.charAt(i));
            ListNode node = new ListNode(val);
            while (curr)

        
            //System.out.println(val);
         
        }
        return curr;
    }

    public static void printListtNode(ListNode listNode) {
        ListNode curr = listNode;
        while (curr != null) {
            System.out.println("NodeAdd: " + listNode.next);
            System.out.println("Value: " + listNode.val);
            curr = curr.next;
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

    public static int[] putNodeValueToArray(int length, ListNode listNode) {
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


