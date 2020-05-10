import java.io.*;
import java.util.*;
public class Day02_1{
	public static void main(String[] args) throws IOException{
		BufferedReader f = new BufferedReader(new FileReader("input.txt"));
		StringTokenizer st;
		ArrayList<String> soFar=new ArrayList<String>();
		for(int i=0; i<250; i++) {
			st=new StringTokenizer(f.readLine());
			String s=st.nextToken();
			for(int j=0; j<i; j++) {
				int count=0;
				for(int k=0; k<s.length(); k++) {
					if(soFar.get(j).charAt(k)!=s.charAt(k))
						count++;
				}
				if(count<=1) {
					int k;
					for(k=0; k<s.length(); k++) {
						if(soFar.get(j).charAt(k)!=s.charAt(k))
							break;
					}
					System.out.println(s.substring(0, k)+s.substring(k+1));
				}
			}
			soFar.add(s);
		}
	}
}