# ER Diagram

### Entities are

   USER | STUDENT | MENTOR | SIGN IN | EVENTS | CALENDAR.  
    The USER can be either a student, a mentor or admin
    which is assigned by the 'role' attribute in the user table.
  Events is transaction that is posted when     a   student is
   booked for mentorship program.

```mermaid
  erDiagram
          USER ||--|| STUDENT : is 
          USER ||--|| MENTOR : is
          USER ||--|| SIGNIN : has
          STUDENT ||--o{ EVENTS : posts
          STUDENT ||--|| CALENDAR : has
          MENTOR ||--|| CALENDAR : has
        USER {
            int user_id PK
            string fullName
            int jNumber
            string email
            string role
            string userName
            string password
        }
        STUDENT {
            int student_id PK
            int user_id FK
        }
        MENTOR {
            int mentor_id PK
            int user_id FK
            string courses
        }
        SIGNIN {
            int signIn_id PK
            int user_id FK
            string userName
            string password    
        }
        EVENTS {
            int events_id PK
            int mentor_id FK
            int student_id FK
            dateFormat startDate
            dateFormat endDate
        }
        CALENDAR {
            int calendar_id PK
            int user_id FK
            dateFormat assignedDate
            dateFormat startDate
            dateFormat endDate
        }
        
```
