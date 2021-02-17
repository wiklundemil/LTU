package Lab2.level;

import java.util.List;
import java.util.ArrayList;
import java.util.Observable;
import java.awt.Graphics;
@SuppressWarnings("deprecation")

public class Level extends Observable {
	private List<Room> listaObjekt = new ArrayList<Room>();
    private boolean spawn;
    int playerX, playerY;
	static Graphics g;
	Room currentRoom;
	
	public Level() {    
		listaObjekt = new ArrayList<Room>();
		currentRoom = null;
		spawn = true;
	}
	
	public boolean place(Room r, int x, int y) { //Kollar så att rummet inte överlappar
			if(spawn == false){
				return(false);
			}
			for(Room obj: listaObjekt) {
				if((Math.abs(obj.x - r.x) > r.dx) //IF satsen fet AF he be thicc tho
				||
					(Math.abs(obj.y - r.y) > r.dy)
				||
					(Math.abs(r.x - obj.x) > obj.dx)
				||
					(Math.abs(r.y - obj.y) > obj.dy))
				{
					continue;	
				}
				else {
					System.out.println("Place retunerar false");
					return (false);
				}
			}
			System.out.println("lägger till objekt");
			listaObjekt.add(r); // LÄgger till obj om den uppfyller kraven
			if(listaObjekt.size() == 6) { //6 = antal object /rum
				currentRoom = currentLocation();
				System.out.println("Printout");	
			}
			return(true);
	}
	public boolean firstLocation(Room r) {
		if(spawn) {
			spawn = false;
			currentRoom = r;
			return true;
		}
		return false;
	}
	
	public Room currentLocation() {
		
		return currentRoom;
	}
	
	public Room nextRoom() {
		return currentRoom;
	}
	
	public List<Room> getArray() {
		return listaObjekt;
	}
	
	public void addObj(Room r) {
		listaObjekt.add(r);
	}
	public void change() {
		setChanged();
		notifyObservers();
	}
}