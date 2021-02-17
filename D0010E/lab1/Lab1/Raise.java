package Lab1;

public class Raise {
	public static double recRaiseOne(double x, int k) {
		if (k==0) {
			recRaiseOneCounter++;
			return 1.0;
		} 
		else {
			recRaiseOneCounter++;
			double var = x * recRaiseOne(x, k-1);
			return var;
		}
	}
	public static double recRaiseHalf(double x, int k) {
		if(k == 0) {
			recRaiseHalfCounter++;
			return 1;
		}
		else if (k % 2 == 0){
			recRaiseHalfCounter++;
			double temp = recRaiseHalf(x,(k/2));
			return temp*temp;
		}
		else{
			recRaiseHalfCounter++;
			double temp = recRaiseHalf(x,(k/2));
			return x*temp*temp;
		}
	}
	public static void main(String[] args) {
		int a0 = Integer.parseInt(args[0]);
		for(int i = 1; i <= a0; i++) {
			System.out.println("Half: " + recRaiseHalf(1.5, i));
			System.out.println("One : " +  recRaiseOne(1.5, i));
			System.out.println("Half Counter: " + recRaiseHalfCounter);
			System.out.println("One Counter : "  + recRaiseOneCounter);
			recRaiseHalfCounter = 0;
			recRaiseOneCounter  = 0;
		}
	}
	static int recRaiseHalfCounter;
	static int  recRaiseOneCounter;
}
