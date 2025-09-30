import java.sql.*;
import java.util.*;

class DatabaseHelper {
    Connection connection;

    public DatabaseHelper() throws SQLException {
        connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/event_management", "root", "");
    }

    public Connection getConnection() {
        return connection;
    }
}

abstract class Menu {
    Scanner sc = new Scanner(System.in);
    Connection connection;
    UpdateHistoryStack updateHistory;

    public Menu(Connection connection, UpdateHistoryStack updateHistory) {
        this.connection = connection;
        this.updateHistory = updateHistory;
    }

    abstract void showMenu();
}

class AdminMenu extends Menu {
    public AdminMenu(Connection connection, UpdateHistoryStack updateHistory) {
        super(connection, updateHistory);
    }


    void showMenu() {
        int choice;
        do {
            System.out.println("\n--- Admin Menu ---");
            System.out.println("1. Create Event");
            System.out.println("2. View All Events");
            System.out.println("3. View All Users");
            System.out.println("4. Update Event Details");
            System.out.println("5. Cancel Event");
            System.out.println("6. Track Available Seats");
            System.out.println("7. View Update History");
            System.out.println("8. View Upcoming Events");
            System.out.println("0. Logout");
            System.out.print("Enter your choice: ");

            while (!sc.hasNextInt()) {
                System.out.print("Enter a valid number: ");
                sc.next();
            }
            choice = sc.nextInt();
            sc.nextLine();

            switch (choice) {
                case 1: createEvent(); break;
                case 2: viewAllEvents(); break;
                case 3: viewAllUsers(); break;
                case 4: updateEventDetails(); break;
                case 5: cancelEvent(); break;
                case 6: trackAvailableSeats(); break;
                case 7: viewUpdateHistory(); break;
                case 8: viewUpdateHistory();
                    EventManagementLinkedList es = new EventManagementLinkedList();
                    es.viewUpcomingEvents(); break;
                case 0: System.out.println("Logging out..."); break;
                default: System.out.println("Invalid choice. Try again."); break;
            }
        } while (choice != 0);
    }

    void createEvent() {
        try {
            String name = "";
            while (name.isBlank()) {
                System.out.print("Enter Event Name: ");
                name = sc.nextLine().trim();
                if (name.isBlank()) {
                    System.out.println("Event name cannot be empty. Please try again.");
                }
            }

            String date = "";
            while (true) {
                System.out.print("Enter Event Date (YYYY-MM-DD): ");
                date = sc.nextLine().trim();
                if (date.matches("^\\d{4}-\\d{2}-\\d{2}$")) {
                    break;
                } else {
                    System.out.println("Invalid date format. Please enter in YYYY-MM-DD format.");
                }
            }

            String location = "";
            while (location.isBlank()) {
                System.out.print("Enter Event Location: ");
                location = sc.nextLine().trim();
                if (location.isBlank()) {
                    System.out.println("Event location cannot be empty. Please try again.");
                }
            }

            String description = "";
            while (description.isBlank()) {
                System.out.print("Enter Event Description: ");
                description = sc.nextLine().trim();
                if (description.isBlank()) {
                    System.out.println("Event description cannot be empty. Please try again.");
                }
            }

            int capacity = -1;
            while (capacity <= 0) {
                System.out.print("Enter Event Capacity (must be a positive number): ");
                if (sc.hasNextInt()) {
                    capacity = sc.nextInt();
                    sc.nextLine();
                    if (capacity <= 0) {
                        System.out.println("Capacity must be greater than 0.");
                    }
                } else {
                    System.out.println("Invalid input. Please enter a number.");
                    sc.nextLine();
                }
            }

            String query = "INSERT INTO events (name, date, location, description, capacity) VALUES (?, ?, ?, ?, ?)";
            PreparedStatement ps = connection.prepareStatement(query);
            ps.setString(1, name);
            ps.setString(2, date);
            ps.setString(3, location);
            ps.setString(4, description);
            ps.setInt(5, capacity);
            ps.executeUpdate();

            updateHistory.push("Created Event: " + name);
            System.out.println("Event created successfully.");

        } catch (SQLException e) {
            System.out.println("Failed to create event. Error: " + e.getMessage());
        }
    }


    void viewAllEvents() {
        try {
            String query = "SELECT * FROM events";
            Statement stmt = connection.createStatement();
            ResultSet rs = stmt.executeQuery(query);

            System.out.printf("\n%-5s %-20s %-12s %-15s %-30s %-10s\n",
                    "ID", "Name", "Date", "Location", "Description", "Capacity");
            System.out.println("-----------------------------------------------------------------------------------------------");

            while (rs.next()) {
                System.out.printf("%-5d %-20s %-12s %-15s %-30s %-10d\n",
                        rs.getInt("id"), rs.getString("name"), rs.getString("date"),
                        rs.getString("location"), rs.getString("description"), rs.getInt("capacity"));
            }
            updateHistory.push("Viewed All Events");
        } catch (SQLException e) {
            System.out.println("Failed to view events.");
        }
    }

    void viewAllUsers() {
        try {
            String query = "SELECT * FROM users";
            Statement stmt = connection.createStatement();
            ResultSet rs = stmt.executeQuery(query);

            System.out.printf("\n%-5s %-20s %-25s %-10s\n", "ID", "Name", "Email", "EventID");
            System.out.println("-------------------------------------------------------------");

            while (rs.next()) {
                System.out.printf("%-5d %-20s %-25s %-10d\n",
                        rs.getInt("id"), rs.getString("name"),
                        rs.getString("email"), rs.getInt("event_id"));
            }
            updateHistory.push("Viewed All Users");
        } catch (SQLException e) {
            System.out.println("Failed to view users.");
        }
    }

    void updateEventDetails() {
        try {
            int eventId = -1;
            while (eventId <= 0) {
                System.out.print("Enter Event ID to Update: ");
                if (sc.hasNextInt()) {
                    eventId = sc.nextInt();
                    sc.nextLine();
                    if (eventId <= 0) {
                        System.out.println("Event ID must be greater than 0.");
                    }
                } else {
                    System.out.println("Invalid input. Please enter a valid number.");
                    sc.nextLine();
                }
            }

            String name = "";
            while (name.isBlank()) {
                System.out.print("New Event Name: ");
                name = sc.nextLine().trim();
                if (name.isBlank()) {
                    System.out.println("Event name cannot be empty. Please try again.");
                }
            }

            String date = "";
            while (true) {
                System.out.print("New Event Date (YYYY-MM-DD): ");
                date = sc.nextLine().trim();
                if (date.matches("^\\d{4}-\\d{2}-\\d{2}$")) {
                    break;
                } else {
                    System.out.println("Invalid date format. Please enter in YYYY-MM-DD format.");
                }
            }

            String location = "";
            while (location.isBlank()) {
                System.out.print("New Location: ");
                location = sc.nextLine().trim();
                if (location.isBlank()) {
                    System.out.println("Location cannot be empty. Please try again.");
                }
            }

            String description = "";
            while (description.isBlank()) {
                System.out.print("New Description: ");
                description = sc.nextLine().trim();
                if (description.isBlank()) {
                    System.out.println("Description cannot be empty. Please try again.");
                }
            }

            int capacity = -1;
            while (capacity <= 0) {
                System.out.print("New Capacity: ");
                if (sc.hasNextInt()) {
                    capacity = sc.nextInt();
                    sc.nextLine();
                    if (capacity <= 0) {
                        System.out.println("Capacity must be greater than 0.");
                    }
                } else {
                    System.out.println("Invalid input. Please enter a number.");
                    sc.nextLine();
                }
            }

            String query = "UPDATE events SET name=?, date=?, location=?, description=?, capacity=? WHERE id=?";
            PreparedStatement ps = connection.prepareStatement(query);
            ps.setString(1, name);
            ps.setString(2, date);
            ps.setString(3, location);
            ps.setString(4, description);
            ps.setInt(5, capacity);
            ps.setInt(6, eventId);

            int rows = ps.executeUpdate();
            if (rows > 0) {
                updateHistory.push("Updated Event ID: " + eventId);
                System.out.println("Event updated successfully.");
            } else {
                System.out.println("Event not found.");
            }

        } catch (SQLException e) {
            System.out.println("Failed to update event details. Error: " + e.getMessage());
        }
    }


    void cancelEvent() {
        try {
            int eventId = -1;

            while (eventId <= 0) {
                System.out.print("Enter Event ID to Cancel: ");
                if (sc.hasNextInt()) {
                    eventId = sc.nextInt();
                    sc.nextLine();
                    if (eventId <= 0) {
                        System.out.println("Event ID must be greater than 0.");
                    }
                } else {
                    System.out.println("Invalid input. Please enter a valid number.");
                    sc.nextLine();
                }
            }

            String query = "DELETE FROM events WHERE id=?";
            PreparedStatement ps = connection.prepareStatement(query);
            ps.setInt(1, eventId);

            int rows = ps.executeUpdate();
            if (rows > 0) {
                updateHistory.push("Cancelled Event ID: " + eventId);
                System.out.println("Event cancelled successfully.");

                Statement stmt = connection.createStatement();
                stmt.executeUpdate("SET @count = 0");
                stmt.executeUpdate("UPDATE events SET id = (@count := @count + 1) ORDER BY id");
                stmt.executeUpdate("ALTER TABLE events AUTO_INCREMENT = 1");

                System.out.println("Event IDs resequenced.");
            } else {
                System.out.println("Event not found.");
            }

        } catch (SQLException e) {
            System.out.println("Failed to cancel event. Error: " + e.getMessage());
        }
    }



    void trackAvailableSeats() {
        try {
            System.out.print("Enter Event ID: ");
            int eventId = sc.nextInt();
            sc.nextLine();

            String query1 = "SELECT capacity FROM events WHERE id=?";
            PreparedStatement ps1 = connection.prepareStatement(query1);
            ps1.setInt(1, eventId);
            ResultSet rs1 = ps1.executeQuery();

            if (rs1.next()) {
                int capacity = rs1.getInt("capacity");

                String query2 = "SELECT COUNT(*) as count FROM users WHERE event_id=?";
                PreparedStatement ps2 = connection.prepareStatement(query2);
                ps2.setInt(1, eventId);
                ResultSet rs2 = ps2.executeQuery();

                if (rs2.next()) {
                    int registered = rs2.getInt("count");
                    int available = capacity - registered;
                    System.out.println("Available seats: " + available);
                    updateHistory.push("Available seats checked for Event ID: " + eventId);
                }
            } else {
                System.out.println("Event not found.");
            }
        } catch (SQLException e) {
            System.out.println("Failed to track available seats.");
        }
    }

    void viewUpdateHistory() {
        updateHistory.printAll();
    }
}

class UserMenu extends Menu {
    public UserMenu(Connection connection, UpdateHistoryStack updateHistory) {
        super(connection, updateHistory);
    }

    void showMenu() {
        int choice;
        do {
            System.out.println("\n--- User Menu ---");
            System.out.println("1. View All Events");
            System.out.println("2. Register for Event");
            System.out.println("3. Rate and Review Event");
            System.out.println("4. View Upcoming Events");
            System.out.println("5. View Available Seats");
            System.out.println("0. Logout");
            System.out.print("Enter your choice: ");

            while (!sc.hasNextInt()) {
                System.out.print("Enter a valid number: ");
                sc.next();
            }
            choice = sc.nextInt();
            sc.nextLine();

            switch (choice) {
                case 1: viewAllEvents(); break;
                case 2: registerUserToEvent(); break;
                case 3: rateAndReviewEvent(); break;
                case 4:
                    EventManagementLinkedList es = new EventManagementLinkedList();
                    es.viewUpcomingEvents(); break;
                case 5: viewAvailableSeats(); break;
                case 0: System.out.println("Logging out..."); break;
                default: System.out.println("Invalid choice. Try again."); break;
            }
        } while (choice != 0);
    }

    void viewAvailableSeats() {
        try {
            System.out.print("Enter Event ID to check seats: ");
            int eventId;

            while (!sc.hasNextInt()) {
                System.out.println("Invalid input! Please enter a valid Event ID (number).");
                sc.next();
            }
            eventId = sc.nextInt();
            sc.nextLine();

            String query1 = "SELECT name, capacity FROM events WHERE id=?";
            PreparedStatement ps1 = connection.prepareStatement(query1);
            ps1.setInt(1, eventId);
            ResultSet rs1 = ps1.executeQuery();

            if (rs1.next()) {
                String eventName = rs1.getString("name");
                int capacity = rs1.getInt("capacity");

                String query2 = "SELECT COUNT(*) as count FROM users WHERE event_id=?";
                PreparedStatement ps2 = connection.prepareStatement(query2);
                ps2.setInt(1, eventId);
                ResultSet rs2 = ps2.executeQuery();

                if (rs2.next()) {
                    int registered = rs2.getInt("count");
                    int available = capacity - registered;

                    System.out.println("\nEvent: " + eventName);
                    System.out.println("Total Capacity: " + capacity);
                    System.out.println("Registered Users: " + registered);
                    System.out.println("Available Seats: " + available);

                    updateHistory.push("User checked seats for Event ID: " + eventId);
                }
            } else {
                System.out.println("Event not found! Please check the Event ID.");
            }
        } catch (SQLException e) {
            System.out.println("Error checking available seats. " + e.getMessage());
        }
    }


    void viewAllEvents() {
        try {
            String query = "SELECT * FROM events";
            Statement stmt = connection.createStatement();
            ResultSet rs = stmt.executeQuery(query);

            System.out.printf("\n%-5s %-20s %-12s %-15s %-30s %-10s\n",
                    "ID", "Name", "Date", "Location", "Description", "Capacity");
            System.out.println("-----------------------------------------------------------------------------------------------");

            while (rs.next()) {
                System.out.printf("%-5d %-20s %-12s %-15s %-30s %-10d\n",
                        rs.getInt("id"), rs.getString("name"), rs.getString("date"),
                        rs.getString("location"), rs.getString("description"), rs.getInt("capacity"));
            }
            updateHistory.push("Viewed All Events");
        } catch (SQLException e) {
            System.out.println("Failed to view events.");
        }
    }

    void registerUserToEvent() {
        try {
            System.out.print("Enter User Name: ");
            String name = sc.nextLine();

            String email;
            do {
                System.out.print("Enter User Email: ");
                email = sc.nextLine();
            } while (!email.matches("^[\\w.-]+@[\\w.-]+\\.\\w+$"));

            int eventId;
            while (true) {
                System.out.print("Enter Event ID to Register: ");
                if (sc.hasNextInt()) {
                    eventId = sc.nextInt();
                    sc.nextLine();
                    break;
                } else {
                    System.out.println("Invalid number.");
                    sc.next();
                }
            }

            String query = "INSERT INTO users (name, email, event_id) VALUES (?, ?, ?)";
            PreparedStatement ps = connection.prepareStatement(query);
            ps.setString(1, name);
            ps.setString(2, email);
            ps.setInt(3, eventId);
            ps.executeUpdate();

            updateHistory.push("Registered user: " + name + " to event ID: " + eventId);
            System.out.println("User registered to event successfully.");
        } catch (SQLException e) {
            System.out.println("Failed to register user.");
        }
    }

    void rateAndReviewEvent() {
        try {
            System.out.print("Enter User ID: ");
            int userId = sc.nextInt();

            System.out.print("Enter Event ID: ");
            int eventId = sc.nextInt();

            int rating;
            while (true) {
                System.out.print("Enter Rating (1–5): ");
                rating = sc.nextInt();
                if (rating >= 1 && rating <= 5) break;
                else System.out.println("Rating must be between 1 and 5.");
            }
            sc.nextLine();

            System.out.print("Enter Review Comment: ");
            String comment = sc.nextLine();

            String query = "INSERT INTO reviews (user_id, event_id, rating, comment) VALUES (?, ?, ?, ?)";
            PreparedStatement ps = connection.prepareStatement(query);
            ps.setInt(1, userId);
            ps.setInt(2, eventId);
            ps.setInt(3, rating);
            ps.setString(4, comment);

            ps.executeUpdate();
            updateHistory.push("User " + userId + " reviewed Event " + eventId + " with rating " + rating);
            System.out.println("Review submitted.");
        } catch (SQLException e) {
            System.out.println("Failed to add review.");
        }
    }
}

class EventManagementSystem {
    static final String adminPass = "admin123";

    public static void main(String[] args) {
        try {
            DatabaseHelper dbHelper = new DatabaseHelper();
            Connection connection = dbHelper.getConnection();
            UpdateHistoryStack updateHistory = new UpdateHistoryStack();
            Scanner sc = new Scanner(System.in);

            System.out.println("--- Welcome to Event Management System ---");
            System.out.print("Enter role (admin/user): ");
            String role = sc.nextLine().trim().toLowerCase();

            if (role.equals("admin")) {
                System.out.print("Enter password: ");
                String password = sc.nextLine().trim();

                if (password.equals(adminPass)) {
                    new AdminMenu(connection, updateHistory).showMenu();
                } else {
                    System.out.println("Invalid admin password. Exiting...");
                }

            } else if (role.equals("user")) {
                new UserMenu(connection, updateHistory).showMenu();

            } else {
                System.out.println("Invalid role entered. Exiting...");
            }

        } catch (SQLException e) {
            System.out.println("Connection Failed! Check output console");
        }
    }
}
