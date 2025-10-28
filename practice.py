# STUDENT CLASS DEFINITION
# Defines a Student class with default attributes and methods for grade management
class student :
    name = "John"  # Default name (will be overridden for each instance)
    email = "john@example.com"  # Default email (will be overridden for each instance)
    grades = [85, 90, 78]  # Default grades list (will be overridden for each instance)

    # METHOD: Add a new grade to the student's grades list
    def add_grade (self, grade) :
        self.grades.append(grade)

    # METHOD: Calculate and return the mathematical average of all grades
    def average_grade (self) :
        return sum(self.grades) / len(self.grades)

    # METHOD: Display complete student information including calculated average
    def display_info(self) :
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Grades: {self.grades}")
        print(f"Average Grade: {self.average_grade():.2f}")
    
    # METHOD: Convert the mutable grades list to an immutable tuple
    def grades_tuple(self):
        return tuple(self.grades)

# CREATING STUDENT OBJECTS
# Instantiate three student objects and override default attributes with unique data

# Student 1: Joseph with initial grades [88, 92, 79]
s1 = student()
s1.name = "Joseph"
s1.email = "joseph@example.com"
s1.grades = [88, 92, 79]

# Student 2: Jackson with initial grades [85, 87, 90]
s2 = student()
s2.name = "Jackson"
s2.email = "jackson@example.com"
s2.grades = [85, 87, 90]

# Student 3: Michael with initial grades [90, 85, 88]
s3 = student()
s3.name = "Michael"
s3.email = "michael@example.com"
s3.grades = [90, 85, 88]

# TESTING add_grade METHOD
# Add one additional grade to each student's existing grades list
s1.add_grade(95)  # Joseph: [88, 92, 79] becomes [88, 92, 79, 95]
s2.add_grade(89)  # Jackson: [85, 87, 90] becomes [85, 87, 90, 89]
s3.add_grade(92)  # Michael: [90, 85, 88] becomes [90, 85, 88, 92]

# DISPLAY ALL STUDENT INFORMATION
# Call display_info() for each student to show name, email, grades, and calculated average
s1.display_info()
s2.display_info()
s3.display_info()

# DICTIONARY DATA STRUCTURE
# Create a dictionary mapping email addresses (keys) to student objects (values)
# This enables quick lookups of students by their email address
student_dict = {
    s1.email: s1,  # "joseph@example.com": <student object>
    s2.email: s2,  # "jackson@example.com": <student object>
    s3.email: s3   # "michael@example.com": <student object>
}

# FUNCTION: Safe student retrieval by email using dictionary.get()
# Returns student object if email exists, None if email not found (no KeyError)
def get_student_by_email(email):
    return student_dict.get(email) 

# FUNCTION: Generate set of all unique grades across all students
# Uses set data structure to automatically eliminate duplicate grade values
def get_all_unique_grades():
    unique_grades = set()
    for student in student_dict.values():
        unique_grades.update(student.grades)  # Add all grades from this student to set
    return unique_grades

# DEMONSTRATE SET DATA STRUCTURE
# Execute function to collect all unique grades and display them sorted
unique_grades = get_all_unique_grades()
print(f"\nAll unique grades across all students: {sorted(unique_grades)}")

# DEMONSTRATE DICTIONARY LOOKUP FUNCTIONALITY
# Test the email-based student retrieval function with a valid email
print(f"\nTesting get_student_by_email function:")
test_student = get_student_by_email("joseph@example.com")
if test_student:
    print(f"Found student: {test_student.name}")
else:
    print("Student not found")

# DEMONSTRATE TUPLE CONVERSION AND IMMUTABILITY
# Convert Joseph's grades list to tuple and verify the conversion
print(f"\nTesting grades_tuple method:")
joseph_grades_tuple = s1.grades_tuple()
print(f"Joseph's grades as tuple: {joseph_grades_tuple}")
print(f"Type: {type(joseph_grades_tuple)}")

# DEMONSTRATE TUPLE IMMUTABILITY WITH EXCEPTION HANDLING
# Attempt to modify tuple element to prove tuples cannot be changed after creation
print(f"\nDemonstrating tuple immutability:")
try:
    joseph_grades_tuple[0] = 100  # This will raise TypeError
    print("Successfully changed tuple value")
except TypeError as e:
    print(f"Error: {e}")
    print("Tuples are immutable - you cannot change their values!")

# DEMONSTRATE LIST MUTABILITY WITH .pop() METHOD
# Remove and return the last element from each student's grades list
print(f"\nRemoving last grade from each student using .pop():")
joseph_removed = s1.grades.pop()    # Removes 95, returns it
jackson_removed = s2.grades.pop()   # Removes 89, returns it
michael_removed = s3.grades.pop()   # Removes 92, returns it

print(f"Joseph's removed grade: {joseph_removed}")
print(f"Jackson's removed grade: {jackson_removed}")
print(f"Michael's removed grade: {michael_removed}")

# DEMONSTRATE LIST INDEXING - POSITIVE AND NEGATIVE INDICES
# Access first element [0] and last element [-1] from each student's grades
print(f"\nFirst and last grades for each student:")
print(f"Joseph - First: {s1.grades[0]}, Last: {s1.grades[-1]}")
print(f"Jackson - First: {s2.grades[0]}, Last: {s2.grades[-1]}")
print(f"Michael - First: {s3.grades[0]}, Last: {s3.grades[-1]}")

# DEMONSTRATE len() FUNCTION FOR COUNTING LIST ELEMENTS
# Display the current number of grades each student has after .pop() operations
print(f"\nNumber of grades for each student:")
print(f"Joseph has {len(s1.grades)} grades")
print(f"Jackson has {len(s2.grades)} grades")
print(f"Michael has {len(s3.grades)} grades")