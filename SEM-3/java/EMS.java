import java.util.*;
import java.sql.*;

class EMS {

}

class Event1{
   int EventId;
   String EventName;
   String EventDate;
   String EventLocation;

   Event1(int id,String name,String date,String location){
       this.EventId = id;
       this.EventName = name;
       this.EventDate = date;
       this.EventLocation = location;
   }
}

class User1{
    int UserId;
    String UserName;
    String UserEmail;
    int RegisterEventId;

    User1(int uid,String uname,String uemail,int registereid){
        this.UserId = uid;
        this.UserName = uname;
        this.UserEmail = uemail;
        this.RegisterEventId = registereid;
    }

}

class EventManagementSystem1{
    Connection DataBaseConnection;
    Scanner inputScanner;
    List<Event1> ListOfEvents;
    List<User1> ListOfUsers;
    HashMap<Integer, Event1> MapOfEventById;
    Map<Integer ,List<User1>> MapOfUserByEventId;

    EventManagementSystem1() {
        inputScanner = new Scanner(System.in);
        ListOfEvents = new ArrayList<Event1>();
        ListOfUsers = new ArrayList<User1>();
        MapOfEventById = new HashMap<Integer, Event1>();
        MapOfUserByEventId = new HashMap<Integer, List<User1>>();
    }

    void startSystem() throws SQLException {
        DataBaseConnection = DriverManager.getConnection("jdbc:mysql://localhost:3306/1eshrvk","root","");
    }

}