# Calendar View

## What is an API End points

An API endpoint is a point at which an API (the code that allows two software programs to communicate with each other) connects with the software program. APIs work by sending *requests*
for information from a web application or web server and receiving a *response*.

### **How API endpoints work**

One side sends the information to the API and is called the [server](https://www.techtarget.com/searchnetworking/definition/client-server). The other side, the client, makes the requests and manipulates the API. The server side that provides the requested information, or resources, is the API endpoint.

![Project container structure](/Doc/img/projectContainersSetup.PNG)

In our case the client is going to be **Student, Mentor and Admin** as seen in the class diagram.

### API connection

After creating the API locally, it will be hosted on an api hosting platform. Swagger is not only good for documenting the API but also has features for running and testing the API. The API should be able to respond to requests as seen below.

When making GET request to the link, the API responds with the following JSON data

### [Base URL: scholarsacademyprojectapi.com/v1]

<details>
<summary>Admin</summary>

<details>

<summary>
GET       /admin/login       Logs admin into the system
</summary>

### Parameters

| Name | Description |
| ---- | ----------- |
| username(required)
string | The user name used for login |
| password(required)
string | The password used for login |

### Responses

| Code | Description               |
| ---- | ------------------------- |
| 200  | Successful Operation      |
| 400  | Invalid username/password |

```json
{
    "code": 200,
    "request": "admin_login",
    "message": "Successfully Logged In!"
}
```

```json
{
    "code": 400,
    "request": "admin_login",
    "message": "Invalid username or password. Please check try again"
}
```

</details>
<details>
<summary>
GET       /admin/getCalendarView       Gets the Calendar data
</summary>

### Parameters

    No Parameters needed.

### Responses

| Code | Description          |
| ---- | -------------------- |
| 200  | Successful Operation |

```json
{
  name:"Dinaol Tadesse",
     courses:{"csc 118","calculus"},
     calendar: {
    { 
     {"Tuesday","Thursday"},
              startTime:"00:12:00",
              endTime:"00:13:00"
   },
           { 
      {"Monday","Wednesday"},
              startTime:"00:07:00",
              endTime:"00:09:00"
  }
 }
}
```

</details>

<details>
<summary>
POST     /admin/addMentor       Adds New Mentor to Database
</summary>

### Parameters

| Name | Description |
| ---- | ----------- |
| body(required)
object | New Mentor Object. |

Example body value:

```json
{         
 name:"Dinaol Tadesse",
     courses:{"csc 118","calculus"},
     calendar: { 
   { 
    {"Tuesday","Thursday"},
            startTime:"00:12:00",
            endTime:"00:13:00"
  },
        { 
   {"Monday","Wednesday"},
            startTime:"00:07:00",
            endTime:"00:09:00"
  }
 }
}
```

### Responses

| Code | Description               |
| ---- | ------------------------- |
| 200  | Successful Operation      |
| 400  | Invalid Schedule supplied |

</details>

<details>
<summary>
PUT       /admin/changeSchedule       Updates the Schedule of Existing Mentor
</summary>

### Parameters

| Name | Description |
| ---- | ----------- |
| jNumber(required)
Int | The J number of the Mentor User |
| body(required)
object | Updated user Object. |

Example body value:

```json
{        
 name:"Dinaol Tadesse",
    courses:{"CSC 118","Data Structures"},
    calendar: { 
  { 
   {"Tuesday","Thursday"},
            startTime:"00:12:00",
            endTime:"00:13:00"
  },
        { 
   {"Monday","Wednesday"},
            startTime:"00:07:00",
            endTime:"00:09:00"
  }
 }
}
```

### Responses

| Code | Description               |
| ---- | ------------------------- |
| 200  | Successful Operation      |
| 400  | Invalid Schedule supplied |

</details>

<details>
<summary>
GET       /admin/logout       Logs out the admin
</summary>

### Parameters

No Parameters needed.

### Responses

| Code | Description          |
| ---- | -------------------- |
| 200  | Successful Operation |

```json
{
    "code": 200,
    "request": "admin_logout",
    "message": "Logged Out"
}
```

</details>

</details>

<details>
<summary>Mentor</summary>

<details>
<summary>
GET       /mentor/login       Logs Mentor into the system
    </summary>

### Parameters

| Name | Description |
| ---- | ----------- |
| username(required)
string | The user name used for login |
| password(required)
string | The password used for login |

### Responses

| Code | Description               |
| ---- | ------------------------- |
| 200  | Successful Operation      |
| 400  | Invalid username/password |

```json
{
    "code": 200,
    "request": "mentor_login",
    "message": "Successfully Logged In!"
}
```

```json
{
    "code": 400,
    "request": "mentor_login",
    "message": "Invalid username or password. Please check try again"
}
```

</details>
<details>

<summary>
GET       /mentor/getCalendarView       Gets the Calendar data
</summary>

### Parameters

No Parameters needed.

### Responses

| Code | Description          |
| ---- | -------------------- |
| 200  | Successful Operation |

```json
{         
 name:"Dinaol Tadesse",
    courses:{"csc 118","calculus"},
    calendar: { 
  { 
   {"Tuesday","Thursday"},
             startTime:"00:12:00",
             endTime:"00:13:00"
  },
           { 
      {"Monday","Wednesday"},
              startTime:"00:07:00",
              endTime:"00:09:00"
   }
 }
}
```

</details>

<details>
<summary>
PUT       /mentor/changeSchedule       Updates Schedule of the Mentor
</summary>

### Parameters

| Name | Description |
| ---- | ----------- |
| body(required)
object | Updated user Object. |

Example body value:

```json
{        
  name:"Dinaol Tadesse",
     courses:{"csc 118","calculus"},
     calendar: { 
   { 
    {"Tuesday","Thursday"},
             startTime:"00:12:00",
              endTime:"00:13:00"
  },
        { 
      {"Monday","Wednesday"},
            startTime:"00:07:00",
            endTime:"00:09:00"
  }
 }
}
```

### Responses

| Code | Description               |
| ---- | ------------------------- |
| 200  | Successful Operation      |
| 400  | Invalid Schedule supplied |

</details>

<details>
<summary>
GET       /mentor/logout       Logs out the Mentor
</summary>  

### Parameters

No Parameters needed.

### Responses

| Code | Description          |
| ---- | -------------------- |
| 200  | Successful Operation |

```json
{
    "code": 200,
    "request": "mentor_logout",
    "message": "Logged Out"
}
```

</details>

</details>

<details>
<summary>
Student
</summary>
<details>
<summary>
GET       /student/login       Logs Student into the system
</summary>

### Parameters

| Name | Description |
| ---- | ----------- |
| username(required)
string | The user name used for login |
| password(required)
string | The password used for login |

### Responses

| Code | Description               |
| ---- | ------------------------- |
| 200  | Successful Operation!     |
| 400  | Invalid username/password |

```json
{
    "code": 200,
    "request": "student_login",
    "message": "Successfully Logged In!"
}
```

```json
{
    "code": 400,
    "request": "student_login",
    "message": "Invalid username or password. Please check try again"
}
```

</details>

<details>
<summary>
GET       /student/getCalendarView       Gets the Calendar Data.
</summary>

### Parameters

No Parameters needed.

### Responses

| Code | Description          |
| ---- | -------------------- |
| 200  | Successful Operation |

```json
{         
name:"Dinaol Tadesse",
     courses:{"csc 118","calculus"},
     calendar: 
  { 
   { 
    {"Tuesday","Thursday"},
            startTime:"00:12:00",
            endTime:"00:13:00"
   },
           { 
      {"Monday","Wednesday"},
            startTime:"00:07:00",
            endTime:"00:09:00"
   }
 }
}
```

</details>

<details>
<summary>
POST       /student/scheduleEvent       create appointment with Mentor
</summary>

### Parameters

| Name | Description |
| ---- | ----------- |
| body(required)
object | New event object. |

Example body value:

```json
{
    "eventId": 12,
    "mentorName": "Dinaol Tadesse",
    "studentName": "Amber Heard",
    "startDate": "2022-05-23 T21:15:23",
    "endDate": "2022-05-23 T22:15:23"
}
```

### Responses

| Code | Description            |
| ---- | ---------------------- |
| 200  | Successful Operation   |
| 400  | Invalid Event supplied |
| 404  | Event not found        |

</details>
<details>
<summary>
GET       /student/logout       Logs out the Student
</summary>

### Parameters

No Parameters needed.

### Responses

| Code | Description          |
| ---- | -------------------- |
| 200  | Successful Operation |

```json
{
    "code": 200,
    "request": "Student_logout",
    "message": "Logged Out"
}
```

</details>
</details>

### Calendar UI

For displaying the calendar on our application, there are different react calendar libraries. We can use the [React Big Calendar library](https://github.com/jquense/react-big-calendar). A small demo of how the calendar looks like can be found [here](https://jquense.github.io/react-big-calendar/examples/index.html?path=/story/about-big-calendar--page).

![Screen Shot 2022-05-18 at 9.21.24 PM.png](https://user-images.githubusercontent.com/32272045/169191267-b8572369-bd86-4794-ae0f-6da53c1bf57c.png)

### Resources

**OpenAPI** - standard way to describe an API

**Swagger API -** [https://swagger.io/specification/](https://swagger.io/specification/)

**Amazon API gateway**

**Requestbin**: [https://pipedream.com/workflows](https://pipedream.com/workflows)

**Tech Target:** [https://www.techtarget.com/searchapparchitecture/definition/API-endpoint#:~:text=An API endpoint is a,server and receiving a response](https://www.techtarget.com/searchapparchitecture/definition/API-endpoint#:~:text=An%20API%20endpoint%20is%20a,server%20and%20receiving%20a%20response).

**API Creation:** [https://blog.stoplight.io/how-to-create-an-api-in-three-steps](https://blog.stoplight.io/how-to-create-an-api-in-three-steps)
