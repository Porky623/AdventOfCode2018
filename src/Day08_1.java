import java.io.*;
import java.util.*;
public class Day08_1{
	public static void main(String[] args) throws IOException{
		Scanner sc=new Scanner(new File("input.txt"));
		Node root=new Node(sc.nextInt(),sc.nextInt());
		int x=input(sc,root,0);
		for(int i=0; i<root.numEnt; i++) {
			root.entries.add(sc.nextInt());
			x+=root.entries.get(i);
		}
		System.out.println(x);
		System.out.println(val(root));
	}
	public static int val(Node node) {
		int x=0;
		if(node.numChild==0) {
			for(int i=0; i<node.numEnt; i++) {
				x+=node.entries.get(i);
			}
			return x;
		}
		for(int i=0; i<node.numEnt; i++) {
			int ind=node.entries.get(i);
			if(0<=ind-1&&ind-1<node.numChild) {
				x+=val(node.children.get(ind-1));
			}
		}
		return x;
	}
	public static int input(Scanner sc, Node cur,int curSum) {
		for(int i=0; i<cur.numChild; i++) {
			cur.children.add(new Node(sc.nextInt(),sc.nextInt()));
			curSum=input(sc,cur.children.get(i),curSum);
			for(int j=0; j<cur.children.get(i).numEnt; j++) {
				cur.children.get(i).entries.add(sc.nextInt());
				curSum+=cur.children.get(i).entries.get(j);
			}
		}
		return curSum;
	}
}

class Node{
	int numChild, numEnt;
	ArrayList<Integer> entries=new ArrayList<Integer>();
	ArrayList<Node> children=new ArrayList<Node>();
	public Node(int c, int e) {
		numChild=c;
		numEnt=e;
	}
}