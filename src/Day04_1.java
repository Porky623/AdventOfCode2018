import java.util.*;
import java.io.*;
public class Day04_1 {
	public static void main(String[] args) throws IOException{
		BufferedReader f = new BufferedReader(new FileReader("input.txt"));
		String next=f.readLine();
		ArrayList<String> inputs=new ArrayList<String>();
		while(next!=null) {
			inputs.add(next);
			next=f.readLine();
		}
		int[][] adjIn=new int[inputs.size()][4];
		for(int i=0; i<adjIn.length; i++) {
			StringTokenizer st1=new StringTokenizer(inputs.get(i));
			StringTokenizer st2=new StringTokenizer(st1.nextToken(),"-");
			st2.nextToken();
			adjIn[i][0]=Integer.parseInt(st2.nextToken());
			adjIn[i][1]=Integer.parseInt(st2.nextToken());
			st2=new StringTokenizer(st1.nextToken(),":");
			int x=Integer.parseInt(st2.nextToken());
			String temp=st2.nextToken();
			adjIn[i][2]=60*x+Integer.parseInt(temp.substring(0, temp.length()-1));
			st1.nextToken();
			temp=st1.nextToken();
			if('0'<=temp.charAt(1)&&'9'>=temp.charAt(1)) {
				adjIn[i][3]=Integer.parseInt(temp.substring(1));
			}
			else if('u'==temp.charAt(0)) {
				adjIn[i][3]=-1;
			}
			else {
				adjIn[i][3]=-2;
			}
		}
		sort(adjIn);
		int i=0;
		HashMap<Integer,HashMap<Integer,Integer>> bigMap=new HashMap<Integer,HashMap<Integer,Integer>>();
		while(i<adjIn.length) {
			int ID=adjIn[i++][3];
			if(ID==-1) {
				System.out.println("BAD!!");
			}
			if (!bigMap.containsKey(ID)){
				bigMap.put(ID, new HashMap<Integer,Integer>());
				for(int j=-1; j<60; j++) {
					bigMap.get(ID).put(j, 0);
				}
			}
			while(adjIn[i][3]==-2) {
				for(int j=adjIn[i][2]; j<adjIn[i+1][2]; j++) {
					bigMap.get(ID).put(j, bigMap.get(ID).get(j)+1);
					bigMap.get(ID).put(-1, bigMap.get(ID).get(-1)+1);
				}
				i+=2;
				if(i>933) {
					break;
				}
			}
		}
		Set<Integer> keys=bigMap.keySet();
//		int max=643;
//		for(int j:keys) {
//			if(bigMap.get(j).get(-1)>bigMap.get(max).get(-1)) {
//				max=j;
//			}
//		}
//		int newMax=0;
//		for(int j=1; j<60; j++) {
//			if(bigMap.get(max).get(j)>bigMap.get(max).get(newMax)) {
//				newMax=j;
//			}
//		}
		int max=643;
		int newMax=0;
		for(int j:keys) {
			for(int k=0; k<60; k++) {
				if(bigMap.get(j).get(k)>bigMap.get(max).get(newMax)) {
					max=j;
					newMax=k;
				}
			}
		}
		System.out.println(newMax*max);
	}
	public static void sort(int[][] arr) {
		Arrays.sort(arr, new Comparator<int[]>() {
			public int compare(int[] int1,int[] int2) {
				if(int1[0]!=int2[0])
					return int1[0]-int2[0];
				if(int1[1]!=int2[1])
					return int1[1]-int2[1];
				if(int1[2]!=int2[2])
					return int1[2]-int2[2];
				return 0;
			}
		});
	}
}
