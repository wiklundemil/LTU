package Lab1;
public class Lifelength2 {
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
	
	public static void main(String[] args) { 
		int first = Integer.parseInt(args[0]);
		System.out.print("f1="+f1(first)+" ");
		System.out.print("f2="+f2(first)+" ");
		System.out.print("f4="+f4(first)+" ");
		System.out.print("f8="+f8(first)+" ");
		System.out.print("f16="+f16(first)+" ");
		System.out.print("f32="+f32(first));

		
	}
}
