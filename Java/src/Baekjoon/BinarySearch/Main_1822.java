package Baekjoon.BinarySearch;

import java.io.*;
import java.util.*;

public class Main_1822 {
    static int[] B;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int na = Integer.parseInt(st.nextToken());
        int nb = Integer.parseInt(st.nextToken());

        int[] A = new int[na];
        B = new int[nb];

        // A 집합 저장
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < na; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(A);

        // B 집합 저장
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < nb; i++) {
            B[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(B);

        int count = 0;
        StringBuilder sb = new StringBuilder();

        // A의 각 원소가 B에 속하는지 확인
        for (int a : A) {
            if (!hasElement(a)) {
                count++;
                sb.append(a).append(' ');
            }
        }

        System.out.println(count);
        if (count > 0) {
            System.out.println(sb.toString().trim());
        }
    }

    static boolean hasElement(int element) {
        int left = 0;
        int right = B.length - 1;

        while (left <= right) {
            int mid = (left + right) / 2;

            if (B[mid] == element) {
                return true;
            } else if (B[mid] < element) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return false;
    }
}
