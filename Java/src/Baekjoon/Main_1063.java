// 1063. 킹
package Baekjoon;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;

public class Main_1063 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");

        int kingC = input[0].charAt(0) - 'A' + 1;
        int kingR = Integer.parseInt(input[0].substring(1));
        int stoneC = input[1].charAt(0) - 'A' + 1;
        int stoneR = Integer.parseInt(input[1].substring(1));
        int N = Integer.parseInt(input[2]);

        HashMap<String, int[]> direction = new HashMap<>();
        direction.put("R", new int[]{0, 1});
        direction.put("L", new int[]{0, -1});
        direction.put("B", new int[]{-1, 0});
        direction.put("T", new int[]{1, 0});
        direction.put("RT", new int[]{1, 1});
        direction.put("LT", new int[]{1, -1});
        direction.put("RB", new int[]{-1, 1});
        direction.put("LB", new int[]{-1, -1});

        for (int i = 0; i < N; i++) {
            int[] dir = direction.get(br.readLine());
            int newKingC = kingC + dir[1];
            int newKingR = kingR + dir[0];

            if (newKingC >= 1 && newKingC <= 8 && newKingR >= 1 && newKingR <= 8) {
                if (newKingC == stoneC && newKingR == stoneR) {
                    int newStoneC = stoneC + dir[1];
                    int newStoneR = stoneR + dir[0];

                    if (newStoneC >= 1 && newStoneC <= 8 && newStoneR >= 1 && newStoneR <= 8) {
                        stoneC = newStoneC;
                        stoneR = newStoneR;
                        kingC = newKingC;
                        kingR = newKingR;
                    }
                } else {
                    kingC = newKingC;
                    kingR = newKingR;
                }
            }
        }
        char kingCChar = (char) (kingC + 'A' - 1);
        char stoneCChar = (char) (stoneC + 'A' - 1);
        System.out.println(kingCChar + "" + kingR);
        System.out.println(stoneCChar + "" + stoneR);
    }
}
