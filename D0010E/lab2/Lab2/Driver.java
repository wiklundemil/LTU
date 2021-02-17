package Lab2;
import java.awt.Color;

import Lab2.level.Level;
import Lab2.level.LevelGUI;
import Lab2.level.Room;

public class Driver {
	public static Room[] listObjekt;
	
	public static void run() {
		Level karta = new Level();
		Level karta2 = new Level();
		
		Room r1 = new Room(200, 100, 100, 100, Color.blue); // Skapar 6 st object
		Room r2 = new Room(310, 100, 100, 100, Color.red);
		Room r3 = new Room(420, 100, 100, 100, Color.yellow);
		Room r4 = new Room(200, 210, 100, 100, Color.cyan);
		Room r5 = new Room(310, 210, 100, 100, Color.green);
		Room r6 = new Room(420, 210, 100, 100, Color.black);
		Room r7 = new Room(410, 210, 100, 100, Color.white);
		
		
		Room rw = new Room(100, 100, 100, 100, Color.blue); // Skapar 6 st object
		Room rs = new Room(210, 210, 100, 100, Color.red);
		Room rd = new Room(210, 100, 100, 100, Color.yellow);
		Room ra = new Room(100, 210, 100, 100, Color.cyan);
		
		karta.place(r1, 200, 100);
		karta.place(r2, 310, 100);
		karta.place(r3, 420, 100);
		karta.place(r4, 200, 210);
		karta.place(r5, 310, 210);
		karta.place(r6, 420, 210);
		karta.place(r7, 410, 210);
	
		karta2.place(rw, 100, 100);
		karta2.place(rd, 210, 100);
		karta2.place(rs, 210, 210);
		karta2.place(ra, 100, 210);
		
		karta.firstLocation(r1); 
		//karta2.firstLocation(rw);
		
		r1.connectEastTo(r2); // r1 till r2
		r2.connectWestTo(r1); // r2 till r1
		
		r2.connectEastTo(r3); // r2 till r3
		r3.connectWestTo(r2); // r3 till r2
		
		r3.connectSouthTo(r6); // r3 till r4
		r6.connectNorthTo(r3); // r4 till r3
		
		r6.connectWestTo(r5); // r4 till r5
		r5.connectEastTo(r6); // r5 till r4
		
		r5.connectWestTo(r4); // r5 till r6
		r4.connectEastTo(r5); // r6 till r5
		
		r4.connectEastTo(r5);
		r5.connectWestTo(r4);
		
		r4.connectNorthTo(r1);
		r1.connectSouthTo(r4);

		r4.connectEastTo(r5);
		r5.connectWestTo(r4);
		
		rw.connectEastTo(rd);
		rd.connectWestTo(rw);
		
		rd.connectSouthTo(rs);
		rs.connectNorthTo(rd);
		
		rs.connectWestTo(ra);
		ra.connectEastTo(rs);
		
		rw.connectSouthTo(ra);
		ra.connectNorthTo(rw);
		
		
		/*Level.addObj(r1); Kan vara onödig
		Level.addObj(r2);
		Level.addObj(r3);
		Level.addObj(r4);
		Level.addObj(r5);
		Level.addObj(r6);*/
		
		System.out.println("Storlek lista: " + karta.getArray().size());
		LevelGUI levelgui = new LevelGUI(karta, "Level1");
	}
}