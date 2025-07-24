import java.sql.*;
import java.util.*;

class Event {
    int eventId;
    String eventName;
    String eventDate;
    String eventLocation;

    Event(int id, String name, String date, String location) {
        this.eventId = id;
        this.eventName = name;
        this.eventDate = date;
        this.eventLocation = location;
    }
}

class User {
    int userId;
    String userName;
    String userEmail;
    int registeredEventId;

    User(int id, String name, String email, int eventId) {
        this.userId = id;
        this.userName = name;
        this.userEmail = email;
        this.registeredEventId = eventId;
    }
}

class EventManagementSystem {
    Connection databaseConnection;
    Scanner inputScanner;
    List<Event> listOfEvents;
    List<User> listOfUsers;
    Map<Integer, Event> mapOfEventsById;
    Map<Integer, List<User>> mapOfUsersByEventId;

    EventManagementSystem() {
        inputScanner = new Scanner(System.in);
        listOfEvents = new ArrayList<Event>();
        listOfUsers = new ArrayList<User>();
        mapOfEventsById = new HashMap<Integer, Event>();
        mapOfUsersByEventId = new HashMap<Integer, List<User>>();
    }

    void startSystem() {
        try {
            databaseConnection = DriverManager.getConnection("jdbc:mysql://localhost:3306/event_management","root","");

            loadEventsFromDatabase();
            loadUsersFromDatabase();

            while (true) {
                System.out.println("Event Management System");
                System.out.println("1. Create New Event");
                System.out.println("2. View All Events");
                System.out.println("3. Register User for Event");
                System.out.println("4. View All Users");
                System.out.println("5. Exit Program");
                System.out.print("Enter your choice: ");

                String choiceInput = inputScanner.nextLine();
                int userChoice = Integer.parseInt(choiceInput);

                if (userChoice == 1) {
                    createNewEvent();
                } else if (userChoice == 2) {
                    displayAllEvents();
                } else if (userChoice == 3) {
                    registerUserToEvent();
                } else if (userChoice == 4) {
                    displayAllUsers();
                } else if (userChoice == 5) {
                    databaseConnection.close();
                    break;
                } else {
                    System.out.println("Invalid choice. Please try again.");
                }
            }

        } catch (Throwable exception) {
            exception.printStackTrace();
        }
    }

    void loadEventsFromDatabase() throws SQLException {
        listOfEvents.clear();
        mapOfEventsById.clear();

        String query = "SELECT * FROM events";
        Statement statement = databaseConnection.createStatement();
        ResultSet resultSet = statement.executeQuery(query);

        while (resultSet.next()) {
            int id = resultSet.getInt("id");
            String name = resultSet.getString("name");
            String date = resultSet.getString("date");
            String location = resultSet.getString("location");

            Event event = new Event(id, name, date, location);
            listOfEvents.add(event);
            mapOfEventsById.put(id, event);
        }
    }

    void loadUsersFromDatabase() throws SQLException {
        listOfUsers.clear();
        mapOfUsersByEventId.clear();

        String query = "SELECT * FROM users";
        Statement statement = databaseConnection.createStatement();
        ResultSet resultSet = statement.executeQuery(query);

        while (resultSet.next()) {
            int id = resultSet.getInt("id");
            String name = resultSet.getString("name");
            String email = resultSet.getString("email");
            int eventId = resultSet.getInt("event_id");

            User user = new User(id, name, email, eventId);
            listOfUsers.add(user);

            if (!mapOfUsersByEventId.containsKey(eventId)) {
                mapOfUsersByEventId.put(eventId, new ArrayList<User>());
            }
            mapOfUsersByEventId.get(eventId).add(user);
        }
    }

    void createNewEvent() throws SQLException {
        System.out.print("Enter event name: ");
        String name = inputScanner.nextLine();

        System.out.print("Enter event date (YYYY-MM-DD): ");
        String date = inputScanner.nextLine();

        System.out.print("Enter event location: ");
        String location = inputScanner.nextLine();

        String insertQuery = "INSERT INTO events (name, date, location) VALUES (?, ?, ?)";
        PreparedStatement preparedStatement = databaseConnection.prepareStatement(insertQuery);
        preparedStatement.setString(1, name);
        preparedStatement.setString(2, date);
        preparedStatement.setString(3, location);
        preparedStatement.executeUpdate();

        System.out.println("Event has been added.");

        loadEventsFromDatabase();
    }

    void displayAllEvents() {
        for (Event event : listOfEvents) {
            System.out.println("Event ID: " + event.eventId);
            System.out.println("Name: " + event.eventName);
            System.out.println("Date: " + event.eventDate);
            System.out.println("Location: " + event.eventLocation);
            System.out.println();
        }
    }

    void registerUserToEvent() throws SQLException {
        displayAllEvents();

        System.out.print("Enter Event ID to register for: ");
        int eventId = Integer.parseInt(inputScanner.nextLine());

        if (!mapOfEventsById.containsKey(eventId)) {
            System.out.println("Event ID does not exist.");
            return;
        }

        System.out.print("Enter user name: ");
        String userName = inputScanner.nextLine();

        System.out.print("Enter user email: ");
        String userEmail = inputScanner.nextLine();

        String insertQuery = "INSERT INTO users (name, email, event_id) VALUES (?, ?, ?)";
        PreparedStatement preparedStatement = databaseConnection.prepareStatement(insertQuery);
        preparedStatement.setString(1, userName);
        preparedStatement.setString(2, userEmail);
        preparedStatement.setInt(3, eventId);
        preparedStatement.executeUpdate();

        System.out.println("User has been registered to the event.");

        loadUsersFromDatabase();
    }

    void displayAllUsers() {
        for (Event event : listOfEvents) {
            System.out.println("Event: " + event.eventName);

            List<User> usersForEvent = mapOfUsersByEventId.getOrDefault(event.eventId, new ArrayList<User>());

            if (usersForEvent.isEmpty()) {
                System.out.println("No users registered for this event.");
            } else {
                for (User user : usersForEvent) {
                    System.out.println("User ID: " + user.userId);
                    System.out.println("Name: " + user.userName);
                    System.out.println("Email: " + user.userEmail);
                    System.out.println();
                }
            }
        }
    }
}

class eventManagementSystem {
    public static void main(String[] args) {
        EventManagementSystem eventSystem = new EventManagementSystem();
        eventSystem.startSystem();
    }
}
