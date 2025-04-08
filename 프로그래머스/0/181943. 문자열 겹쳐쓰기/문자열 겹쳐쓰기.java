class Solution {
    public String solution(String my_string, String overwrite_string, int s) {
        // 앞 부분 + 덮어쓰기할 부분 + 남은 뒷 부분
        String answer = my_string.substring(0, s)
                        + overwrite_string 
                        + my_string.substring(s + overwrite_string.length());
        return answer;
    }
    public static void main(String[] args){
        Solution sol = new Solution();
        System.out.println(sol.solution("He11oWor1d", "lloWorl", 2));
        System.out.println(sol.solution("Program29b8UYP", "merS123", 7)); 
    }
}