import java.util.Scanner;
class Stack1{
    static int TOP,SIZE;
    int[] s;
    Stack1(int size){
        SIZE = size;
        s = new int[SIZE];
        TOP = -1;
    }
    void push(int data){
        if(TOP >=  SIZE-1){
            System.out.println("Stack Overflow");
            return;
        }
        s[++TOP] = data;
    System.out.println("Pushed: "+data);
    }
    void pop(){
        if(TOP == -1){
            System.out.println("Stack Underflow");
            return;
        }
        System.out.println("Popped: "+s[TOP--]);
    }
    void peep(){
        if(TOP == -1){
            System.out.println("Stack Underflow");
            return;
        }
        System.out.println("Peeped: "+s[TOP]);
    }
    void change(int I, int X){
        if(TOP - I + 1 <= -1){
            System.out.println("Invalid Index");
            return;
        }
        s[TOP] = X;
        System.out.println("Changed: "+X);
    }
    void display(){
        if(TOP == -1){
            System.out.println("Stack Underflow");
            return;
        }
        for(int i = TOP; i >= 0; i--){
            System.out.println(s[i]);
        }
       
    }
}

@SuppressWarnings("unused")
class Stack{
    @SuppressWarnings("resource")
    public static void main(String[]args) {
     Scanner scanner = new Scanner(System.in);
     System.out.println("Enter the size of the stack"); 
     int N = scanner.nextInt();
     Stack1 s = new Stack1(N);


        boolean b = true;
        while(b){
            System.out.println("1.Push  2.Pop  3.Peep  4.Change  5.Display 6.Exit");
            int choice = scanner.nextInt();
            System.out.println();


            switch(choice){
                case 1 -> {
                    System.out.println("Enter the data to push");
                    int data = scanner.nextInt();
                    System.out.println("Enter the data to push");
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
                case 6 -> b = false;
                default -> System.out.println("Invalid Choice");
            }
        }
    }
}