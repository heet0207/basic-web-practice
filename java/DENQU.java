import java.util.Scanner;
class DENQU1{
    int SIZE;
    int REAR;
    int FRONT;
    int[] queue;
    public DENQU1(int n){
        SIZE = n;
        REAR = -1;
        FRONT = -1;
        queue = new int[SIZE];
    }
    
    void insertFront(int x){
        if(FRONT == 0 && REAR == SIZE-1){
            System.out.println("Queue is full");
        }else{
            if(FRONT == -1){
                FRONT = 0;
                REAR = 0;
            }else if(FRONT == 0){
                FRONT = SIZE - 1;
            }else{
                FRONT--;
            }
            queue[FRONT] = x;
        }
        System.err.println("Inserted " + x + " at front");
    }   
    void insertRear(int x){
        if(FRONT == 0 && REAR == SIZE-1){
            System.out.println("Queue is full");
        }else{
            if(FRONT == -1){
                FRONT = 0;
                REAR = 0;
            }else if(REAR == SIZE - 1){
                REAR = 0;
            }else{
                REAR++;
            }
            queue[REAR] = x;
        }
        System.err.println("Inserted " + x + " at rear"); 
    }
    void deleteFront(){
        if(FRONT == -1){
            System.out.println("Queue is empty");
        }else{
            if(FRONT == REAR){
                FRONT = -1;
                REAR = -1;
            }else if(FRONT == SIZE - 1){
                FRONT = 0;
            }else{
                FRONT++;
            }
        }
    }                               

    void deleteRear(){
        if(FRONT == -1){
            System.out.println("Queue is empty");
        }else{
            if(FRONT == REAR){
                FRONT = -1;
                REAR = -1;
            }else if(REAR == 0){
                REAR = SIZE - 1;
            }else{
                REAR--;
            }
        }
    }

    void display(){
        if(FRONT == -1){
            System.out.println("Queue is empty");
        }else{
            System.out.print("Queue: ");
            if(REAR >= FRONT){
                for(int i = FRONT; i <= REAR; i++){
                    System.out.print(queue[i] + " ");
                }
            }else{
                for(int i = FRONT; i < SIZE; i++){
                    System.out.print(queue[i] + " ");
                }
                for(int i = 0; i <= REAR; i++){
                    System.out.print(queue[i] + " ");
                }
            }
            System.out.println();
        }
    }
}

class DENQU{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in); 
        System.err.println("Enter the size of the queue");
        int N = sc.nextInt();
        DENQU1 D = new DENQU1(N);

        ;
        boolean b = true;
        while(b){
            System.err.println("1. Insert at front 2. Insert at rear 3. Delete from front 4. Delete from rear 5. Display 6. Exit");
            int choice = sc.nextInt();
            switch(choice){
                case 1:
                    System.err.println("Enter the element to insert at front");
                    int x = sc.nextInt();
                    D.insertFront(x);
                    break;
                case 2:
                    System.err.println("Enter the element to insert at rear");
                    int y = sc.nextInt();
                    D.insertRear(y);
                    break;
                case 3:
                    D.deleteFront();
                    break;
                case 4:
                    D.deleteRear();
                    break;
                case 5:
                    D.display();
                    break;
                default:
                    System.err.println("Invalid choice");
            }
            System.err.println("1. Insert at front 2. Insert at rear 3. Delete from front 4. Delete from rear 5. Display 6. Exit");
            choice = sc.nextInt();
        }
    }
}