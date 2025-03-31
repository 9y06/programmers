import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        
        char[] ch = str.toCharArray();
        for (char c: ch) {
	    if (Character.isUpperCase(c)) {
		    c = Character.toLowerCase(c);
	    } else {
		    c = Character.toUpperCase(c);
	    }
	    System.out.print(c);
        }
    }
}