import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class Solution {
  public static void solution(String S) {
    // "We test coders. Give us a try."
    StringBuilder sentence = new StringBuilder();
    ArrayList<String> sentences = new ArrayList<>();
    for(int i = 0; i < S.length(); i++) {
        char currentChar = S.charAt(i);
        if (currentChar != '.' || currentChar != '!' || currentChar != '?') {
          sentence.append(currentChar);
          System.out.println(sentence);
        } else if(currentChar == '.'|| currentChar != '!' || currentChar != '?') {
          continue;
        } else {
          sentences.add(sentence.toString());
        }
    }
  }

  public static int[] solution2(int N) {
    // write your code in Java SE 11
    int[] result = new int[N];
    int x = N;
    int i = 0;

    // if number is odd, add a 0 to the array
    if(N % 2 != 0) {
      result[i] = 0;
      i++;
      while (x > 0 && i < result.length) {
        int q = x/2;
        result[i] = q;
        i++;

        result[i] = -(q);
        i++;

        x = x/2;
      }
    }
    else{
      result[i] = N;
      i++;
      result[i] = -(N);
      i++;
      while(x > 0 && i <result.length) {
        int q = x/2;
        result[i] = q;
        i++;

        result[i] = -(q); // Add the complement to the array
        i++;

        x = x/2;
      }
    }


    for(int num : result) {
      System.out.println(num);
    }
    return result;
  }

  public static void main(String[] args) {
    int[] arr = solution2(7);

//      String s = "We test coders. Give us a try! Hello binh how are you doing?";
//      String[] sentences = s.split("\\?|\\.|\\!");
//      ArrayList<Integer> wordsCount = new ArrayList();
//
//
//      for (String sentence: sentences) {
//        String[] words = sentence.split(" ");
//        int wordCounter = 0;
//
//        for (int i = 0; i < words.length; i++) {
//          String word = words[i];
//          if (word.isEmpty()) {
//            wordCounter -= 1;
//          }
//          //System.out.println(word);
//          wordCounter++;
//        }
//        wordsCount.add(wordCounter);
//        //System.out.println(wordCounter);
//      }
//      int max = Integer.MIN_VALUE;
//      for (int num : wordsCount) {
//        if (num >= max) {
//          max = num;
//        }
//      }
//
//      System.out.println(max);

      //solution(s);
//    File file = new File("test.txt");
//    Scanner sc = null;
//    try {
//      sc = new Scanner(file);
//    } catch (FileNotFoundException e) {
//      e.printStackTrace();
//    }
//
//    while (sc.hasNextLine())
//    System.out.println(sc.nextLine());
  }  
}
