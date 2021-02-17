package Lab2.level;

import java.awt.Color;

public class Room { 
	int x, y;
	int dx, dy;
	Color color;
	Room north = null, south = null, east = null, west = null; 
	Room[] doorways;
	
	
	public Room(int x, int y, int dx, int dy, Color color) { // Constructor
		this.x = x;
		this.y = y;
		this.dx = dx;
		this.dy = dy;
		this.color = color;
		doorways = new Room[4];
		
		System.out.println(this.dx + "x" + this.dy + this.color);
	}


	public void connectNorthTo(Room r) {
		this.north = r;  				
		doorways[0] = r;
	}
	public void connectEastTo(Room r) {
		this.east = r;
		doorways[1] = r;
	}
	public void connectSouthTo(Room r) {
		this.south = r;
		doorways[2] = r;
	}
	public void connectWestTo(Room r) {
		this.west = r;
		doorways[3] = r;
	}
}