package Programmers.TwoPointer;

// Lv2. 연속된 부분 수열의 합
public class SumSequence {
    public static int[] sumSequence(int[] sequence, int k) {
        int left = 0, right = 0, sum = 0;
        int minLength = Integer.MAX_VALUE;
        int[] answer = new int[2];

        while (right < sequence.length) {
            sum += sequence[right];

            while (sum > k) {
                sum -= sequence[left++];
            }

            if (sum == k) {
                if ((right - left) < minLength) {
                    minLength = right - left;
                    answer[0] = left;
                    answer[1] = right;
                }
            }

            right++;
        }

        return answer;
    }

    public static void main(String[] args) {
        System.out.println(sumSequence(new int[]{1, 2, 3, 4, 5}, 7));
    }
}
