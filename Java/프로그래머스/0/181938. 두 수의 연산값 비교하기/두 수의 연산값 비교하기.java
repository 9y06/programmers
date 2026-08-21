class Solution {
    public int solution(int a, int b) {
        String ab = String.valueOf(a) + String.valueOf(b);
        
        if (Integer.parseInt(ab) < (2 * a * b)) {
            return 2* a*b;
        } else {
            return Integer.parseInt(ab);
        }
    }
}