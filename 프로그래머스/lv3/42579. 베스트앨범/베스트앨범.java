import java.util.*;

class Solution {
    public int[] solution(String[] genres, int[] plays) 
    {
        // genre당 누적 play
        HashMap<String, Integer> map = new HashMap<>();
        for (int i = 0; i < genres.length; i++)
        {
        	map.put(genres[i], map.getOrDefault(genres[i], 0) + plays[i]);
        }
        
        // key 값만 가져와서 genre에 넣기
        ArrayList<String> genre = new ArrayList<>();
        for (String key : map.keySet())
        {
        	genre.add(key);
        }
        
        // key 값에 해당하는 value를 내림차순으로 정렬, 람다 함수 사용
        Collections.sort(genre, (o1, o2) -> map.get(o2) - map.get(o1));
        
        ArrayList<Integer> list = new ArrayList<>();
        for (int i = 0; i < genre.size(); i++)
        {
        	// g -> "classic", "pop"
        	String g = genre.get(i);
        	// g에 해당하는 장르에서 play횟수가 가장 큰 인덱스 찾기
        	int max = 0;
        	int firstldx = -1;
        	for (int j = 0; j < genres.length; j++)
        	{
        		if(g.equals(genres[j]) && max < plays[j])
        		{
        			max = plays[j];
        			firstldx = j;
        		}
        	}
        	// g에 해당하는 장르에서 play횟수가 두 번쨰로 큰 인덱스 찾기
        	max = 0;
        	int secondldx = -1;
        	for (int j = 0; j < genres.length; j++)
        	{
        		if(g.equals(genres[j]) && max < plays[j] && j != firstldx)
        		{
        			max = plays[j];
        			secondldx = j;
        		}
        	}
        	list.add(firstldx);
        	if(secondldx >= 0)
        	{
        	    list.add(secondldx);
        	}
        }
       	int[] result = new int[list.size()];
    	for (int k = 0; k < list.size(); k++)
    	{
    		result[k] = list.get(k);
    	}
        return result;
    }	
}