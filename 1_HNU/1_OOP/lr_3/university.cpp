#include "university.h"

int defaultYear = 2026;

int Student::totalStudents = 0; 

Teacher::Teacher(std::string n) : name(n) {}
Teacher::~Teacher() { std::cout << "\t[~] Знищено викладача: " << name << "\n"; }

RecordBook::RecordBook(int num) : bookNumber(num) {}
RecordBook::~RecordBook() {  }

Course::Course(std::string name, int cred) : courseName(name), credits(cred), courseTeacher(nullptr) {}
Course::~Course() { std::cout << "\t[~] Знищено курс: " << courseName << "\n"; }

void Course::assignTeacher(Teacher* t) { 
    courseTeacher = t; 
    std::cout << "\t[+] Викладача " << t->name << " призначено на курс " << courseName << " (Агрегація)\n"; 
}

// РЕАЛІЗАЦІЯ СТУДЕНТА (Конструктори та інше)

Student::Student() 
    : name_("Анонім"), studentId_(0), admissionYearRef_(defaultYear), recordBook_(0) {
    totalStudents++;
    std::cout << "\t[+] (Конструктор без параметрів) Створено: " << name_ << "\n";
}

Student::Student(std::string name, int id, int bookNum, int& yearRef)
    : name_(name), studentId_(id), admissionYearRef_(yearRef), recordBook_(bookNum) {
    totalStudents++;
    std::cout << "\t[+] (Конструктор з параметрами) Створено: " << name_ << " [ID: " << studentId_ << "]\n";
}

Student::Student(const Student& other)
    : name_(other.name_ + " (Копія)"), studentId_(other.studentId_), admissionYearRef_(other.admissionYearRef_), recordBook_(other.recordBook_.bookNumber) {
    totalStudents++;
    std::cout << "\t[+] (Конструктор копіювання) Скопійовано студента: " << name_ << "\n";
}

Student::~Student() {
    totalStudents--;
    std::cout << "\t[~] Деструктор (Вихід з блоку): Знищено студента " << name_ << "\n";
}

void Student::printTotalStudents() {
    std::cout << "\t[*] Загальна кількість студентів (Static method): " << totalStudents << "\n";
}

std::string Student::getName() const { return name_; }
int Student::getId() const { return studentId_; }

void Exam::conductExam(Student& s, Course& c, Teacher& t, int grade) {
    std::cout << "\t[!] (Асоціація) Студент " << s.getName() << " склав іспит з курсу [" 
              << c.courseName << "] у викладача " << t.name << " на оцінку " << grade << ".\n";
}

void calculateBonus(Student s) {
    std::cout << "\t[*] (За значенням) Розрахунок бонусу для " << s.getName() << ": 500 грн.\n";
}

void calculateBonus(Student* s) {
    std::cout << "\t[*] (За вказівником) Розрахунок підвищеного бонусу для " << s->getName() << ": 1500 грн!\n";
}

Student createHonorStudent(Student s) {
    std::cout << "\t[*] (Повернення об'єкта) Переведення в магістратуру...\n";
    return s;
}