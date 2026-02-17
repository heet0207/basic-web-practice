#include <iostream>
#include <string>
using namespace std;

class Book {
private:
    const string ISBN;
    const string title;
    const string author;
    const string publicationDate;
    const double price;
    static int totalBooks;

public:
    Book(string isbn, string t, string a, string pubDate, double p)
        : ISBN(isbn), title(t), author(a), publicationDate(pubDate), price(p) {
        totalBooks++;
    }

    static int getTotalBooks() {
        return totalBooks;
    }

    virtual void displayBookDetails() const {
        cout << "ISBN: " << ISBN << endl;
        cout << "Title: " << title << endl;
        cout << "Author: " << author << endl;
        cout << "Publication Date: " << publicationDate << endl;
        cout << "Price: $" << price << endl;
    }

    virtual ~Book() {}
};

int Book::totalBooks = 0;

class Novel : public Book {
private:
    const string genre;

public:
    Novel(string isbn, string t, string a, string pubDate, double p, string g)
        : Book(isbn, t, a, pubDate, p), genre(g) {}

    void displayBookDetails() const override {
        Book::displayBookDetails();
        cout << "Genre: " << genre << endl;
    }
};

class Textbook : public Book {
private:
    const string subject;
    const int classNumber;

public:
    Textbook(string isbn, string t, string a, string pubDate, double p, string s, int cn)
        : Book(isbn, t, a, pubDate, p), subject(s), classNumber(cn) {}

    void displayBookDetails() const override {
        Book::displayBookDetails();
        cout << "Subject: " << subject << endl;
        cout << "Class Number: " << classNumber << endl;
    }
};

class BookBorrower {
private:
    const string borrowerID;
    const string borrowerName;
    const string address;
    const string phoneNumber;

public:
    BookBorrower(string id, string name, string addr, string phone)
        : borrowerID(id), borrowerName(name), address(addr), phoneNumber(phone) {}

    void displayBorrowerDetails() const {
        cout << "Borrower ID: " << borrowerID << endl;
        cout << "Borrower Name: " << borrowerName << endl;
        cout << "Address: " << address << endl;
        cout << "Phone Number: " << phoneNumber << endl;
    }
};
