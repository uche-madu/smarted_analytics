from datetime import date
import pandas as pd
import random
from faker import Faker
from faker.providers import BaseProvider

# Custom Provider for Nigerian Names and Addresses
class NigerianSchoolDataProvider(BaseProvider):
    def nigerian_first_name(self):
        first_names = [
            "Chinedu", "Ngozi", "Yemi", "Bola", "Ifeanyi", "Uche", "Amina", "Emeka",
            "Nkechi", "Tope", "Chika", "Bisi", "Femi", "Kunle", "Gbenga", "Tolu",
            "Funmi", "Ada", "Olu", "Sade", "Dapo", "Kehinde", "Nnamdi", "Kemi",
            "Chinonso", "Ebele", "Obinna", "Amara", "Chidera", "Olumide", "Bankole",
            "Ezinne", "Chimamanda", "Yinka", "Ayo", "Dele", "Chiamaka", "Omotola",
            "Segun", "Kolawole", "Sikiru", "Maryam", "Fatimah", "Toyin", "Kudirat"
        ]
        return self.random_element(first_names)

    def nigerian_last_name(self):
        last_names = [
            "Okafor", "Balogun", "Olawale", "Eze", "Ibrahim", "Adesina", "Ogunleye",
            "Nwosu", "Osagie", "Okonkwo", "Chukwu", "Alabi", "Onyejekwe", "Obi",
            "Ojo", "Adeola", "Adebayo", "Anyanwu", "Ajayi", "Ogbemudia", "Awolowo",
            "Ikenna", "Akintola", "Oni", "Odugbemi", "Adeyemi", "Ikechukwu", "Etuk"
        ]
        return self.random_element(last_names)

    def nigerian_address(self):
        addresses = [
            "12 Adeola Avenue, Lagos", "45 Ibrahim Street, Abuja", "23 Balogun Close, Ikeja, Lagos",
            "9 Aminu Kano Crescent, Wuse, Abuja", "17 Glover Road, Ikoyi, Lagos", "32 Nnamdi Azikiwe Drive, Enugu",
            "18 Oluwole Street, Ibadan", "15 Ogbemudia Street, Benin", "22 Oniru Crescent, Victoria Island, Lagos"
        ]
        return self.random_element(addresses)

    def state_of_origin(self):
        states_of_origin = ["Lagos", "Abuja", "Kano", "Kaduna", "Oyo", "Rivers", "Enugu", "Anambra"]
        return self.random_element(states_of_origin)
    
    def blood_group(self):
        blood_groups = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
        return self.random_element(blood_groups)

    def subject(self):
        subjects = [
            "English Language", "Mathematics", "Civic Education", "Biology", "Physics", "Chemistry", 
            "Further Mathematics", "Health Education", "Computer Science", "Technical Drawing", 
            "Food and Nutrition", "Agricultural Science", "Financial Accounting", "Book Keeping", 
            "Commerce", "Data Processing", "Office Practice", "Typewriting", "Economics", "Government", 
            "Literature in English", "Christian Religion Knowledge", "Geography", "Fine Art"
        ]
        return self.random_element(subjects)
    
    def genotype(self):
        genotypes = ["AA", "AS", "SS", "AC"]
        return self.random_element(genotypes)

    def marital_status(self):
        marital_status = ["Married", "Single", "Divorced", "Separated", "Widowed"]
        return self.random_element(marital_status)

    def qualification(self):
        qualifications = ["B.Ed.", "M.Sc.", "B.Sc.", "Ph.D.", "PGDE", "M.A.", "M.Ed."]
        return self.random_element(qualifications)

    def stream_name(self):
        streams = {
            "Basic Science and Maths": ["Biology", "Physics", "Chemistry", "Further Mathematics", "Health Education", "Computer Science"],
            "Technical and Agricultural": ["Technical Drawing", "Food and Nutrition", "Agricultural Science", "Physics", "Chemistry", "Biology"],
            "Commercial": ["Financial Accounting", "Book Keeping", "Commerce", "Data Processing", "Office Practice", "Typewriting"],
            "Liberal Arts and Social Science": ["Economics", "Government", "Literature in English", "Christian Religion Knowledge", "Geography", "Fine Art"]
        }
        return self.random_element(list(streams.keys()))


# Initialize Faker and add custom providers
fake = Faker()
fake.add_provider(NigerianSchoolDataProvider)

# Define constants
YEAR_OF_ADMISSION = "2022"


streams = {
    "Basic Science and Maths": ["Biology", "Physics", "Chemistry", "Further Mathematics", "Health Education", "Computer Science"],
    "Technical and Agricultural": ["Technical Drawing", "Food and Nutrition", "Agricultural Science", "Physics", "Chemistry", "Biology"],
    "Commercial": ["Financial Accounting", "Book Keeping", "Commerce", "Data Processing", "Office Practice", "Typewriting"],
    "Liberal Arts and Social Science": ["Economics", "Government", "Literature in English", "Christian Religion Knowledge", "Geography", "Fine Art"]
}

stream_names = list(streams.keys())


# Function to create student IDs
def create_student_id(year, count, stream_abbr):
    """Create student IDs using format: Year + unique 4-digit number + stream abbreviation."""
    return f"{year}{count:04d}{stream_abbr}"

# Function to generate names and IDs for students and parents
def generate_student_parent_pairs(stream_name, num_students=30):
    student_data = []
    parent_data = []

    # Generate pairs for the given number of students
    for i in range(1, num_students + 1):
        stream_abbr = "".join([word[0] for word in stream_name.split()]).upper()
        student_id = create_student_id(YEAR_OF_ADMISSION, i, stream_abbr)

        # Generate consistent student and parent names
        first_name = random.choice([fake.nigerian_first_name(), fake.first_name()])
        middle_name = random.choice([fake.nigerian_first_name(), fake.first_name()])
        last_name = fake.nigerian_last_name()
        full_name = f"{first_name} {middle_name} {last_name}"

        parent_id = f"PAR{random.randint(1000, 9999)}"
        parent_first_name = fake.nigerian_first_name()
        parent_middle_name = random.choice([fake.nigerian_first_name(), fake.first_name()])
        parent_full_name = f"{parent_first_name} {parent_middle_name} {last_name}"
        parent_gender = random.choice(["Male", "Female"])

        # Generate additional details
        gender = random.choice(["Male", "Female"])
        date_of_birth = fake.date_of_birth(minimum_age=13, maximum_age=20)
        address = fake.nigerian_address()
        blood_group = fake.blood_group()
        genotype = fake.genotype()
        state_of_origin = fake.state_of_origin()
        registration_date = fake.date_between(start_date=date(2022, 8, 1), end_date=date(2022, 10, 31))

        # Store student data
        student_data.append({
            "student_id": student_id,
            "first_name": first_name,
            "middle_name": middle_name,
            "last_name": last_name,
            "gender": gender,
            "date_of_birth": date_of_birth,
            "stream": stream_name,
            "grade_level": "SS3",
            "blood_group": blood_group,
            "genotype": genotype,
            "state_of_origin": state_of_origin,
            "address": address,
            "parent_id": parent_id,
            "registration_date": registration_date,
            "full_name": full_name
        })

        # Store parent data
        parent_data.append({
            "parent_id": parent_id,
            "first_name": parent_first_name,
            "middle_name": parent_middle_name,
            "last_name": last_name,
            "gender": parent_gender,
            "marital_status": fake.marital_status(),
            "phone_number": fake.phone_number(),
            "email": fake.email(),
            "address": address,
            "occupation": fake.job(),
            "relationship_to_student": "Father" if parent_gender == "Male" else "Mother",
            "full_name": parent_full_name
        })

    return pd.DataFrame(student_data), pd.DataFrame(parent_data)

def generate_teachers(num_teachers=10):
    teacher_data = []

    for _ in range(1, num_teachers + 1):
        teacher_id = f"TEA{random.randint(1000, 9999)}"

        # Generate consistent teacher details
        first_name = fake.nigerian_first_name()
        middle_name = random.choice([fake.nigerian_first_name(), fake.first_name()])
        last_name = fake.nigerian_last_name()
        full_name = f"{first_name} {middle_name} {last_name}"
        gender = random.choice(["Male", "Female"])
        date_of_birth = fake.date_of_birth(minimum_age=25, maximum_age=60)
        address = fake.nigerian_address()
        phone_number = fake.phone_number()
        email = fake.email()
        hire_date = fake.date_between(start_date=date(2010, 1, 1), end_date=date(2022, 10, 31))
        subject = fake.subject()
        qualification = fake.qualification()
        years_of_experience = random.randint(1, 35)

        # Store teacher data
        teacher_data.append({
            "teacher_id": teacher_id,
            "first_name": first_name,
            "middle_name": middle_name,
            "last_name": last_name,
            "gender": gender,
            "date_of_birth": date_of_birth,
            "phone_number": phone_number,
            "email": email,
            "address": address,
            "hire_date": hire_date,
            "subject_id": subject,
            "qualification": qualification,
            "years_of_experience": years_of_experience,
            "full_name": full_name
        })

    return pd.DataFrame(teacher_data)


# Generate and display the data
student_df, parent_df = generate_student_parent_pairs("Basic Science and Maths", num_students=10)
print("Students Data:\n", student_df.head())
print("\nParents Data:\n", parent_df.head())

# Generate and display the teacher data
teacher_df = generate_teachers(num_teachers=10)
print("Teachers Data:\n", teacher_df.head())







