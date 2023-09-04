

import java.util.HashMap;
import java.util.*;
// 1. participant 배열 이용해서 HashMap에 넣기
// 2. completion 배열 이용해서 HashMap에서 지워나가기
// 3. 마지막 남은 HashMap에서 Key값 출력하기
public class Solution {
	public String solution(String[] participant, String[] completion)
	{
		String answer = "";
		HashMap<String, Integer> map = new HashMap<>();
		for (int i = 0; i < participant.length; i++)
		{
			if (map.containsKey(participant[i]))
				map.put(participant[i], map.get(participant[i]) + 1);
			else
				map.put(participant[i], 1);
		}
		for (int j = 0; j < completion.length; j++)
		{
			map.put(completion[j], map.get(completion[j]) - 1);
		}
		for (Map.Entry<String, Integer> entry : map.entrySet())
		{
			if(entry.getValue() != 0)
			{
				answer = entry.getKey();
			}
		}
		return answer;
	}
}
