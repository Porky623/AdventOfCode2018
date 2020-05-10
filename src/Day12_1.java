import java.io.*;
import java.util.*;
public class Day12_1{
	public static void main(String[] args) throws IOException{
		BufferedReader f=new BufferedReader(new FileReader("input.txt"));
		String initial="###.#..#..##.##.###.#.....#.#.###.#.####....#.##..#.#.#..#....##..#.##...#.###.#.#..#..####.#.##.#";
		String next=f.readLine();
		boolean[] plants=new boolean[2000000];
		int zero=400;
		for(int i=zero; i<zero+initial.length(); i++) {
			if(initial.charAt(i-zero)=='#')
				plants[i]=true;
			else
				plants[i]=false;
		}
		HashMap<String,Character> map=new HashMap<String,Character>();
		while(next!=null) {
			String[] input=next.split(" ");
			map.put(input[0], '#');
			next=f.readLine();
		}
		int leftMost=zero;
		int rightMost=zero+97;
		for(int i=0; i<500; i++) {
			boolean[] temp=new boolean[plants.length];
			for(int j=leftMost-3; j<=rightMost-1; j++) {
				StringBuilder s=new StringBuilder();
				for(int k=0; k<5; k++) {
					if(plants[j+k])
						s.append('#');
					else
						s.append('.');
				}
				if(map.containsKey(s.toString())) {
					temp[j+2]=true;
				}
			}
			plants=temp;
			loop:
			for(int j=leftMost-3; j<1000; j++) {
				if(plants[j]) {
					leftMost=j;
					break loop;
				}
			}
			loop:
			for(int j=rightMost+3; j>=0; j--) {
				if(plants[j]) {
					rightMost=j;
					break loop;
				}
			}
			int count=0;
			for(int ij=leftMost; ij<=rightMost; ij++) {
				if(plants[ij])
					count+=ij-zero;
			}
			System.out.println(count);
		}
	}
}