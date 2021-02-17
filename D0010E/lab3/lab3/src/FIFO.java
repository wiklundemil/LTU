import java.util.ArrayList;
import java.util.NoSuchElementException;
import java.util.Vector;

public class FIFO implements Queue{
	private ArrayList<Object> listQueue = new ArrayList<Object>();
	private int maxSize = 0; //Maximun value should be stored in class. Max amount of objects of type Object.
	
	//Adds a item to queue.
	public void add(Object item) {
		listQueue.add(item);
	}

	//Removes first item in queue (the first one that was added).
	
	public void removeFirst() {
		if((listQueue.isEmpty()) == false) {
			listQueue.remove(0);
		}
		else {
			throw new NoSuchElementException();
		}
	}

	//Returns out first item in queue.
	
	public Object first() {
		if(listQueue.isEmpty() == true) {
			throw new NoSuchElementException();
		}
		return listQueue.get(0);
	}

	//Sets a max amount of items in queue. 
	@Override
	public int maxSize() {
		return maxSize; //returns the variable maxSize that changes within the class.
	}

	//Method should return true if amount of items in list == 0
	
	public boolean isEmpty() {
		if(listQueue.size() == 0 ) {
			return true;
		}
		return false;
	}

	//Returns the amount of items in list.
	@Override //Override beacuase there is built in methid in java named size etc...
	public int size() {
		if(listQueue.isEmpty() == true) {
			throw new NoSuchElementException();
		}
		return listQueue.size(); 
	}

	//Returns a String beginning with "Queue: " +  item name +  item position in queue
	@Override
	public String toString() {
			int objIndex = 0;
			String s  = "";
			for(Object obj: listQueue) {
				s = s +"(" + String.valueOf(obj) + ") ";
				objIndex++;
			}
		return "Queue: " + s;
	}
	
	public boolean equals(Object f) {
		FIFO fNew = ((FIFO) f);
		if(f instanceof FIFO == true){ //If f is not a FIFO type Then do this
			if(this.listQueue.size() == fNew.listQueue.size()) {
				for(int i = 0; i < size(); i++) {
					if(this.listQueue.get(i) != null && fNew.listQueue.get(i) == null) {
						return false;
					}
					if(this.listQueue.get(i) == null && fNew.listQueue.get(i) != null) {
						return false;
					}
					if(this.listQueue.get(i) == null && fNew.listQueue.get(i) == null) {
						continue;
					}
					if(((this.listQueue.get(i)).equals(fNew.listQueue.get(i)) == false)) {
						return false;
					}
				}
				return true;
			}
		}
		return false;
	}
}
