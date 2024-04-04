import Arithmetic.Operations;
import java.util.*;

class ArithmeticPackage{
    public static void main(String[] args){
        Scanner scn = new Scanner(System.in);
        System.out.print("Enter the First Number : ");
        float a = scn.nextFloat();
        System.out.print("Enter the Second Number : ");
        float b = scn.nextFloat();
        Operations op = new Operations(a,b);
        System.out.println(a+"+"+b+"="+(op.add()));
        System.out.println(a+"-"+b+"="+(op.subtract()));
        System.out.println(a+"x"+b+"="+(op.product()));
        System.out.println(a+"/"+b+"="+(op.division()));
    }
}
