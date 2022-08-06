import java.util.Scanner;

public class palindromestr {
    public static void main(String [] args){
        Scanner sc = new Scanner(System.in);//get user input
        System.out.println("Enter the String:");
        String St=sc.nextLine();
        int length=St.length();//find the length() String value
        //String name=St;
        String reverse="";//init temp variable
        for(int i=length-1;i>=0;i--){
             reverse=reverse+St.charAt(i);// split the value for character so we use 'charAt()' method, store the reversed value
        }
        if(St.equals(reverse)){//check the condition we compare two object so we use '.equal()'method
            System.out.println(St+" is palindrome");
        }else{
            System.out.println(St+" is not palindrome");
        }
    }
}
