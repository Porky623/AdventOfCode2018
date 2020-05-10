import java.io.*;
import java.util.*;
public class Day10_1{
	public static void main(String[] args) throws IOException{
		BufferedReader f=new BufferedReader(new FileReader("input.txt"));
		PrintWriter out=new PrintWriter(new BufferedWriter(new FileWriter("output.csv")));
		String next=f.readLine();
		while(next!=null) {
			String[] inputs=next.split("<");
			String[] inp=inputs[1].split(", ");
			out.print(inp[0].trim()+",");
			out.print(inp[1].trim().split("> ")[0].trim()+",");
			inp=inputs[2].split(", ");
			out.print(inp[0].trim()+",");
			out.println(inp[1].trim().split(">")[0].trim());
			next=f.readLine();
		}
		out.close();
	}
}