import java.util.Scanner;
class K {
@SuppressWarnings("resource")
public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    System.out.println("Enter Base Address");    
    int BA = scanner.nextInt();
    System.out.println("Enter Size OF Element ");
    int SOE = scanner.nextInt();
    System.out.println("Enter Upper Bound ");
    int UB = scanner.nextInt();
    System.out.println("Enter Lower Bound ");
    int LB = scanner.nextInt();
    System.out.println("Enter Number of Elements ");
    int K = scanner.nextInt();
    if (K > UB) {
        System.out.println("Invalid Input");
    } else
    {
        int Address = BA + (SOE * (K - LB));
        System.out.println(Address);   
    }
  } 
}    

