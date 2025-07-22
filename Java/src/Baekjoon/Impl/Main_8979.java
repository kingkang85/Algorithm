package Baekjoon.Impl;

import java.io.*;
import java.util.*;

/**
 * 8979. 올림픽
 *
 * 1. 각 국가의 금,은,동메달 수 저장
 * 2. K보다 더 잘한 나라 수 + 1
 */
public class Main_8979 {
    static class Country {
        int id, gold, silver, bronze;

        Country(int id, int gold, int silver, int bronze) {
            this.id = id;
            this.gold = gold;
            this.silver = silver;
            this.bronze = bronze;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        // 메달 정보 저장
        Country[] countries = new Country[N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int id = Integer.parseInt(st.nextToken());
            int gold = Integer.parseInt(st.nextToken());
            int silver = Integer.parseInt(st.nextToken());
            int bronze = Integer.parseInt(st.nextToken());
            countries[i] = new Country(id, gold, silver, bronze);
        }

        // K번 국가 찾기
        Country targetCountry = null;
        for (Country country : countries) {
            if (country.id == K) {
                targetCountry = country;
                break;
            }
        }

        int rank = 0;
        for (Country country : countries) {
            if (country.id != K && isBetter(country, targetCountry)) {
                rank++;
            }
        }

        System.out.println(rank+1);
    }

    static boolean isBetter(Country a, Country b) {
        if (a.gold != b.gold) return a.gold > b.gold;
        if (a.silver != b.silver) return a.silver > b.silver;
        return a.bronze > b.bronze;
    }
}
