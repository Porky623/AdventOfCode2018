import java.io.*;
import java.util.*;
public class Day01_1{
	public static void main(String[] args) throws IOException{
		int val=0;
		HashSet<Integer> seen=new HashSet<Integer>();
		while(true) {
			BufferedReader f = new BufferedReader(new FileReader("input.txt"));
			String next=f.readLine();
			StringTokenizer st;
			seen.add(0);
			while(next!=null) {
				st = new StringTokenizer(next);
				String s = st.nextToken();
				int x=Integer.parseInt(s.substring(1));
				if(s.charAt(0)=='-')
					x*=-1;
				val+=x;
				if(seen.contains(val)) {
					System.out.println(""+val);
					System.exit(0);
				}
				seen.add(val);
				next=f.readLine();
			}
		}
	}
}