import java.io.*;
import java.util.*;
import java.awt.*;
public class Day03_1{
	public static void main(String[] args) throws IOException{
		BufferedReader f = new BufferedReader(new FileReader("input.txt"));
		String next=f.readLine();
		int[][] sections=new int[1349][];
		int thicc=0;
//		HashSet<Integer> done=new HashSet<Integer>();
		while(next!=null){
			StringTokenizer st=new StringTokenizer(next);
			int ID=Integer.parseInt(st.nextToken().substring(1));
			st.nextToken();
			StringTokenizer st2=new StringTokenizer(st.nextToken(),",");
			int r1=Integer.parseInt(st2.nextToken());
			String s=st2.nextToken();
			int c1=Integer.parseInt(s.substring(0, s.length()-1));
			st2=new StringTokenizer(st.nextToken(),"x");
			int gapR=Integer.parseInt(st2.nextToken());
			int gapC=Integer.parseInt(st2.nextToken());
			sections[ID-1]=new int[] {ID,r1,c1,gapR,gapC};
//			for(int i=0;i<gapR;i++) {
//				l1:
//				for(int j=0;j<gapC;j++) {
//					int x=1000*(i+r1)+j+c1;
//					if(repeat.contains(x)) {
//						continue l1;
//					}
//					else if(seen.contains(x)) {
//						repeat.add(x);
//						thicc++;
//					}
//					else {
//						seen.add(x);
//					}
//				}
//			}
			next=f.readLine();
		}
		for(int a=0; a<1349; a++) {
			HashSet<Integer> seen=new HashSet<Integer>();
			int r1=sections[a][1];
			int c1=sections[a][2];
			int gapR=sections[a][3];
			int gapC=sections[a][4];
			for(int i=0; i<gapR; i++) {
				for(int j=0; j<gapC; j++) {
					seen.add(2000*(i+r1)+j+c1);
				}
			}
			boolean rep=false;
			for(int b=0; b<1349; b++) {
				if(a!=b)
				for(int i=0;i<sections[b][3];i++) {
					for(int j=0;j<sections[b][4];j++) {
						int x=2000*(i+sections[b][1])+j+sections[b][2];
						if(seen.contains(x)) {
							rep=true;
						}
					}
				}
			}
			if(!rep)
			System.out.println(a+1);
		}
	}
}