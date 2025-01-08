// 2525. 오븐 시계
package Baekjoon;

import java.io.*;

public class Main_2525 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] now = br.readLine().split(" ");
        int hour = Integer.parseInt(now[0]);
        int min = Integer.parseInt(now[1]);
        int need = Integer.parseInt(br.readLine());

        int endHour, endMin;
        if (min + need < 60) {
            endHour = hour;
            endMin = min + need;
        } else {
            endHour = hour + (min + need) / 60;
            if (endHour >= 24) {
                endHour -= 24;
            }
            endMin = (min + need) % 60;
        }

        System.out.println(endHour + " " + endMin);
    }
}
