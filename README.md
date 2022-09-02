# Quizze (Quiz Portal)
## [Description](https://github.com/avnishranwa7/Quiz/blob/main/Description)
We want to make an online quiz platform where teachers from colleges or schools will be able to conduct online quizzes according to respective courses they are teaching.

Salient features of this platform includes:
- Register and sign-in for both teachers and students.
- Teachers can create courses and enroll registered students in them.
- Teachers can create course-wise quizzes with mutiple-choice questions with upto four options.
- Enrolled students can give quiz in the time frame set by teachers.
- Results will be shown immediately after the quiz ends and can be accessed by both the teachers and students.
## [ER Model Description](https://github.com/avnishranwa7/Quiz/blob/main/ER%20Model%20Description)
ER Diagram Description :
-	If the teacher and student have an existing account then they can login otherwise they can register themselves and create their account.
-	The users will have to setup their username and password.
-	The teacher enrolls the student to their respective courses.
-	The teacher can create quizzes and link it to their courses.
-	Every quiz will have its unique ID.
-	The students enrolled in a course can view details of upcoming and previous quizzes.
-	Questions of a quiz will have unique ID.
-	The students response to each question of a quiz can be uniquely identified by the students rollno and the questions id.

Entities and Attributes : 
- Students Entity 
  - Attributes are RollNo, Name, Mail, Password.
  - RollNo acts as the primary key.
- Courses Entity 
  - Attributes are Course_ID, Course_Name.
  - Course_ID acts as the primary key.
- Teacher Entity
  - Attributes are Teacher_ID, Name, Mail, Password.
  - Teacher_ID acts as the primary key.
- Quiz Entity
  - Attributes are quiz_id, Course_ID, duration, date, start_time, end_time, quiz_name.
  - quiz_id acts as the primary key.
- Questions Entity
  - Attributes are q_id, quiz_id, question, ans, opt1, opt2, opt3, opt4.
  - q_id acts as the primary key.
- Responses Entity 
  - Attributes are RollNo, q_id, response.
  - RollNo and q_id together act as a composite primary key.
- Results Entity 
  - Attributes are RollNo, quiz_id, marks.
  - RollNo and quiz_id together act as a composite primary key.
## [ER Model](https://github.com/avnishranwa7/Quiz/blob/main/ER%20Model.png)
![alt text](https://github.com/avnishranwa7/Quiz/blob/main/ER%20Model.png)
## [Relational Schema](https://github.com/avnishranwa7/Quiz/blob/main/Relational%20Schema.jpg)
![alt text](https://github.com/avnishranwa7/Quiz/blob/main/Relational%20Schema.jpg)
## [Technologies Used](https://github.com/avnishranwa7/Quiz/blob/main/Technologies%20Used)
- Front-End : HTML, CSS, Django Template Language
- Back-End : Django
- Database : MySQL
