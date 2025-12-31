
import java.util.Scanner;
class RCMO {
    @SuppressWarnings("resource")
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter Base Address");    
        int BA = scanner.nextInt();
        System.out.println("Enter Size OF Element ");
        int SOE = scanner.nextInt();
        System.out.println("Enter Upper Bound Row ");
        int UBR = scanner.nextInt();
        System.out.println("Enter Lower Bound Row ");
        int LBR = scanner.nextInt();
        System.out.println("Enter Upper Bound Column ");
        int UBC = scanner.nextInt();
        System.out.println("Enter Lower Bound Column ");   
        int LBC = scanner.nextInt();
        System.out.println("Enter i Number ");
        int i = scanner.nextInt();
        System.out.println("Enter j Number ");
        int j = scanner.nextInt();

        int ROW = UBR - LBR + 1;
        int COLUMN = UBC - LBC + 1;

        boolean b = true;
        while (b) { 
            System.out.println("1. RMO \n2. CMO \n3. Exit");
            System.out.println("Enter your choice");
            int choice = scanner.nextInt();
            switch (choice) {
                case 1 -> {
                    System.out.println("RMO");
                    if (ROW == 1) {
                        System.out.println("RMO is not possible");
                    } else {
                        int Address = BA + (SOE*(((i - LBR) * COLUMN) + (j - LBC)));
                        System.out.println(Address);
                    }
                }
                case 2 -> {
                    System.out.println("CMO");
                    if (COLUMN == 1) {
                        System.out.println("CMO is not possible");
                    } else {
                        int Address1 = BA + (SOE*((i - LBR) + ((j - LBC)* ROW)));
                        System.out.println(Address1);
                    }
                }
                case 3 -> {
                    System.out.println("Exit");
                    b = false;
                }
                default -> System.out.println("Invalid choice");
            }
        }
    }
}
