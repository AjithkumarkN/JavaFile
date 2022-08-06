import java.util.Scanner;

public class palindrome {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("enter the palindrome value:");
        int no = sc.nextInt();//get the input from user
        int temp = 0;
        int tem = no;
        while (no > 0) {//check the codition it's true program run untill condition false
            int con = no % 10;//take the last value of number(121) take 1
            temp = (temp * 10) + con;//add (0*10)+1=0+1=1
            no = no / 10;//121/10=12 save to no variable
        }
        if (temp == tem) {//check the condition number is palindrome or not
            System.out.println("it is palindrome:" + temp);
        } else {
            System.out.println("it's not palindrome:" + temp);
        }      //121 reverse the no 121 is palindrome
    }          //123 reverse the no 321 is not palindrome
}
