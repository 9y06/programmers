class Solution {
    public String solution(String str1, String str2) {
        String answer = "";
        
        char[] arr1 = new char[str1.length()];
        char[] arr2 = new char[str2.length()];

        for (int i = 0; i < str1.length(); i++) {
            arr1[i] = str1.charAt(i);
        }
        for (int i = 0; i < str2.length(); i++) {
            arr2[i] = str2.charAt(i);
        }
                
        for (int i = 0; i < arr1.length; i++) {
                answer += arr1[i];
                answer += arr2[i];
        }
        return answer.toString();
    }
}