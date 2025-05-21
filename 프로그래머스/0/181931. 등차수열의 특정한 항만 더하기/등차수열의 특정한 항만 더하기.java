class Solution {
    public int solution(int a, int d, boolean[] included) {
        int answer = 0;
        int[] intArray = new int[included.length];
        int cnt = 0;
        for(int i = a; cnt < included.length; i += d) {
            intArray[cnt] = i;
            cnt += 1;
        }
        for(int i = 0; i < included.length; i++) {
            if (included[i] == true) {
                answer += intArray[i];
            }
        }
        return answer;
    }
}