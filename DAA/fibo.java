import java.util.*;/**
 * fibo
 */
public class fibo {
    public static int recursive(int n){
        if(n==0 || n==1){
            return n;
        }
        return recursive(n-1) + recursive(n-2);
    }

    public static void nonrecursive(int n){
        int a=0;
        int b=1;
        for(int i=0;i<n;i++){
            System.out.println(a+"");
            int c= a+b;
            a=b;
            b=c;
        }
    }

    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the numbers n ");
        int n =sc.nextInt();

        for(int i=0;i<n;i++){
            System.out.println(recursive(i)+"");
        }

        System.out.println();

        nonrecursive(n);

        sc.close();
    }
    
}