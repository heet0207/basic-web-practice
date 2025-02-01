import java.util.*;

class Airline {
    String to, from, TO, FROM, Fname, Mname, Lname, seat_no, Mo_no, Duration, F_no = "AB1272";
    int date, month, year, person, i = 0, ticket_status;
    int flight_price, total_price, travel_insurance, ammount;
    boolean payment_method = true, ticket_booked = false;
    Airline[] a;

    String r1 = "AHMEDABAD", r2 = "MUMBAI", r3 = "DELHI", r4 = "BENGALURU", r5 = "KOLKATA", r6 = "HYDERABAD",
            r7 = "CHENNAI";

    void book_ticket() {
        Scanner sc = new Scanner(System.in);

        boolean route = true;
        while (route) {
            System.out.println("Here only 7 routes are availabale ");
            System.out.println(
                    "1." + r1 + "  2." + r2 + "  3." + r3 + "  4." + r4 + "  5." + r5 + "  6." + r6 + "  7." + r7);
            System.out.println();
            System.out.println("Enter a route name");
            boolean check_route = true;
            while (check_route) {
                System.out.print("TO   : ");
                to = sc.nextLine();
                TO = to.toUpperCase();
                TO = TO.replaceAll("\\s+", "");

                if (TO.equals(r1) || TO.equals(r2) || TO.equals(r3) || TO.equals(r4) || TO.equals(r5) || TO.equals(r6)
                        || TO.equals(r7)) {
                    check_route = false;
                } else {
                    System.out
                            .println("You have entered invalid route, Please enter Carefully as per Available Routes");
                }
            }
            check_route = true;

            while (check_route) {
                System.out.print("FROM : ");
                from = sc.nextLine();
                FROM = from.toUpperCase();
                FROM = FROM.replaceAll("\\s+", "");

                if (FROM.equals(r1) || FROM.equals(r2) || FROM.equals(r3) || FROM.equals(r4) || FROM.equals(r5)
                        || FROM.equals(r6) || FROM.equals(r7)) {
                    check_route = false;
                } else {
                    System.out
                            .println("You have entered invalid route, Please enter Carefully as per Available Routes");
                }
            }

            if (TO.equals(FROM)) {
                System.out.println("you have Entered Invalid Route, please enter carefully");
            } else {
                boolean mobile = true;
                while (mobile) {
                    System.out.println("\nEnter your mobile no.");
                    System.out.print("+91 ");
                    Mo_no = sc.next();
                    if (Mo_no.charAt(0) >= '7' && Mo_no.charAt(0) <= '9') {
                        if (Mo_no.length() == 10) {
                            int count = 0;
                            for (i = 0; i < 10; i++) {
                                if (Mo_no.charAt(i) >= '0' && Mo_no.charAt(i) <= '9') {
                                    if (i == 9)
                                        mobile = false;
                                } else {
                                    count++;
                                    break;
                                }
                            }
                            if (count > 0) {
                                System.out.println("Please enter correct Mobile no.");
                            }
                        } else {
                            System.out.println("Please enter correct mobile no.");
                        }
                    } else {
                        System.out.println("First digit of Mobile no. must be contain of 7,8 or 9 Only.");
                    }
                }
                boolean check = true;
                while (check) {
                    System.out.println("Enter a day");
                    date = sc.nextInt();
                    System.out.println("Enter a month");
                    month = sc.nextInt();
                    System.out.println("Enter a year");
                    year = sc.nextInt();

                    switch (month) {
                        case 1:
                        case 3:
                        case 5:
                        case 7:
                        case 8:
                        case 10:
                        case 12:
                            if ((date >= 1 && date <= 31) && year >= 2024) {
                                check = false;
                            } else {
                                System.out.println("You have entered innvalid date");
                            }
                            break;

                        case 4:
                        case 6:
                        case 9:
                        case 11:
                            if ((date >= 1 && date <= 30) && year >= 2024) {
                                check = false;
                            } else {
                                System.out.println("You have entered innvalid date");
                            }
                            break;

                        case 2:
                            if (((year % 400 == 0) || (year % 4 == 0 && year % 100 != 0)) && year >= 2024) {
                                if (date >= 1 && date <= 29) {
                                    check = false;
                                } else {
                                    System.out.println("you have entered Invalid date  Please enter carefully");
                                }
                            } else if ((date >= 1 && date <= 28) && year >= 2024) {
                                check = false;
                            } else {
                                System.out.println("You have entered innvalid year");
                            }
                            break;
                        default:
                            System.out.println("You have entered Invalid month  Please enter carefully");
                            break;
                    }

                }
                System.out.println("Enter a total number of person");
                person = sc.nextInt();

                a = new Airline[person];
                for (i = 0; i < person; i++) {
                    a[i] = new Airline();// start object creating
                    System.out.println("----------Enter a details for person " + (i + 1) + "----------");
                    a[i].details(); // call detail() function
                }
                System.out.println();
                int k = 1;
                char ch = 'A';
                for (int i = 1; i <= 10; i++)// This for loop make a flight seats pattern
                {

                    System.out.print(ch + "  ");
                    for (int j = 1; j <= 8; j++) {
                        if (k > 30) {
                            k = 1;
                        }
                        if ((j == 4) || (j == 5)) {
                            System.out.print("   ");
                        } else {
                            System.out.print(String.format("%02d", k));
                            System.out.print(" ");
                            k++;
                        }
                    }
                    ch++;
                    System.out.println();
                }
                for (i = 0; i < person; i++) {
                    System.out.println("Select a seat for Person " + (i + 1));
                    a[i].seat_selection();// call seat_selction() function
                }
                price_set();// call price set function
                route = false;
            }
        }
    }

    void details() {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter First name");
        Fname = sc.next();
        System.out.println("Enter a Middle name");
        Mname = sc.next();
        System.out.println("Enter a Last name ");
        Lname = sc.next();

    }

    void seat_selection() {
        Scanner sc = new Scanner(System.in);
        boolean seat = true;
        System.out.println("For example, A01, A02, A03...");

        while (seat) {
            System.out.println();

            seat_no = sc.nextLine();
            seat_no = seat_no.replaceAll("\\s+", "");// All spaces remove from seat_no
            seat_no = seat_no.toUpperCase();

            char ch = seat_no.charAt(0);// 1st character store in char ch i.e. A,B,C,D,....
            String s1 = Character.toString(ch);// 1st character converted in String
            String s2[] = seat_no.split(s1);// Split from 1st character
            String s3 = s2[1];// After splitting, 1st character stored in s2[0] and number like 01,02...
                              // stored in s[3] and that number will stored in String s3

            if (seat_no.charAt(0) == 'A' || seat_no.charAt(0) == 'F') {
                s3 = s3.replaceFirst("0", "");// remove 0 from 01 or 02 0r 03... and stored in String s3
            }
            if ((seat_no.charAt(0) == 'B' || seat_no.charAt(0) == 'G') && !s3.equals("10")) {
                s3 = s3.replaceFirst("0", "");
            }
            int s_no = Integer.parseInt(s3);

            if (seat_no.length() == 3 || seat_no.length() == 2) {
                if (seat_no.charAt(0) >= 'A' && seat_no.charAt(0) <= 'J') {
                    if ((seat_no.charAt(0) == 'A' || seat_no.charAt(0) == 'F') && (s_no >= 1 && s_no <= 6)) {
                        seat = false;
                    } else if ((seat_no.charAt(0) == 'B' || seat_no.charAt(0) == 'G') && (s_no >= 7 && s_no <= 12)) {
                        seat = false;
                    } else if ((seat_no.charAt(0) == 'C' || seat_no.charAt(0) == 'H') && (s_no >= 13 && s_no <= 18)) {
                        seat = false;
                    } else if ((seat_no.charAt(0) == 'D' || seat_no.charAt(0) == 'I') && (s_no >= 19 && s_no <= 24)) {
                        seat = false;
                    } else if ((seat_no.charAt(0) == 'E' || seat_no.charAt(0) == 'J') && (s_no >= 25 && s_no <= 30)) {
                        seat = false;
                    } else {
                        System.out.println("you have entered invalid seat number  please enter carefully");
                    }
                } else {
                    System.out.println("you have entered invalid series of seat no.  please enter carefully");
                }
            } else {
                System.out.println("you have entered invalid seat no.  please enter carefully");
            }

        }
    }

    void price_set() {
        Scanner sc = new Scanner(System.in);
        switch (TO) {
            case "MUMBAI":
                flight_price = 3500;
                Duration = "1h 30m | non stop";
                break;

            case "DELHI":
                flight_price = 4000;
                Duration = "1h 45m | non stop";
                break;

            case "BENGALURU":
                flight_price = 7000;
                Duration = "3h 15m | non stop";
                break;

            case "KOLKATA":
                flight_price = 9000;
                Duration = "5h 50m | 1 stop(DEL)";
                break;

            case "HYDERABAD":
                flight_price = 6500;
                Duration = "1h 40m | non stop";
                break;

            case "CHENNAI":
                flight_price = 8000;
                Duration = "5h 45m | 1 stop(BOM)";
                break;

            default:
                flight_price = 4500;
                Duration = "2h 45m | non stop";
                break;
        }
        System.out.println(FROM + " TO " + TO + " Ticket Price per person : " + flight_price + "/-");
        total_price = flight_price * person;
        System.out.println("TOTAL Price : " + total_price + "/-");
        System.out.println("Travelling duration : " + Duration);
        System.out.println(
                "\nDo you want to get Travel insurance ?\nIf you have travel insurance , when you will cancel the ticket you will get full refund of your Total price");
        System.out.println("\nTo get Travel insurance, you have to pay 800/- Rupees");

        boolean insurance_choice = true;
        while (insurance_choice) {
            System.out.println("Press 1 for Yes \nPress 2 for No\n\nEnter your choice.");
            travel_insurance = sc.nextInt();
            if (travel_insurance == 1) {
                System.out.println("If you will cancel your ticket, You will get " + total_price + "/- Refund");
                total_price = total_price + 800;
                insurance_choice = false;
            } else if (travel_insurance == 2) {

                System.out.println("If you will cancel your ticket, You will get "
                        + (total_price - ((35 * total_price) / 100)) + "/- Refund");
                insurance_choice = false;
            } else {
                System.out.println("You have entered invalid choice , please enter correct choice");
            }
        }
        payment();
    }

    void payment() {
        Scanner sc = new Scanner(System.in);
        System.out.println(
                "\nHere total 3 types of payment method avaliable\nPress 1 for credit card\nPress 2 for Debit card\nPress 3 for UPI");
        int pay = sc.nextInt();

        boolean credit = true;
        boolean debite = true;
        boolean UPI = true;
        boolean debite_check = true;
        int n = 0;
        while (payment_method) {
            switch (pay) {
                case 1:

                    while (credit) {

                        System.out.println("Enter your credit card number");
                        String credit_no = sc.next();
                        if (credit_no.length() == 16) {
                            for (i = 0; i < 16; i++) {
                                if (credit_no.charAt(i) >= '0' && credit_no.charAt(i) <= '9') {
                                    if (i == 15) {
                                        credit = false;
                                    }
                                    continue;
                                } else {
                                    System.out.println("Please enter correct Credit card no.");
                                    break;
                                }
                            }
                        } else {
                            System.out.println("Credit card no. length must be of 16 digits only");
                        }
                    }
                    if (i == 16) {
                        System.out.println("You have to pay " + total_price + "/- to book a ticket");
                        System.out.println("Enter ammount to pay ticket price");
                        ammount = sc.nextInt();
                        if (ammount == total_price) {
                            System.out.println("Transaction successfull");
                            payment_method = false;
                            ticket_booked = true;
                            ticket_status = 1;
                        } else {
                            System.out.println("You have entered insufficient amount , please enter sufficient amount");
                        }
                    }
                    break;

                case 2:
                    // int n = 0;
                    while (debite_check) {

                        System.out.println("Enter your Debit card number");
                        String debite_no = sc.next();
                        if (debite_no.length() == 12) {
                            for (int k = 0; k < 12; k++) {
                                if (debite_no.charAt(k) >= '0' && debite_no.charAt(k) <= '9') {
                                    if (k == 11) {
                                        debite_check = false;
                                    }
                                    continue;
                                } else {
                                    System.out.println("Please enter correct Debit card no.");
                                    break;
                                }
                            }
                        } else {
                            System.out.println("Debit card no. length must be of 12 digits only");
                        }
                    }
                    while (debite) {

                        System.out.println("Enter your Debit card Password");
                        String debite_password = sc.next();
                        n = debite_password.length();
                        if (n == 6 || n == 4) {
                            for (i = 0; i < n; i++) {
                                if (debite_password.charAt(i) >= '0' && debite_password.charAt(i) <= '9') {
                                    if (i == (n - 1)) {
                                        debite = false;
                                    }
                                    continue;
                                } else {
                                    System.out.println("Please enter correct Debit card password");
                                    break;
                                }
                            }
                        } else {
                            System.out.println("Debit card password length must be of 4 or 6 digits only");
                        }
                    }
                    if (i == n) {
                        System.out.println("You have to pay " + total_price + "/- to book a ticket");
                        System.out.println("Enter ammount for pay ticket price");
                        ammount = sc.nextInt();
                        if (ammount == total_price) {
                            System.out.println("Transaction succesfull");
                            payment_method = false;
                            ticket_booked = true;
                            ticket_status = 1;
                        } else {
                            System.out.println("You have entered insufficient amount , please enter sufficient amount");
                        }
                    }
                    break;

                case 3:
                    while (UPI) {
                        System.out.println("Enter your UPI ID");
                        String UPI_ID = sc.next();
                        if (UPI_ID.length() >= 5) {
                            UPI = false;
                        } else {
                            System.out.println("You have entered incorrect UPI id , please enter carefully");
                        }
                    }
                    System.out.println("You have to pay " + total_price + "/- to book a ticket");
                    System.out.println("Enter amount for pay ticket price");
                    ammount = sc.nextInt();
                    if (ammount == total_price) {
                        System.out.println("Transaction succesfull");
                        payment_method = false;
                        ticket_booked = true;
                        ticket_status = 1;
                    } else {
                        System.out.println("You have entered insufficient amount , please enter sufficient amount");
                    }
                    break;

                default:
                    System.out.println("Invalid choice, please Enter a valid choice");
                    break;
            }
        }

    }

    void show_ticket() {
        System.out.println();
        if (ticket_booked && ticket_status == 1) {
            System.out.print("------------------TICKET CONFIRMATION------------------\n");
            System.out.println(FROM + "            TO            " + TO);
            System.out.println("Flight no : " + F_no);
            for (int k = 0; k < person; k++) {
                System.out.println("\nName   : " + a[k].Fname + " " + a[k].Mname + " " + a[k].Lname);
                System.out.println("Seat no: " + a[k].seat_no);
            }
            System.out.println("Mobile No : " + Mo_no);
            System.out.println("Date  : " + date + "/" + month + "/" + year);
            if (travel_insurance == 1) {
                System.out.println("Insurance Status : YES");
            } else {
                System.out.println("Insurance Status : NO");
            }
            System.out.println("Duration  : " + Duration);
            System.out.println("\n--------------------HAPPY JOURNEY--------------------");
        } else {
            System.out.println("You haven't booked Ticket, please book your ticket first.");
        }
    }

    void cancle_ticket() {
        Scanner sc = new Scanner(System.in);
        if (ticket_booked && ticket_status == 1) {
            System.out.println();
            boolean cancle_check = true;
            System.out.println("Are you sure want to cancle a booking?");
            while (cancle_check) {
                System.out.println("Press 1 for Yes\nPress 2 for No");
                int cancle_choice = sc.nextInt();
                switch (cancle_choice) {
                    case 1:
                        if (travel_insurance == 1) {
                            System.out.println("Okay, you will get " + (total_price - 800) + "/- Refund");
                            ++ticket_status;
                            cancle_check = false;
                        } else {
                            System.out.println(
                                    "Okay, you will get " + (total_price - ((35 * total_price) / 100)) + "/- Refund");
                            ++ticket_status;
                            cancle_check = false;
                        }
                        break;

                    case 2:
                        cancle_check = false;
                        break;

                    default:
                        System.out.println("\nPlease, Enter a correct choice");
                        break;
                }
            }
        } else {
            System.out.println("\nYou haven't booked Ticket, please book your ticket.");
        }
    }
}

class Airplane {
    public static void main(String args[]) {
        String UID, Password, Confirm_Password;
        Scanner sc = new Scanner(System.in);
        Airline air = new Airline();

        System.out.println("--------------- Login Page ---------------\n");
        System.out.println("Create your userId.\nuserId length must be greater than or equal to 7");
        boolean UID_length = true, check_Password = true;
        while (UID_length) {
            System.out.print("UserId : ");
            UID = sc.next();
            if (UID.length() >= 7) {
                System.out.println(
                        "\nCreate your Password\nPassword length mustbe greater than or equal to 4 and less than or equal to 8\n");
                System.out.print("Password : ");
                Password = sc.next();

                if (Password.length() >= 4 && Password.length() <= 8) {
                    while (check_Password) {
                        System.out.print("Enter confirm password : ");
                        Confirm_Password = sc.next();

                        if (Password.equals(Confirm_Password)) {
                            check_Password = false;
                            UID_length = false;
                        } else {
                            System.out.println("Password & Confirm Password must be same, Please enter carefully");
                        }
                    }
                } else {
                    System.out.println("Invalid Password length, Please enter carefully.");
                }
            } else {
                System.out.println("Invalid userId length, Please enter carefully.");
            }
        }

        System.out
                .println("\n--------------------WELCOME TO THE INDIAN AIRLINE RESERVATION SYSTEM--------------------");

        boolean b = true;
        while (b) {
            System.out.println("\nPress 1 to book a flight ticket");
            System.out.println("Press 2 to see your flight ticket");
            System.out.println("Press 3 to cancel your flight ticket");
            System.out.println("Press 4 to exit from the System\n");

            System.out.println("Enter your choice");
            int choice = sc.nextInt();

            switch (choice) {
                case 1:
                    air.book_ticket();
                    break;

                case 2:
                    air.show_ticket();
                    break;

                case 3:
                    air.cancle_ticket();
                    break;

                case 4:
                    b = false;
                    System.out.println("Thank You for visiting");
                    break;

                default:
                    System.out.println("You have Entered invalid choice, Please enter correct choice.");
                    break;
            }
        }
    }
}