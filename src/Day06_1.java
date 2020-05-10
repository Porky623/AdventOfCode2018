import java.io.*;
import java.util.*;
public class Day06_1{
	public static void main(String[] args) throws IOException{
		Scanner sc=new Scanner(new File("input.txt"));
		ArrayList<int[]> inputs=new ArrayList<>();
		while(sc.hasNext()) {
			int[] temp=new int[] {sc.nextInt(),sc.nextInt()};
			inputs.add(temp);
			sc.nextLine();
		}
		int maxX,maxY,minX,minY;
		maxX=maxY=0;
		minX=minY=500;
		for(int i=0; i<inputs.size(); i++) {
			if(maxX<inputs.get(i)[0])
				maxX=inputs.get(i)[0];
			if(maxY<inputs.get(i)[1])
				maxY=inputs.get(i)[1];
			if(minX>inputs.get(i)[0])
				minX=inputs.get(i)[0];
			if(minY>inputs.get(i)[1])
				minY=inputs.get(i)[1];
		}
		int[] counts=new int[inputs.size()];
		int count2=0;
		boolean[] ignore=new boolean[counts.length];
		for(int i=minX; i<=maxX;i++) {
			for(int j=minY; j<=maxY; j++) {
				int[] dist=new int[counts.length];
				int sum=0;
				boolean repeat=false;
				int min=0;
				for(int k=0; k<dist.length; k++) {
					dist[k]=Math.abs((inputs.get(k)[0]-i))+Math.abs((inputs.get(k)[1]-j));
					if(dist[k]==dist[min])
						repeat=true;
					if(dist[k]<dist[min]) {
						repeat=false;
						min=k;
					}
					sum+=dist[k];
				}
				if(sum<10000)
					count2++;
				if(!repeat)
					counts[min]++;
				if((i==minX||i==maxX||j==minY||j==maxY)&&!repeat) {
					ignore[min]=true;
				}
			}
		}
		int ind=0;
		while(ignore[ind])
			ind++;
		int max=ind;
		for(int i=max+1; i<counts.length; i++) {
			if(counts[i]>counts[max]&&!ignore[i])
				max=i;
		}
		System.out.println(counts[max]);
		System.out.println(count2);
	}
}