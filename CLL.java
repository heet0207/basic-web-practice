import java.lang.Exception;
import java.sql.*;
import java.util.Scanner;
import java.io.*;
class Managnment {
    public static void main(String[] args) throws Exception {
        Class.forName("com.mysql.cj.jdbc.Driver");
        Connection con =
                DriverManager.getConnection("jdbc:mysql://localhost:3306/lju", "root",
                        "");
        String sql = "select * from faculty where facid = 1";
        PreparedStatement pst = con.prepareStatement(sql);
        ResultSet rs = pst.executeQuery();
        System.out.print(rs.getInt(1));
        System.out.print(rs.getString(2));
        System.out.print(rs.getFloat(3));
        System.out.print(rs.getString(4));
    }
}