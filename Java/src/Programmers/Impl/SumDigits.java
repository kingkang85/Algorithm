package Programmers.Impl;

// Lv1. 자릿수 더하기
public class SumDigits {
    public int sum(int n) {
        int answer = 0;

        String[] nums = String.valueOf(n).split("");
        for (String num : nums) {
            answer += Integer.parseInt(num);
        }

        return answer;
    }

    public static void main(String[] args) {
        SumDigits c = new SumDigits();
        System.out.println(c.sum(123));
    }
}
