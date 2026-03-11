import java.sql.*;

class UpdateHistoryStack {
    int size = 1000;
    String[] history;
    int top;

    UpdateHistoryStack() {
        history = new String[size];
        top = -1;
    }

    void push(String update) {
        if (top == size - 1) {
            System.out.println("History is full. Cannot add more updates.");
            return;
        }
        top++;
        history[top] = update;
    }

    void printAll() {
        if (top == -1) {
            System.out.println("No updates in history.");
            return;
        }
        System.out.println("--- Update History ---");
        for (int i = 0; i <= top; i++) {
            System.out.println((i + 1) + ". " + history[i]);
        }
    }
}

class EventManagementLinkedList {
    static final String URL = "jdbc:mysql://localhost:3306/event_management";
    static final String USER = "root";
    static final String PASSWORD = "";

    static class EventNode {
        int id;
        String name;
        String date;
        String location;
        String description;
        EventNode next;

        EventNode(int id, String name, String date, String location, String description) {
            this.id = id;
            this.name = name;
            this.date = date;
            this.location = location;
            this.description = description;
            this.next = null;
        }
    }

    static class EventLinkedList {
        private EventNode head;

        public void add(EventNode newNode) {
            if (head == null) {
                head = newNode;
            } else {
                EventNode temp = head;
                while (temp.next != null) {
                    temp = temp.next;
                }
                temp.next = newNode;
            }
        }

        public void display() {
            if (head == null) {
                System.out.println("\nNo upcoming events.");
                return;
            }

            // Print table header
            System.out.printf("\n%-5s %-20s %-12s %-15s %-30s\n",
                    "ID", "Name", "Date", "Location", "Description");
            System.out.println("------------------------------------------------------------------------------------------");

            // Print rows
            EventNode temp = head;
            while (temp != null) {
                System.out.printf("%-5d %-20s %-12s %-15s %-30s\n",
                        temp.id, temp.name, temp.date, temp.location, temp.description);
                temp = temp.next;
            }
        }
    }

    public void viewUpcomingEvents() {
        EventLinkedList list = new EventLinkedList();

        try (Connection connection = DriverManager.getConnection(URL, USER, PASSWORD)) {
            String query = "SELECT * FROM events WHERE date >= CURDATE() ORDER BY date";
            PreparedStatement ps = connection.prepareStatement(query);
            ResultSet rs = ps.executeQuery();

            while (rs.next()) {
                int id = rs.getInt("id");
                String name = rs.getString("name");
                String date = rs.getString("date");
                String location = rs.getString("location");
                String description = rs.getString("description");

                EventNode node = new EventNode(id, name, date, location, description);
                list.add(node);
            }

            list.display();

        } catch (SQLException e) {
            System.out.println("Database error: " + e.getMessage());
        }
    }
}

