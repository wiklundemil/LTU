package Lab1;

public class Lifelength4 {
	public static int f1(int a0) {
		if((a0/2.0) == (a0/2)) { // Float == a0/2, om a0/2 �r ej float g�r den ned i if. 
			return a0/2;
		}
		else if(a0 == 1) {
			return 1;
		}
		else {
			return 3*a0+1;
		}
	}
	public static int f2(int a0) {
		return f1(f1(a0));
	}
	public static int f4(int a0) {
		return f2(f2(a0));
	}
	public static int f8(int a0) {
		return f4(f4(a0));
	}
	public static int f16(int a0) {
		return f8(f8(a0));
	}
	public static int f32(int a0) {
		return f16(f16(a0));
	}
	public static int iterateF(int a0, int n) { //Returns the n first steps
		while(n != 0) {
			a0 = f1(a0);
			n--;
		}
		return a0;
	}
	public static int iterLifeLength(int a0) {
		int lifelength = 0;
		while(a0 > 1) {
			a0 = f1(a0);
			lifelength++;
		}
		return lifelength;
	}
	public static String intsToString(int n) {
		String result = "";
		for(n = 1; n <= 15;) {
			result = result + "The life length of " + n + " is " + iterLifeLength(n) + ".\n";
			n++;
		}
		return result;
	}
	
	
	public static void main(String[] args) { 
		int a0 = Integer.parseInt(args[0]);
		System.out.println(intsToString(a0));		
	}
}


/*
int first = Integer.parseInt(args[0]);
int n = 0; // counter
while (first > 1) {
	first = f1(first);
	n++;
	System.out.println("f"+ n+ "="+ first);
}
*/
