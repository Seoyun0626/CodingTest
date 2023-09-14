

import java.util.*;
class Solution {
    public int[] solution(int[] array, int[][] commands)
    {
        int[] answer = new int[commands.length];
        // array배열을 자른 list
        ArrayList<Integer> list = new ArrayList<Integer>();

        for (int i = 0; i < commands.length; i++)
        {
            // array 숫자 배열 자르기
            for (int j = commands[i][0]; j <= commands[i][1]; j++)
            {
                list.add(array[j-1]);
            }
            // 오름차순 정렬
            Collections.sort(list);
            answer[i] = list.get(commands[i][2] - 1);
            list.clear();
        }
        return answer;
    }
}