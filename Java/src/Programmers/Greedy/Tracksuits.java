package Programmers.Greedy;

public class Tracksuits {
    public int tracksuits(int n, int[] lost, int[] reserve) {
        int[] students = new int[n+2];
        int answer = n;

        for (int l : lost) students[l]--;
        for (int r : reserve) students[r]++;

        for (int i = 1; i <= n; i++) {
            if (students[i] == -1) {
                if (students[i-1] == 1) {
                    students[i]++;
                    students[i-1]--;
                } else if (students[i+1] == 1) {
                    students[i]++;
                    students[i+1]--;
                } else {
                    answer--;
                }
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        Tracksuits c = new Tracksuits();
        System.out.println(c.tracksuits(5, new int[]{2, 4}, new int[]{1, 3, 5}));
    }
}
