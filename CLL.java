import java.util.*;
@SuppressWarnings("All")
class CLL{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        neel n = new neel();
        boolean  b = true;
    }
}

class neel{

    class Node{
        int data;
        Node next;
        Node(int d){
            data = d;
            next = null;
        }
    }

    Node Head = null;

    void insertFirst(int d){
        Node n1 = new Node(d);
        if(Head == null){
            Head = n1;
            n1.next = Head; // Point to itself
        } else {
            Node temp = Head;
            while(temp.next != Head) {
                temp = temp.next; // Traverse to the last node
            }
            temp.next = n1; // Link the last node to the new node
            n1.next = Head; // New node points to the head
            Head = n1; // Update head to new node
        }
    }
}
