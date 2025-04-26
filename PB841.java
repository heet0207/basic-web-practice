import java.util.Scanner;

class Employee {
    String emp_firstname, emp_lastname, address, mail_id, mobile_no;
    int emp_id;
    double experience;
    
    // Constructor to initialize employee details
    Employee(String firstName, String lastName, double experience, String address, String mobileNo) {
        this.emp_firstname = firstName;
        this.emp_lastname = lastName;
        this.experience = experience;
        this.address = address;
        this.mobile_no = mobileNo;
        
        // Generate Mail ID
        this.mail_id = generateMailId();
        
        // Generate Employee ID
        this.emp_id = generateId();
    }
    
    // Method to generate email ID
    private String generateMailId() {
        return emp_firstname.toLowerCase() + "." + emp_lastname.toLowerCase() + "@kju.in";
    }
    
    // Method to generate employee ID
    private int generateId() {
        // Assuming the base ID starts from 124
        return 124;
    }
    
    // Method to display employee details
    void display() {
        System.out.println("Emp_name: " + emp_firstname + " " + emp_lastname);
        System.out.println("Emp_id: " + emp_id);
        System.out.println("Mail_id: " + mail_id);
        System.out.println("Address: " + address);
        System.out.println("Experience: " + experience);
        System.out.println("Mobile_no: " + mobile_no);
    }
}

class Assistant_Professor extends Employee {
    double bp, salary;
    String post = "Assistant Professor";
    
    @SuppressWarnings("OverridableMethodCallInConstructor")
    Assistant_Professor(String firstName, String lastName, double experience, String address, String mobileNo, double bp) {
        super(firstName, lastName, experience, address, mobileNo);
        this.bp = bp;
        salary = calculateSalary();
    }
    
    double calculateSalary() {
        double da = 0.70 * bp;
        double hra = 0.10 * bp;
        double pf = 0.12 * bp;
        return bp + da + hra - pf;
    }
    
    @Override
    void display() {
        super.display();
        System.out.println("Post: " + post);
        System.out.println("Basic Pay: " + bp);
        System.out.println("Salary: " + salary);
    }
}

class Associate_Professor extends Employee {
    double bp, salary;
    String post = "Associate Professor";
    
    @SuppressWarnings("OverridableMethodCallInConstructor")
    Associate_Professor(String firstName, String lastName, double experience, String address, String mobileNo, double bp) {
        super(firstName, lastName, experience, address, mobileNo);
        this.bp = bp;
        salary = calculateSalary();
    }
    
    double calculateSalary() {
        double da = 0.75 * bp;
        double hra = 0.15 * bp;
        double pf = 0.12 * bp;
        return bp + da + hra - pf;
    }
    
    @Override
    void display() {
        super.display();
        System.out.println("Post: " + post);
        System.out.println("Basic Pay: " + bp);
        System.out.println("Salary: " + salary);
    }
}

class Professor extends Employee {
    double bp, salary;
    String post = "Professor";
    
    @SuppressWarnings("OverridableMethodCallInConstructor")
    Professor(String firstName, String lastName, double experience, String address, String mobileNo, double bp) {
        super(firstName, lastName, experience, address, mobileNo);
        this.bp = bp;
        salary = calculateSalary();
    }
    
    double calculateSalary() {
        double da = 0.80 * bp;
        double hra = 0.17 * bp;
        double pf = 0.12 * bp;
        return bp + da + hra - pf;
    }
    
    @Override
    void display() {
        super.display();
        System.out.println("Post: " + post);
        System.out.println("Basic Pay: " + bp);
        System.out.println("Salary: " + salary);
    }
}

public class PB841 {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            while (true) {
                System.out.println("Enter post (1. Assistant Professor, 2. Associate Professor, 3. Professor, 4. Exit): ");
                int choice = sc.nextInt();
                sc.nextLine(); // Consume newline character
                
                if (choice == 4) {
                    break;
                }
                
                System.out.println("Enter first name: ");
                String firstName = sc.nextLine();
                
                System.out.println("Enter last name: ");
                String lastName = sc.nextLine();
                
                System.out.println("Enter experience (in years): ");
                double experience = sc.nextDouble();
                sc.nextLine(); // Consume newline character
                
                System.out.println("Enter address: ");
                String address = sc.nextLine();
                
                String mobileNo;
                while (true) {
                    System.out.println("Enter mobile number (10 digits): ");
                    mobileNo = sc.nextLine();
                    if (mobileNo.length() == 10 && mobileNo.matches("\\d+")) {
                        break;
                    } else {
                        System.out.println("Invalid mobile number. Please enter a valid 10-digit number.");
                    }
                }
                
                System.out.println("Enter basic pay: ");
                double bp = sc.nextDouble();
                
                switch (choice) {
                    case 1 -> {
                        Assistant_Professor assistantProfessor = new Assistant_Professor(firstName, lastName, experience, address, mobileNo, bp);
                        assistantProfessor.display();
                    }
                    case 2 -> {
                        Associate_Professor associateProfessor = new Associate_Professor(firstName, lastName, experience, address, mobileNo, bp);
                        associateProfessor.display();
                    }
                    case 3 -> {
                        Professor professor = new Professor(firstName, lastName, experience, address, mobileNo, bp);
                        professor.display();
                    }
                    default -> System.out.println("Invalid choice. Please try again.");
                }
            }
        }
    }
}
