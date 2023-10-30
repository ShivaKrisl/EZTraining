import java.util.*;

public class ProblemSolution {
    public void solution(String s1, String s2) {
        ArrayList<Integer> res = new ArrayList<>();
        //write your code here
        if(s1.length()>=s2.length())
        {
            for(int i=0;i<s1.length();i++)
            {
                if(s1.charAt(i)==s2.charAt(0))
                {
                    int pos = i;
                    int j=0;
                    while(pos<s1.length()&&j<s2.length() && s2.charAt(j)==s1.charAt(pos))
                    {
                        j++;
                        pos++;
                    }
                    if(j==s2.length())
                    {
                        res.add(i);
                    }
                }
            }
        }
        else
        {
            for(int i=0;i<s2.length();i++)
            {
                if(s2.charAt(i)==s1.charAt(0))
                {
                    int pos = i;
                    int j=0;
                    while(pos<s2.length()&&j<s1.length() && s1.charAt(j)==s2.charAt(pos))
                    {
                        j++;
                        pos++;
                    }
                    if(j==s1.length())
                        res.add(i);
                }
            }
        }
        if(res.size()>=1)
        {for(Integer i:res)
        {
            System.out.println(i);
        }}
        else
        {
            System.out.println(-1);
        }
    }
}
