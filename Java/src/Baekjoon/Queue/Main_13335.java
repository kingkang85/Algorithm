package Baekjoon.Queue;

import java.io.*;
import java.util.*;

public class Main_13335 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int w = Integer.parseInt(st.nextToken());
        int L = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        Queue<Integer> trucks = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            trucks.offer(Integer.parseInt(st.nextToken()));
        }

        Queue<Integer> bridge = new LinkedList<>();
        for (int i = 0; i < w; i++) {
            bridge.offer(0);
        }

        int time = 0;
        int bridgeWeight = 0;

        while (!trucks.isEmpty() || bridgeWeight > 0) {
            time++;
            bridgeWeight -= bridge.poll();

            if (!trucks.isEmpty() && bridgeWeight + trucks.peek() <= L) {
                int truck = trucks.poll();
                bridge.offer(truck);
                bridgeWeight += truck;
            } else {
                bridge.offer(0);
            }
        }

        System.out.println(time);
    }
}
