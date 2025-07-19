import java.sql.*;

class j1 {
    public static void main(String[] args) throws Throwable {
        Class.forName("com.mysql.n
        jdbc.Driver");
        Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/1eshrvk", "root", "");

        System.out.println(con != null ? "Connection Successful" : "Connection Failed");

        String Create = "CREATE TABLE STUDENT (SID INT ,SNAME VARCHAR(50),SMARK DOUBLE)";

        Statement st = con.createStatement();
        st.executeUpdate(Create);

        int r = st.executeUpdate(Create);

        System.out.println(r > 0 ? "Success" : "Failed");
    }
}
