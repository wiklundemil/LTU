import java.util.ArrayList;
import java.util.Scanner;
import java.io.File;
import java.io.IOException;

public class GraphIO {
//	public void addNode(int id, int x, int y) {			//Dessa ligger redan i FIFOmain
//		Node id = new Node();
//	}
//	public void addEdge(int id, int id2, int weight) {
//		
//	}
	static public void readFile(Graph g, String filename) {
		System.out.print("Filnamn: "+ filename); //Kontrollerar filename vilken string som passades
		try {
			File file = new File(filename);
			Scanner scanner = new Scanner(file); //Scanner måste ta en File type.
			int nodeAmount = Integer.parseInt(scanner.nextLine());//Reads the first line in graphFile (100)
			
			for(int i = 0; i < nodeAmount; i++) { //For the amount of nodes we do this. Had blancspace in graphfile. *Fixed*
				String line = scanner.nextLine(); // Creates a string of the line for each run it make. New string for each row
				
				String id = line.split(" ")[0];
				String x  = line.split(" ")[1];
				String y  = line.split(" ")[2];
				
				int idInt = Integer.parseInt(id);
				int xInt   = Integer.parseInt(x);
				int yInt   = Integer.parseInt(y);
				
				g.addNode(idInt, xInt, yInt); // addNode kräver int värde
				System.out.println("Node added: " + i);
				
			}
			int i=0; //Mini counter
			while(scanner.hasNextLine()) { //For as long as there is a next row then do this...
				String line = scanner.nextLine(); //Each time while runs then we move down a row declareing line to a new row
				
				int id1    = Integer.parseInt(line.split(" ")[0]); 
				int id2    = Integer.parseInt(line.split(" ")[1]);
				int weight = Integer.parseInt(line.split(" ")[2]);
				g.addEdge(id1, id2, weight);
				System.out.println("Edge added: " + i); 
				i++;
			}
			scanner.close();
		}
		catch(IOException error) {
			System.out.print("Kommer hit");
			error.printStackTrace();
        }
	}
}
