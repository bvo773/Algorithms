public class Main {
    public static boolean isPalindrome(int x) {
        // 121  -> 121
        if (x < 0){return false;}
    
        // Convert x to string
        String numS = String.valueOf(x);
        
        // Reverse the string
        StringBuilder reverseS = new StringBuilder();
        for (int i = numS.length()-1; i >= 0; i--) {
            char num = numS.charAt(i);
            reverseS.append(num);
        }

        // Convert reverse string to num
        long num = Long.parseLong(reverseS.toString());

        if (num == x) {
            return true;
        }
        else {return false;}

    }

    

    public static void main(String[] args) {
        System.out.println(isPalindrome(-101));
    }



}
