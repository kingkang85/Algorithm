package Baekjoon.TwoPointer;

import java.io.*;
import java.util.*;

public class Main_1253 {
    static int[] nums;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        nums = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(nums);

        int result = 0;
        for (int i = 0; i < N; i++) {
            int target = nums[i];
            int left = 0;
            int right = N - 1;

            while (left < right) {
                // 자기 자신은 제외
                if (left == i) {
                    left++;
                    continue;
                }

                if (right == i) {
                    right--;
                    continue;
                }

                int sum = nums[left] + nums[right];

                if (sum == target) {
                    result++;
                    break;
                } else if (sum < target) {
                    left++;
                } else {
                    right--;
                }
            }
        }

        System.out.println(result);
    }
}
