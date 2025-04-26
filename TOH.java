
import java.util.Scanner;
class TOH {
    public static void main(String[] args) {
        @SuppressWarnings("resource")
        Scanner scanner = new Scanner(System.in);
            int n = scanner.nextInt();
            toh(n, 'A', 'B', 'C');
        }

    static void toh(int n, char A, char B, char C) {
        if (n == 1) {
            System.out.println("Move disk 1 from " + A + " to " + C);
            return;
        }
        toh(n - 1, A, C, B);
        System.out.println("Move disk " + n + " from " + A + " to " + C);
        toh(n - 1, B, A, C);
    }
}
