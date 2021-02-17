package Lab1;

public class Lifelength6 {
	public static int f1(int a0) {
		if((a0/2.0) == (a0/2)) { // Float == a0/2, om a0/2 är ej float går den ned i if. 
			return a0/2;
		}
		else if(a0 == 1) {
			return 1;
		}
		else {
			return 3*a0+1;
		}
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
			result = result + "Iteration: The life length of " + n + " is " + iterLifeLength(n) + "\n";
			n++;
		}
		return result;
	}
	public static int lifelengthRek(int a0) {
		if (a0 == 1) {
			return 0;
		}
		return 1 + lifelengthRek(f1(a0));
	}
	
	
	public static void main(String[] args) { 
		int a0 = Integer.parseInt(args[0]);
		int i = 0;
		for(i = 0; i <= 15;) {
			if(a0 == 0) {
				continue;
			}
			System.out.println("Recursion: The life length of " + a0 + " is " + lifelengthRek(a0));		
			i++;
			a0--;
		}
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
