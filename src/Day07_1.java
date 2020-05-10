import java.io.*;
import java.util.*;
public class Day07_1{
	public static void main(String[] args) throws IOException{
		BufferedReader f=new BufferedReader(new FileReader("input.txt"));
		String next=f.readLine();
		boolean[] canDo=new boolean[26];
		int canDoCount=26;
		HashMap<Character,HashSet<Character>> map=new HashMap<>();
		for(int i=0; i<26; i++) {
			canDo[i]=true;
			map.put((char)(i+'A'), new HashSet<Character>());
		}
		while(next!=null) {
			String[] input=next.trim().split(" ");
			if(canDo[input[7].charAt(0)-'A'])
				canDoCount--;
			canDo[input[7].charAt(0)-'A']=false;
			map.get(input[7].charAt(0)).add(input[1].charAt(0));
			next=f.readLine();
		}
		int notWorking=5;
		Queue<Integer> endTimes=new PriorityQueue<Integer>();
		for(int i=0; i<5; i++) {
			endTimes.add(0);
		}
		boolean[] used=new boolean[26];
		String soFar="";
		int lastTime=0;
		while(!endTimes.isEmpty()) {
			int t=endTimes.poll();
			lastTime=t;
			notWorking++;
			while(!endTimes.isEmpty()&&endTimes.peek()==t&&notWorking<5) {
				endTimes.poll();
				notWorking++;
			}
			int i;
			for(i=0; i<notWorking; i++) {
				int j;
				loop:
				for(j=0; j<26; j++) {
					if(canDo[j]) {
						break loop;
					}
				}
				if(j==26) {
					break;
				}
				System.out.println((char)(j+'A'));
				canDoCount--;
				notWorking--;
				canDo[j]=false;
				used[j]=true;
				int endTime=t+61+j;
				endTimes.add(endTime);
				
			}
			loop2:
			for(int k=0; k<26; k++) {
				if(used[k])
					continue loop2;
				char c=(char)(k+'A');
				for(Character c2:map.get(c)) {
					if(!used[c2-'A'])
						continue loop2;
				}
				canDo[k]=true;
				canDoCount++;
			}
		}
		System.out.println(lastTime);
//		boolean cont=true;
//		loop:
//		while(cont) {
//			for(int i=0; i<26; i++) {
//				if(canDo[i]) {
//					soFar+=(char)(i+'A');
//					used[i]=true;
//					canDo[i]=false;
//					loop2:
//					for(int j=0; j<26; j++) {
//						if(used[j])
//							continue loop2;
//						char c=(char)(j+'A');
//						for(Character c2:map.get(c)) {
//							if(!used[c2-'A'])
//								continue loop2;
//						}
//						canDo[j]=true;
//					}
//					continue loop;
//				}
//			}
//			cont=false;
//		}
//		System.out.println(soFar);
	}
}