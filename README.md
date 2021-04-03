# Quizze (Quiz Portal)
## [Description](https://github.com/avnishranwa7/Quiz/blob/main/Description)
We want to make an online quiz platform where teachers from colleges or schools will be able to conduct online quizzes according to respective courses they are teaching.

Salient features of this platform includes:
- Register and sign-in for both teachers and students
- Teachers can create courses and enroll registered students in them
- Teachers can create course-wise quizzes with mutiple-choice questions with upto four options
- Enrolled students can give quiz in the time frame set by teachers
- Results will be shown immediately after the quiz ends and will be emailed to both the teachers and students
## [ER Model Description](https://github.com/avnishranwa7/Quiz/blob/main/ER%20Model%20Description)
ER Diagram Description :
-	If the teacher and student have an existing account then they can login otherwise they can register themselves and create their account.
-	The users will have to setup their username and password.
-	The teacher enrolls the student to their respective sources.
-	The teacher can create quizzes and link it to their courses.
-	Every quiz will have its unique ID.
-	The students enrolled in a course can view details of upcoming and previous quizzes.
-	Questions of a quiz will have unique ID.
-	The students response to each question of a quiz can be uniquely identified by the students rollno and the questions id.

Entities and Attributes : 
-	Students Entity : Attributes are rollno, sname, email, password.
	              : rollno acts as the primary key.
-	Courses Entity : Attributes are course_id, course_name.
	            : course_id acts as the primary key.
-	Teachers Entity : Attributes are teacher_id, tname, email, password.
	              : teacher_id acts as the primary key.
-	Quizzes Entity : Attributes are quiz_id, course_id, duration, date, start_time, end_time.
	            : quiz_id acts as the primary key.
-	Questions Entity : Attributes are q_id, quiz_id, question, ans, opt1, opt2, opt3, opt4.
	                : q_id acts as the primary key.
-	Responses Entity : Attributes are rollno, q_id, response, quiz_id.
		   : rollno and q_id together act as a composite primary key.
-	Results Entity : Attributes are rollno, course_id, quiz_id, marks.
	           : rollno acts as the primary key.
## [ER Model](https://github.com/avnishranwa7/Quiz/blob/main/ER%20Model.png)
## [Relational Schema](https://github.com/avnishranwa7/Quiz/blob/main/Relational%20Schema.jpeg)
![alt text](https://github.com/avnishranwa7/Quiz/blob/main/Relational%20Schema.jpeg)
## [Technologies Used](https://github.com/avnishranwa7/Quiz/blob/main/Technologies%20Used)
- Front-End: HTML, CSS, Django Template Language
- Back-End: Django
- Database: MySQL
