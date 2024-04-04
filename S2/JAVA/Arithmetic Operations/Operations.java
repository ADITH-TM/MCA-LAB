package Arithmetic;

interface OperationsInterface{
    float add();
    float subtract();
    float product();
    float division();
}
public class Operations implements OperationsInterface{
    public float num1,num2;
    public Operations(float num1,float num2){
        this.num1 = num1;
        this.num2 = num2;
    }
    public float add(){
        return num1+num2;
    }
    public float subtract(){
        return num1-num2;
    }
    public float product(){
        return num1*num2;
    }
    public float division(){
        return num1/num2;
    }
}
