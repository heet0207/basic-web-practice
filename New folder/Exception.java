import java.util.Scanner;
class Exception {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the size of the stack");
        int N = scanner.nextInt();      
        Stack1 s = new Stack1(N);   
        while(true){
            System.out.println("1. Push\n2. Pop\n3. Peep\n4. Change\n5. Display\n6. Exit");
            int choice = scanner.nextInt();
            switch(choice)
{                case 1 -> {
    System.out.println("Enter the data to push");
    int data = scanner.nextInt();
    s.push(data);
                }
                case 2 -> s.pop();
                case 3 -> s.peep();
                case 4 -> {
                    System.out.println("Enter the index and data to change");
                    int I = scanner.nextInt();
                    int X = scanner.nextInt();
                    s.change(I,X);
                }
                case 5 -> s.display();
                case 6 -> System.exit(0);
                default -> System.out.println("Invalid Choice");
            }
        }
        }
    }