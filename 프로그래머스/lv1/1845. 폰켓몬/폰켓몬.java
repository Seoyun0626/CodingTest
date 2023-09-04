import java.util.HashMap;

// 1. HashMap을 사용해서 포켓몬 종류(key)와 종류에 따른 값(value)을 저장하자
// put -> key:value값 저장, get -> key이용하여 value값 return
public class Solution {
	public int solution(int[] nums)
	{
		HashMap<Integer, Integer> map = new HashMap<>();
		for (int i = 0; i < nums.length; i++)
		{
			if (map.containsKey(nums[i]))
				map.put(nums[i], map.get(nums[i]) + 1);
			else
				map.put(nums[i], 1);
		}
		if (map.size() >= (nums.length / 2))
			return (nums.length / 2);
		else
			return map.size();
	}

}
