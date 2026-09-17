#ifndef UNIVERSITY_H
#define UNIVERSITY_H

#include <string>
#include <iostream>

class Teacher {
public:
    std::string name;
    Teacher(std::string n = "Невідомий викладач");
    ~Teacher();
};

class RecordBook {
public:
    int bookNumber;
    RecordBook(int num = 0);
    ~RecordBook();
};

class Course {
public:
    std::string courseName;
    int credits;
    
    Teacher* courseTeacher; 

    Course(std::string name = "Невідомо", int cred = 0);
    ~Course();
    void assignTeacher(Teacher* t);
};

class Student {
private:
    std::string name_;
    
    const int studentId_;        
    int& admissionYearRef_;      
    
    RecordBook recordBook_;      

public:
    static int totalStudents;    

    Student(); 
    Student(std::string name, int id, int bookNum, int& yearRef); 
    Student(const Student& other); 
    
    ~Student();                  

    static void printTotalStudents(); 

    std::string getName() const;
    int getId() const;
};

class Exam {
public:
    static void conductExam(Student& s, Course& c, Teacher& t, int grade);
};

void calculateBonus(Student s);

void calculateBonus(Student* s);

Student createHonorStudent(Student s);

#endif // UNIVERSITY_H