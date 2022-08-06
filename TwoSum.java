import java.util.Scanner;

public class TwoSum {
    private static int[] twoNum(int[] nums,int target){
        for(int i=0;i<nums.length-1;i++) {// start 0 index to till front of last value
            for (int j = i + 1; j < nums.length; j++) { //start 1 index end last index
                if (nums[i] + nums[j] == target) { //check the condition add two number get the target value
                    return new int[]{i,j};// return the index value
                }
            }
        }
        return new int[]{};
    }
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int num=sc.nextInt();//user input
        int [] nums=new int[num];//create the new array
        for(int i=0;i<nums.length;i++){
            nums[i]=sc.nextInt();//get the value from user and stored array index
        }
        int target=sc.nextInt();
        sc.close();//close the Scanner
        int[] indices=twoNum(nums, target);
        if(indices.length==2){
            System.out.println(indices[0]+" "+indices[1]);//condition true print this or print else part
        }else{
            System.out.println("Solution Not Found");
        }
    }
}
