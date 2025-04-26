import java.util.Scanner;

class pettern {
    @SuppressWarnings({ "ConvertToTryWithResources", "unused" })
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter Rows Number");
        int N = scanner.nextInt();
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N; j++) {
                if (i == 1 || i == N || j == 1 || j == N) {
                    System.out.print("* ");
                } else {
                    System.out.print("  ");
                }
            }
            System.out.println();
        }
        System.out.println("Enter Rows Number");
    }
}