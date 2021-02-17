package Lab1;

public class Lifelength1 {
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
	public static void main(String[] args) { 
		int a0 = Integer.parseInt(args[0]);
		System.out.print(f1(a0));	
	}
}