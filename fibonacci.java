import java.util.Scanner;

public class fibonacci {
    public static void main (String [] args){
        Scanner sc =new Scanner(System.in);
        System.out.println("Enter the Fibonacci value:");
        //get the input from user how many value we want print
        int no=sc.nextInt();
        int a=0,b=1;
        System.out.println(a+"\n"+b);//print first two value 0 and 1
        for(int i=0;i<=no-2;i++){//itretor after three value because we already print first two so we give the input of 'no-2'
            int c=a+b;
            System.out.println(c);//print the after value of 0 and 1 because we already printed
            a=b;//swap the value
            b=c;
        }                     // give the input 5, print 01123
    }
}
