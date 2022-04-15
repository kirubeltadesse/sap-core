# sap-web
Scholar Academy  Project

# Scholars-Academy-Overview

Object Model Diagram
- interface/transitional class
- Database 

```mermaid
 classDiagram

    User <-- SignIn
    User <-- Student
    User <-- Mentor
    User <-- Admin
    Mentor *-- WeekEntry
    Student -- Calendar
    Mentor -- Calendar
    Admin -- Calendar
    Admin -- Mentor
    Student -- Event

    class Admin
    Admin: +string name 
    Admin: +string email
    Admin: +int jNumber
    Admin: +string role
    Admin: string addMentor()
    Admin: Calendar getCalendarView()
    Admin: string changeTimeSlat(string mentor)

    class User
    User: +string fullname 
    User: +string userName 
    User: +string password 
    User: +string email
    User: +int jNumber
    User: +string role
    User: string changeName()

    class Event
    Event: +string mentorName 
    Event: +string studnetName 
    Event: +date startDate
    Event: +date endDate
    Event: +void sendEmail(string mentorEmail, string studentEmail)

    class Mentor
    Mentor: +string name 
    Mentor: +date timeSlot
    Mentor: +string courses 
    Mentor: Calendar getCalendarView()

    class Calendar
    Calendar: +vector<Mentors> getMentors()
    Calendar: +vector timeSlots 


    class Student
    Student: +string role
    Student: Calendar getCalendarView()
    Student: string createEvent()
    Student: string setRole()

    class WeekEntry
    WeekEntry: -string days 
    WeekEntry: -Date startTime 
    WeekEntry: -Date endTime 

    class SignIn
    SignIn: +string userName
    SignIn: +string password



```

Sequence Diagram for Admin

```mermaid 
sequenceDiagram
    actor Admin
    Admin->>+signIn/signUp: getUser() 
    signIn/signUp-->>-Admin: successfully login / error response
    Admin->>+CalendarView: getCaldentView() 
    CalendarView-->>-Admin: weekView() / error response
    Admin->>+addMentor: create mentor class 
    addMentor-->>-Admin: Mentor has been added / error response
    Admin->>+CalendarView: changeTimeSlot   
    CalendarView-->>-Admin: schedule updated! / error response
    Admin->>+Logout: logout 
    Logout-->>-Admin: logout / error response
```


Sequence Diagram for Mentor

```mermaid 
sequenceDiagram
    actor Mentor
    Mentor->>+signIn/signUp: getUser() 
    signIn/signUp-->>-Mentor: successfully login / error response
    signIn/signUp->>+CalendarView: getCaldentView() 
    CalendarView-->-Mentor: weekView() / error response
    Mentor->>+CalendarView: changeTimeSlot   
    CalendarView-->>+Mentor: schedule updated! / error response
    Mentor->>+Logout: logout 
    Logout-->>-Mentor: logout / error response
```




Sequence Diagram for Student

```mermaid 
sequenceDiagram
    actor Student
    Student->>+signIn/signUp: getUser() 
    signIn/signUp-->>-Student: successfully login / error response
    signIn/signUp->>+CalendarView: getCaldentView() 
    CalendarView-->>-Student: weekView() / error response 
    CalendarView->>+Event: schedule event() / error response 
    Event-->>-Student: your appointment has be scheduled / error response 
    Student->>+Logout: logout 
    Logout-->>-Student: logout / error response 
```
