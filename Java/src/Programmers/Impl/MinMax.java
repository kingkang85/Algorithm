package Programmers.Impl;

// Lv2. 최댓값과 최솟값
public class MinMax {
    public static String minMax(String s) {
        String[] numbers = s.split(" ");

        int minValue = Integer.parseInt(numbers[0]);
        int maxValue = Integer.parseInt(numbers[0]);

        for (String number : numbers) {
            if (Integer.parseInt(number) < minValue) {
                minValue = Integer.parseInt(number);
            }

            if (Integer.parseInt(number) > maxValue) {
                maxValue = Integer.parseInt(number);
            }
        }

        return minValue + " " + maxValue;
    }

    public static void main(String[] args) {
        System.out.println(minMax("-1 -2 -3 -4"));
    }
}
