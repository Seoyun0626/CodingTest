import java.util.*;
public class Solution {
	public boolean solution(String[] phone_book)
	{
		boolean answer = true;
		HashSet<String> set = new HashSet<>();
		for (int i = 0; i < phone_book.length; i++)
		{
			set.add(phone_book[i]);
		}
		for (String phone : phone_book)
		{
			for (int j = 1; j < phone.length(); j++)
			{
				if(set.contains(phone.subSequence(0, j)))
					answer = false;
			}
		}
		return answer;
	}
}