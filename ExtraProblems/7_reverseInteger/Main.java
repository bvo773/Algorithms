public class Main{
    // constraints -(2^31) <= x <= 2^31 - 1
    public static int reverse(int x) {
        boolean isNeg;
        if (x < 0) {
            isNeg = true;
        }
        else {
            isNeg = false; 
        }

        // convert integer to string
        String numS = String.valueOf(x);
        StringBuilder reverseS = new StringBuilder();
        if (!isNeg) {
            // reverse the string 
            for (int i = numS.length()-1; i >= 0; i--) {
                char num = numS.charAt(i);
                reverseS.append(num);
            }
        }
        else{
        // reverse the string if negative
            for (int i = numS.length()-1; i >= 1; i--) {
                char num = numS.charAt(i);
                reverseS.append(num);
            }
        }


        // convert it back to int
        int reverseN;
        if (isNeg) {
            reverseN = Integer.parseInt(reverseS.toString());
            reverseN = reverseN * -1;
        }
        else {
            reverseN = Integer.parseInt(reverseS.toString());
        }
        
        // check if int is between the contraints
        int leftConstraint = (int) (Math.pow(-2, 31));
        int rightConstrant = (int) (Math.pow(2,31) - 1); 
        if ((leftConstraint <= reverseN) && (reverseN <=rightConstrant)) {
            return reverseN;
        }else {
            return 0;
        }

    }
    public static void main(String[] args) {
        System.out.println(reverse(-7887778));

       
    }
}