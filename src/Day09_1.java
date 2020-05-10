import java.io.*;
import java.util.*;
public class Day09_1{
	public static void main(String[] args) throws IOException{
		int numPlayers=419;
		int lastMarble=7105200;
		int[] players=new int[numPlayers];
		ArrayList<Integer> marbles=new ArrayList<Integer>();
		marbles.add(0);
		int curInd=0;
		for(int addedMarble=1; addedMarble<=lastMarble; addedMarble++) {
			if(addedMarble%23==0) {
				int curPlayer=(addedMarble-1)%numPlayers;
				players[curPlayer]+=addedMarble;
				int ind=(curInd-7+7*marbles.size())%marbles.size();
				players[curPlayer]+=marbles.get(ind);
				marbles.remove(ind);
				curInd=(ind)%marbles.size();
			}
			else if(marbles.size()==1){
				marbles.add(addedMarble);
				curInd=1;
			}
			else {
				int newInd=(curInd+2)%marbles.size();
				if(curInd+2==marbles.size())
					newInd=marbles.size();
				if(curInd+2==marbles.size())
					marbles.add(addedMarble);
				else
				marbles.add((curInd+2)%marbles.size(), addedMarble);
				curInd=newInd;
			}
		}
		int max=players[0];
		for(int i=1; i<numPlayers; i++) {
			if(max<players[i])
				max=players[i];
		}
		System.out.println(max);
	}
}