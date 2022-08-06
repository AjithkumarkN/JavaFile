import java.util.Scanner;
import java.util.*;

public class amstrong {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);//user input
        System.out.println("Enter the Amstrong Number:");
        int num=sc.nextInt();//user input int value
        int original=num;
        int result=0;
        while(num!=0){//program run until condition false
            int nums=num%10;
             result+=Math.pow(nums,3);//it's denote power of 3 means(num*num*num)/it's use math .pow()method
            num=num/10;
        }
        if(result==original){//check codition true ,true means seperate the number and multiply and add the final number equal to orginal number
            System.out.println(original+" is amstrong number");
        }else{
            System.out.println(original+" is not amstrong number");
        }
    }
}
