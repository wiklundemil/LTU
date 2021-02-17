package Lab1;

public class cleanup {
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
/* These methods is for task2 */
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
/*Task 2 methods end */

/* These methods is for task3 */
	public static int iterateF(int a0, int a1) { //Returns the n first steps
		while(a1 != 0) {
			a0 = f1(a0);
			a1--;
		}
		return a0;
	}
/*Task 3 methods end */

/* These methods is for task4 */
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
/*Task 4 methods end */
	
/* These methods is for task6 */
	public static int lifelengthRek(int a0) {
		if (a0 == 1) {
			return 0;
		}
		return 1 + lifelengthRek(f1(a0));
	}
/*Task 4 methods end */
	public static void task1(int a1) { 
		System.out.print(f1(a1));	
	}
	public static void task2(int first) { 
		System.out.print("f1="+f1(first)+" ");
		System.out.print("f2="+f2(first)+" ");
		System.out.print("f4="+f4(first)+" ");
		System.out.print("f8="+f8(first)+" ");
		System.out.print("f16="+f16(first)+" ");
		System.out.print("f32="+f32(first));
	}
	public static void task3(int a0, int a1) { 
		System.out.print(iterateF(a0,a1));	
	}
	public static void task4(int a0) { 
		System.out.println("Lifelength of "+a0+" is "+lifelengthRek(a0));	
	}
	
	public static void task6(int a0) { 
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
	public static void main(String[] args) { 
		int a0 = Integer.parseInt(args[0]);
		int a1 = Integer.parseInt(args[1]);
		int a2 = Integer.parseInt(args[2]); //Program gives error if this line of code is not asigned a value in terminal
		int n= a0;
		switch (n) {
		  case 1:
			cleanup.task1(a1);
		    break;
		  case 2:
			cleanup.task2(a1);
		    break;
		  case 3:
			cleanup.task3(a1, a2);
		    break;
		  case 4:
			cleanup.task4(a1);
		    break;
		  case 5:
			    System.out.println("Case 5 finns inte :)");
			    break;
		  case 6:
			cleanup.task6(a1);
		    break;
		}
	}
}