import java.io.*;
import java.util.*;
public class Day11_1{
	public static void main(String[] args) throws IOException{
		int gridNum=2187;
		int[][] grid=new int[301][301];
		for(int i=1; i<301; i++) {
			for(int j=1; j<301; j++) {
				int rackID=i+10;
				int power=rackID*j;
				power=(power+gridNum)%1000;
				power*=rackID;
				power=(power/100)%10;
				grid[i][j]=power-5;
			}
		}
		int[][][] powers=new int[301][][];
		powers[1]=grid;
		int[] max=new int[] {235,85,1};
		int maxPower=grid[235][85];
		for(int size=2; size<301; size++) {
			powers[size]=new int[302-size][302-size];
			for(int i=1; i<powers[size].length; i++) {
				for(int j=1; j<powers[size].length; j++) {
					int power=0;
					for(int a=0; a<size-1; a++) {
						power+=grid[i+size-1][j+a];
						power+=grid[i+a][j+size-1];
					}
					power+=grid[i+size-1][j+size-1];
					powers[size][i][j]=powers[size-1][i][j]+power;
					if(powers[size][i][j]>maxPower) {
						maxPower=powers[size][i][j];
						max[0]=i;
						max[1]=j;
						max[2]=size;
					}
				}
			}
		}
		System.out.println(max[0]+" "+max[1]+" "+max[2]);
//		int[] max=new int[] {1,1};
//		int maxPower=0;
//		for(int i=1; i<=298; i++) {
//			for(int j=1; j<=298; j++) {
//				int power=0;
//				for(int a=0; a<3; a++) {
//					for(int b=0; b<3; b++) {
//						power+=grid[i+a][j+b];
//					}
//				}
//				if(power>maxPower) {
//					max[0]=i;
//					max[1]=j;
//					maxPower=power;
//				}
//			}
//		}
//		System.out.println(max[0]+" "+max[1]);
	}
}