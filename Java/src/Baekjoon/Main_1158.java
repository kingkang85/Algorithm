// 1158. 요세푸스 문제
package Baekjoon;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Queue;
import java.util.LinkedList;

public class Main_1158 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int N = Integer.parseInt(input[0]);
        int K = Integer.parseInt(input[1]);

        Queue<Integer> q = new LinkedList<>();
        // Queue q = new LinkedList();
        for (int i = 1; i < N + 1; i++) {
            q.offer(i);
            // q.add(i);
        }

        StringBuilder result = new StringBuilder("<");
        while (q.size() > 1) {
            // q 앞에서 K - 1번 뽑아서 뒤에 붙이기
            for (int i = 0; i < K - 1; i++) {
                q.offer(q.poll());
                // q.offer(q.remove());
            }
            result.append(q.poll()).append(", ");
        }
        result.append(q.poll()).append(">");

        System.out.println(result);
    }
}
