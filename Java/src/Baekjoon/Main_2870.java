package Baekjoon;

import java.io.*;
import java.math.BigInteger;
import java.util.*;
import java.util.regex.*;

public class Main_2870 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        List<BigInteger> numbers = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            String input = br.readLine();

            Matcher matcher = Pattern.compile("\\d+").matcher(input);  // 숫자를 찾는 정규 표현식
            while (matcher.find()) {
                String numStr = matcher.group();  // 찾은 숫자 문자열 반환
                BigInteger num = new BigInteger(numStr);
                numbers.add(num);
            }
        }

        Collections.sort(numbers);  // 오름차순 정렬

        for (BigInteger num : numbers) {
            System.out.println(num);
        }
    }
}
