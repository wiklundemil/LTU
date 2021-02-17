
package Lab2.level;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.util.ArrayList;
import java.util.List;
import java.util.Observable;
import java.util.Observer;

import javax.swing.JFrame;
import javax.swing.JPanel;
@SuppressWarnings("deprecation")

public class LevelGUI implements Observer {

	private Level lv;
	private Display d;
	
	public LevelGUI(Level level, String name) {
		
		this.lv = level;
		
		JFrame frame = new JFrame(name);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		// TODO: You should change 200 to a value 
		// depending on the size of the level
		d = new Display(lv,800,600);
		
		frame.getContentPane().add(d);
		frame.pack();
		frame.setLocation(0,0);
		frame.setVisible(true);
		
		lv.addObserver(this); //Must be called by every class that wants to observe the levelGUI(). 
		
		
	}
	
	
	public void update(Observable arg0, Object arg1) {
			d.repaint();
	}
	
	private class Display extends JPanel {
		
		
		public Display(Level fp, int x, int y) {
		
			
			addKeyListener(new Listener());
			
			setBackground(Color.pink);
			setPreferredSize(new Dimension(x+20,y+20));
			setFocusable(true);
		}
	
		public void paintComponent(Graphics g) {
			super.paintComponent(g);
			drawRooms(g);
//		    drawPlayer(g);
		}
		
		
		public void drawRooms(Graphics g) {
			List<Room> newlist = new ArrayList<Room>();
			newlist = lv.getArray();
			
			for(Room obj: newlist)  { //for each loop Room = type r = object :namn på lista. 			
				g.setColor(obj.color);	//Floor Color
				g.fillRect(obj.x, obj.y, obj.dx, obj.dy); //Fyller i Rec
				g.drawRect(obj.x, obj.y, obj.dx, obj.dy); //Utkankt Rec
				
				if(obj.north != null) {
					g.setColor(Color.ORANGE);
					g.fillRect((obj.x + obj.dx/2 - 5), obj.y, 10, 25);
				}
				
				if(obj.west != null) {
					g.setColor(Color.ORANGE);
					g.fillRect(obj.x - 9, (obj.y + obj.dy/2 - 5), 25, 10);
				}
				
				if(obj.south != null) {
					g.setColor(Color.ORANGE);
					g.fillRect((obj.x + obj.dx/2 - 5),(obj.y + obj.dy - 15), 10, 25);
				}
				
				if(obj.east != null) {
					g.setColor(Color.ORANGE);
					g.fillRect((obj.x + obj.dx - 14), obj.y + obj.dy/2 - 5, 25, 10);
				}
				if(obj == lv.nextRoom()) { //
					drawPlayer(g, obj);
						
				}
			}
		}

		private void drawPlayer(Graphics g, Room r) {
			g.setColor(Color.white);
			g.drawString("_/(♥ω♥)/‾", r.x + (r.dx)/4, r.y + (r.dy)/2);
			
		}
		
		private class Listener implements KeyListener {
	 	
	 		public void keyPressed(KeyEvent arg0) {
	 			if(arg0.getKeyCode() == KeyEvent.VK_W) { // if key that is pressed == W then...
	 				if(lv.currentRoom.north != null){ // Om Knappen W trycks in så kommer denna ifsatsen att kontrollera att det finns en koridor i nordrikningen för currentRoom. 
						lv.currentRoom = lv.currentRoom.north;  //Current room ska ändras till det rummet som är connected åt norr
						
						System.out.println("Går norrut... Nu är vi i Rum: " + lv.currentRoom.color);
					}
	 			}
	 			else if(arg0.getKeyCode() == KeyEvent.VK_A) { // if key that is pressed == A then...
	 				if(lv.currentRoom.west != null){ // Om Knappen W trycks in så kommer denna ifsatsen att kontrollera att det finns en koridor i nordrikningen för currentRoom. 
						lv.currentRoom = lv.currentRoom.west;
						System.out.println("Går Väster... Nu är vi i Rum: " + lv.currentRoom.color); // Ändra spelarenposition
					}
	 			}
	 			else if(arg0.getKeyCode() == KeyEvent.VK_S) { // if key that is pressed == S then...
	 				if(lv.currentRoom.south != null){ // Om Knappen W trycks in så kommer denna ifsatsen att kontrollera att det finns en koridor i nordrikningen för currentRoom. 
						lv.currentRoom = lv.currentRoom.south;
						System.out.println("Går south... Nu är vi i Rum: " + lv.currentRoom.color);
					}
	 			}
	 			else if(arg0.getKeyCode() == KeyEvent.VK_D) { // if key that is pressed == D then...
	 				if(lv.currentRoom.east != null){ // Om Knappen W trycks in så kommer denna ifsatsen att kontrollera att det finns en koridor i nordrikningen för currentRoom. 
						lv.currentRoom = lv.currentRoom.east;
						System.out.println("Går öst... Nu är vi i Rum: " + lv.currentRoom.color);
					}
	 			}
	 			lv.change();
	 		}

	 		public void keyReleased(KeyEvent arg0) {
	 		}

	 		public void keyTyped(KeyEvent event) {
	 		}
	 	}

	}
	
}