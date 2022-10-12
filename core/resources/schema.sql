CREATE TABLE "MENTOR" (
  "mentor_id" int,
  "user_id" int,
  "courses" VARCHAR,  
  PRIMARY KEY ("mentor_id")
);
CREATE TABLE "STUDENT" (
  "student_id" int,
  "user_id" int,
  PRIMARY KEY ("student_id")
);

CREATE TABLE "CALENDAR" (
  "calendar_id" int,
  "user_id" int,
  "assignedDate" Date,
  "startDate" Date,
  "endDate" Date,
  PRIMARY KEY ("calendar_id")
);

CREATE TABLE "USER" (
  "user_id" int,
  "fullName" VARCHAR,
  "jNumber" int,
  "email" VARCHAR,
  "role" VARCHAR,
  "userName" VARCHAR,
  "password" VARCHAR,
  PRIMARY KEY ("user_id")
);

CREATE TABLE "SIGNIN" (
  "signin_id" int,
  "user_id" int,
  "userName" VARCHAR,
  "password" VARCHAR,
  PRIMARY KEY ("signin_id")
);

CREATE TABLE "EVENTS" (
  "events_id" int,
  "mentor_id" int,
  "student_id" int,
  "startDate" Date,
  "endDate" Date,
  PRIMARY KEY ("events_id")
);
