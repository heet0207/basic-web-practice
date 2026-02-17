class T2 extends Thread
{
 public static void main(String [] args)
 {
    T2 t = new T2();
    Thread T = new Thread(t);
 t.start();
 System.out.print("one. ");
 t.start();
 System.out.print("two. ");
 }
 public void run() {
 System.out.print("Thread ");
 }
}