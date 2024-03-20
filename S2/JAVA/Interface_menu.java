import java.util.Scanner;
import java.lang.*;

interface calculation{
	void getdata();
	void area();
	void perimeter();
}

class Circle implements calculation{
	float r;
	
	@Override
	public void getdata() {
		
		Scanner sc = new Scanner(System.in);
		System.out.println("\nEnter the radius of Circle:");
		r = sc.nextFloat();
		
	}
	
	@Override
	public void area() {
		System.out.println("->Area of Circle:"+(Math.PI*r*r));
	}
	
	@Override
	public void perimeter() {
		System.out.println("->Perimeter of Circle:"+(2*Math.PI*r));
	}
}

class Rectangle extends Circle{
	int l,b;
	
	@Override
	public void getdata() {
		super.getdata();
		Scanner sc1 = new Scanner(System.in);
		System.out.println("Enter the length of Rectangle:");
		l = sc1.nextInt();
		System.out.println("Enter the breadth of Rectangle:");
		b = sc1.nextInt();
		
	}
	
	@Override
	public void area() {
		super.area();
		System.out.println("->Area of Rectangle:"+(l*b));
	}
	
	@Override
	public void perimeter() {
		super.perimeter();
		System.out.println("->Perimeter of Rectangle:"+(2*(l+b)));
	}
	
}

class Interface_menu {

	public static void main(String[] args) {
		Rectangle r = new Rectangle();
		
		int choice;
		boolean input = false;
		Scanner sc2 = new Scanner(System.in);
		System.out.println("AREA & PERIMETER CALCULATOR");
		
		while(input == false){
		System.out.println("\nMAIN MENU\n1.To input the values  \t2.To find area  \n3.To find perimeter\t4.Exit\nEnter your Choice:");
		choice = sc2.nextInt();
		
		switch(choice) {
		
		case 1:
			r.getdata();
			break;
		case 2:
			r.area();
			break;
		case 3:
			r.perimeter();
			break;
		case 4:
			System.out.println("EXITING");
			System.exit(0);
		
		}
		
		}


	}

}
