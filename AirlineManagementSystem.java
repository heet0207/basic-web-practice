import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class Flight {
    int flightId;
    String destination;
    double price;

    Flight(int flightId, String destination, double price) {
        this.flightId = flightId;
        this.destination = destination;
        this.price = price;
    }
}

class Ticket {
    int ticketId;
    int flightId;
    String passengerName;

    Ticket(int ticketId, int flightId, String passengerName) {
        this.ticketId = ticketId;
        this.flightId = flightId;
        this.passengerName = passengerName;
    }
}

public class AirlineManagementSystem {
    private static List<Flight> flights = new ArrayList<>();
    private static List<Ticket> tickets = new ArrayList<>();
    private static int ticketCounter = 1;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        initializeFlights();
        
        while (true) {
            System.out.println("\n1. View Flights 2. Book 3. Cancel 4. View Tickets 5. Exit: ");
            int choice = scanner.nextInt();
            scanner.nextLine();

            switch (choice) {
                case 1:
                    viewFlights();
                    break;
                case 2:
                    bookTicket(scanner);
                    break;
                case 3:
                    cancelTicket(scanner);
                    break;
                case 4:
                    viewTickets();
                    break;
                case 5:
                    System.out.println("Goodbye!");
                    scanner.close();
                    return;
                default:
                    System.out.println("Invalid choice.");
            }
        }
    }

    private static void initializeFlights() {
        flights.add(new Flight(101, "New York", 500.00));
        flights.add(new Flight(102, "London", 700.00));
        flights.add(new Flight(103, "Tokyo", 900.00));
    }

    private static void viewFlights() {
        System.out.println("\nAvailable Flights:");
        for (Flight flight : flights) {
            System.out.println("Flight ID: " + flight.flightId + ", Destination: " + flight.destination + ", Price: $" + flight.price);
        }
    }

    private static void bookTicket(Scanner scanner) {
        System.out.print("Enter Flight ID: ");
        int flightId = scanner.nextInt();
        scanner.nextLine();
        System.out.print("Enter Passenger Name: ");
        String name = scanner.nextLine();
        tickets.add(new Ticket(ticketCounter, flightId, name));
        System.out.println("Ticket booked successfully! Ticket ID: " + ticketCounter);
        ticketCounter++;
    }

    private static void cancelTicket(Scanner scanner) {
        System.out.print("Enter Ticket ID: ");
        int ticketId = scanner.nextInt();
        tickets.removeIf(ticket -> ticket.ticketId == ticketId);
        System.out.println("Ticket " + ticketId + " cancelled successfully.");
    }

    private static void viewTickets() {
        if (tickets.isEmpty()) {
            System.out.println("No tickets booked yet.");
        } else {
            System.out.println("\nBooked Tickets:");
            for (Ticket ticket : tickets) {
                System.out.println("Ticket ID: " + ticket.ticketId + ", Flight ID: " + ticket.flightId + ", Passenger: " + ticket.passengerName);
            }
        }
    }
}
