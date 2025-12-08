import java.lang.Exception;
import java.sql.*;
import java.util.Scanner;
import java.io.*;

class WeddingDatabaseApp {
    public static void main(String[] args) throws Exception {
        Class.forName("com.mysql.cj.jdbc.Driver");
        Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/1eshrvk", "root", "");

        Scanner sc = new Scanner(System.in);
        {
            while (true) {
                System.out.println("\n------ Menu ------");
                System.out.println("1. Press 1 to Insert data in database.");
                System.out.println("2. Press 2 to Update data in database.");
                System.out.println("3. Press 3 to Delete data from database.");
                System.out.println("4. Press 4 to Read data from database.");
                System.out.println("5. Press 5 to Get information about happyWedding table.");
                System.out.println("6. Press 6 to Exit.");

                int choice = sc.nextInt();

                switch (choice) {
                    case 1:
                        insertData(conn);
                        break;
                    case 2:
                        updateData(conn, sc);
                        break;
                    case 3:
                        deleteData(conn, sc);
                        break;
                    case 4:
                        readData(conn, sc);
                        break;
                    case 5:
                        getTableInfo(conn, sc);
                        break;
                    case 6:
                        System.exit(0);
                    default:
                        System.out.println("Invalid choice.");
                }
            }
        }
    }

    // Case 1
    @SuppressWarnings("CallToPrintStackTrace")
    private static void insertData(Connection conn) {
        String sql = "INSERT INTO happyWedding (id, name, age, salary, photo, description) VALUES (?, ?, ?, ?, ?, ?)";

        try (PreparedStatement ps = conn.prepareStatement(sql);
            FileInputStream photo = new FileInputStream("D:/Sasuke.jpg");
            FileReader desc = new FileReader("D://github-recovery-codes.txt")) {

            ps.setInt(1, 1); // id
            ps.setString(2, "Ravi"); // name
            ps.setInt(3, 28); // age
            ps.setDouble(4, 60000.50); // salary
            ps.setBinaryStream(5, photo);
            ps.setCharacterStream(6, desc);

            int result = ps.executeUpdate();
            System.out.println(result + " row inserted successfully.");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    // Case 2
    @SuppressWarnings("CallToPrintStackTrace")
    private static void updateData(Connection conn, Scanner sc) {
        System.out.print("Enter name: ");
        String name = sc.next();
        System.out.print("Enter new age: ");
        int age = sc.nextInt();
        System.out.print("Enter new salary: ");
        double salary = sc.nextDouble();

        String query = "UPDATE happyWedding SET age = " + age + ", salary = " + salary + " WHERE name = '" + name + "'";

        try (Statement stmt = conn.createStatement()) {
            int result = stmt.executeUpdate(query);
            System.out.println(result + " row(s) updated.");
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    // Case 3
    @SuppressWarnings("CallToPrintStackTrace")
    private static void deleteData(Connection conn, Scanner sc) {
        System.out.print("Enter ID to delete: ");
        int id = sc.nextInt();
        String sql = "DELETE FROM happyWedding WHERE id = ?";

        try (PreparedStatement ps = conn.prepareStatement(sql)) {
            conn.setAutoCommit(false);
            ps.setInt(1, id);
            ps.executeUpdate();

            System.out.print("Do you want to commit or rollback? (commit/rollback): ");
            String choice = sc.next();

            if (choice.equalsIgnoreCase("commit")) {
                conn.commit();
                System.out.println("Row deleted successfully.");
            } else {
                conn.rollback();
                System.out.println("Rollback done. No row deleted.");
            }
            conn.setAutoCommit(true);
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    // Case 4
    @SuppressWarnings("CallToPrintStackTrace")
    private static void readData(Connection conn, Scanner sc) {
        System.out.print("Enter age: ");
        int age = sc.nextInt();
        System.out.print("Enter salary: ");
        double salary = sc.nextDouble();

        String query = "SELECT * FROM happyWedding WHERE age = " + age + " AND salary = " + salary;

        try (Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(query)) {

            while (rs.next()) {
                System.out.println("ID: " + rs.getInt("id") +
                        ", Name: " + rs.getString("name") +
                        ", Age: " + rs.getInt("age") +
                        ", Salary: " + rs.getDouble("salary"));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    // Case 5
    @SuppressWarnings("CallToPrintStackTrace")
    private static void getTableInfo(Connection conn, Scanner sc) {
        System.out.print("Enter column index (starting from 1): ");
        int index = sc.nextInt();

        String sql = "SELECT * FROM happyWedding";

        try (PreparedStatement ps = conn.prepareStatement(sql);
             ResultSet rs = ps.executeQuery()) {

            ResultSetMetaData meta = rs.getMetaData();
            int columnCount = meta.getColumnCount();
            if (index < 1 || index > columnCount) {
                System.out.println("Invalid column index.");
                return;
            }

            System.out.println("Total Columns: " + columnCount);
            System.out.println("Column Name: " + meta.getColumnName(index));
            System.out.println("Column Type: " + meta.getColumnTypeName(index));

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
