import java.util.*;
class Employee{
    int eNo;
    String eName;
    double eSalary;
    void disp(){
        System.out.println("Employee Details : ");
        System.out.println("Employee No : "+eNo);
        System.out.println("Employee Name : "+eName);
        System.out.println("Employee Salary : "+eSalary);
    }
}
class EmployeeSearch{
    public static void main(String[] args) {
        int i;
        Scanner scn = new Scanner(System.in);
        Employee emp[] = new Employee[10];
        System.out.println("Enter total no of employees : ");
        int n = scn.nextInt();
        for(i=0;i<n;i++){
            emp[i] = new Employee();
            System.out.println("Enter the Details of Employee "+(i+1));
            System.out.print("Emp No : ");
            emp[i].eNo = scn.nextInt();
            System.out.print("Name : ");
            emp[i].eName = scn.next();
            System.out.print("Salary : ");
            emp[i].eSalary = scn.nextDouble();
        }
        System.out.println("Enter the Emp No to search : ");
        int s = scn.nextInt();
        for(i=0;i<n;i++){
            if(emp[i].eNo == s){
                emp[i].disp();
                System.exit(0);
            }
        }
        System.out.println("Employee not found");
    }
}
