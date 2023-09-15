

import java.util.ArrayList;

import static java.util.Collections.max;

class Solution {
    public int solution(int[][] sizes) {
        ArrayList<Integer> big = new ArrayList<Integer>();
        ArrayList<Integer> small = new ArrayList<Integer>();
        int answer = 1;
        for (int i =0; i< sizes.length; i++)
        {
            if (sizes[i][0] > sizes[i][1])
            {
                big.add(sizes[i][0]);
                small.add(sizes[i][1]);
            }
            else
            {
                big.add(sizes[i][1]);
                small.add(sizes[i][0]);
            }
        }
        answer = max(big) * max(small);
        return answer;
    }
}