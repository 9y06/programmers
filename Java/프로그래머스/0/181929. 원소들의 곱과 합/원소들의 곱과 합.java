import java.util.Arrays;

class Solution {
    public int solution(int[] num_list) {
        int multi_sum = 1;
        for (int i = 0; i < num_list.length; i++) {
            multi_sum *= num_list[i];
        }

        int plus_sum = Arrays.stream(num_list).sum();

        if (multi_sum < Math.pow(plus_sum, 2)) {
            return 1;
        } else {
            return 0;
        }
    }
}
