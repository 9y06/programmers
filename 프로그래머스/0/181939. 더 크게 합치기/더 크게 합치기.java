class Solution {
    public int solution(int a, int b) {
        String ab = String.valueOf(a) + String.valueOf(b);
        String ba = String.valueOf(b) + String.valueOf(a);
        
        if (Integer.parseInt(ab) < Integer.parseInt(ba)) {
            return Integer.parseInt(ba);
        } else {
            return Integer.parseInt(ab);
        }
    }
}