from datetime import date
import time
import pandas as pd
import random
import gspread
from faker import Faker
from faker.providers import BaseProvider
from configs import (
    SERVICE_ACCOUNT_FILE,
    SHEET_CONFIG
)

# Custom Provider for Nigerian Names and Addresses
class NigerianSchoolDataProvider(BaseProvider):
    def nigerian_first_name(self):
        first_names = [
            "Chinedu", "Ngozi", "Yemi", "Bola", "Ifeanyi", "Uche", "Amina", "Emeka", 
            "Nkechi", "Tope", "Chika", "Bisi", "Femi", "Kunle", "Gbenga", "Tolu", 
            "Funmi", "Ada", "Olu", "Sade", "Dapo", "Kehinde", "Nnamdi", "Kemi", 
            "Chinonso", "Ebele", "Obinna", "Amara", "Chidera", "Olumide", "Bankole", 
            "Ezinne", "Chimamanda", "Yinka", "Ayo", "Dele", "Chiamaka", "Omotola", 
            "Segun", "Kolawole", "Sikiru", "Maryam", "Fatimah", "Toyin", "Kudirat", 
            "Abdul", "Rukayat", "Efe", "Mfon", "Oghenekaro", "Adebisi", "Khadijah", 
            "Ahmed", "Yusuf", "Jide", "Temitope", "Tosin", "Nafisat", "Hadiza", 
            "Aisha", "Taiwo", "Bimbo", "Gbadebo", "Simisola", "Zainab", "Saheed", 
            "Ifeoma", "Ndidi", "Tajudeen", "Emmanuella", "Chukwuemeka", "Onyeka", 
            "Ndubisi", "Oluwatobiloba", "Yemisi", "Oluwasegun", "Eunice", "Suliat", 
            "Anike", "Usman", "Adebola", "Oluwanifemi", "Ayodeji", "Mojirayo", 
            "Chisom", "Efeoma", "Muna", "Obiageli", "Yewande"
        ]
        return self.random_element(first_names)

    def nigerian_last_name(self):
        last_names = [
            "Okafor", "Balogun", "Olawale", "Eze", "Ibrahim", "Adesina", "Ogunleye", 
            "Nwosu", "Osagie", "Okonkwo", "Chukwu", "Alabi", "Onyejekwe", "Obi", 
            "Ojo", "Adeola", "Adebayo", "Anyanwu", "Ajayi", "Ogbemudia", "Awolowo", 
            "Ikenna", "Akintola", "Oni", "Odugbemi", "Adeyemi", "Ikechukwu", "Etuk", 
            "Okorie", "Amaechi", "Ogbonna", "Agbaje", "Chukwuma", "Adegoke", "Ogunmola", 
            "Musa", "Sanusi", "Oyeleke", "Opeoluwa", "Bello", "Obafemi", "Danjuma", 
            "Adamu", "Muhammad", "Ozor", "Gadzama", "Oboh", "Ekechukwu", "Olaniyan", 
            "Olojede", "Orji", "Nwachukwu", "Umeh", "Uzor", "Anosike", "Odeleye", 
            "Olatunji", "Falade", "Dare", "Bakare", "Fashola", "Jaiyeola", "Adigun", 
            "Adewole", "Orjiakor", "Onochie", "Adeyinka", "Olubiyi", "Omoruyi", 
            "Idowu", "Omoyeni", "Obasanya", "Olaide", "Oluwole", "Ogunsanwo", "Oshin", 
            "Kasim", "Obiano", "Ejiogu"
        ]
        return self.random_element(last_names)

    def nigerian_address(self):
        addresses = [
            "12 Adeola Avenue, Lagos", "45 Ibrahim Street, Abuja", "23 Balogun Close, Ikeja, Lagos",
            "9 Aminu Kano Crescent, Wuse, Abuja", "17 Glover Road, Ikoyi, Lagos", "32 Nnamdi Azikiwe Drive, Enugu",
            "18 Oluwole Street, Ibadan", "15 Ogbemudia Street, Benin", "22 Oniru Crescent, Victoria Island, Lagos",
            "1 Awolowo Road, Ikoyi, Lagos", "33 Ogundana Street, Ikeja, Lagos", "10 Marina Road, Victoria Island, Lagos",
            "14 Opebi Road, Ikeja, Lagos", "27 Ahmadu Bello Way, Victoria Island, Lagos", "5 Okonjo-Iweala Street, Abuja",
            "30 Asokoro Avenue, Asokoro, Abuja", "7 Maitama Crescent, Maitama, Abuja", "8 Aguiyi Ironsi Street, Maitama, Abuja",
            "21 Awka Road, Onitsha, Anambra", "35 New Haven Road, Enugu", "42 Ngwo Street, Enugu",
            "15 Herbert Macaulay Way, Yaba, Lagos", "12 Bankole Street, Lagos Island, Lagos", "19 Alimosho Road, Egbeda, Lagos",
            "6 Surulere Avenue, Surulere, Lagos", "2 Allen Avenue, Ikeja, Lagos", "25 Bode Thomas Street, Surulere, Lagos",
            "11 Wetheral Road, Owerri, Imo", "16 Tetlow Road, Owerri, Imo", "23 Egbu Road, Owerri, Imo",
            "9 Olu Obasanjo Road, Port Harcourt, Rivers", "22 Old Aba Road, Port Harcourt, Rivers", "17 Elelenwo Street, Port Harcourt, Rivers",
            "4 Sani Abacha Way, Kano", "29 Yankari Close, Kano", "7 Shehu Shagari Way, Kano",
            "18 Makurdi Road, Kaduna", "33 Yakubu Gowon Way, Kaduna", "12 Tafawa Balewa Way, Bauchi",
            "19 Ahmadu Bello Street, Bauchi", "15 Jos Road, Bauchi", "23 Muhammadu Buhari Way, Minna",
            "27 Paiko Road, Minna", "14 Airport Road, Benin", "32 Ugbor Road, Benin", "8 Boundary Road, Benin",
            "5 Orelope Street, Osogbo, Osun", "17 Gbongan Road, Osogbo, Osun", "30 Mokola Road, Ibadan, Oyo",
            "9 Dugbe Street, Ibadan, Oyo", "11 Ring Road, Ibadan, Oyo", "7 Iwo Road, Ibadan, Oyo",
            "3 Queen Elizabeth Road, Ilorin, Kwara", "16 Taiwo Road, Ilorin, Kwara", "25 Asa Dam Road, Ilorin, Kwara",
            "8 Stadium Road, Calabar, Cross River", "13 Marian Road, Calabar, Cross River", "21 Moore Road, Calabar, Cross River"
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
        qualifications = ["B.Ed.", "M.Sc.", "B.Sc.", "PGDE", "M.A.", "M.Ed."]
        return self.random_element(qualifications)

    def stream_name(self):
        streams = {
            "Basic Science and Maths": ["Biology", "Physics", "Chemistry", "Further Mathematics", "Health Education", "Computer Science"],
            "Technical and Agricultural": ["Technical Drawing", "Food and Nutrition", "Agricultural Science", "Physics", "Chemistry", "Biology"],
            "Commercial": ["Financial Accounting", "Book Keeping", "Commerce", "Data Processing", "Office Practice", "Typewriting"],
            "Liberal Arts and Social Science": ["Economics", "Government", "Literature in English", "Christian Religion Knowledge", "Geography", "Fine Art"]
        }
        return self.random_element(list(streams.keys()))
    
    def remark(self):
        teacher_remarks = [
            "Excellent performance!", "Needs improvement", "Good effort", "Outstanding!",
            "Satisfactory", "Below expectations", "Keep up the good work", "Poor attendance",
            "Well done", "Great improvement", "Average performance", "Shows potential",
            "Struggles with some concepts"
        ]
        return self.random_element(teacher_remarks) 


# Initialize Faker and add custom provider
fake = Faker()
fake.add_provider(NigerianSchoolDataProvider)

# Define constants and configuration

gc = gspread.service_account(filename=SERVICE_ACCOUNT_FILE)

YEAR_OF_ADMISSION = "2022"
core_subjects = ["English Language", "Mathematics", "Civic Education"]
streams = {
    "Basic Science and Maths": ["Biology", "Physics", "Chemistry", "Further Mathematics", "Health Education", "Computer Science"],
    "Technical and Agricultural": ["Technical Drawing", "Food and Nutrition", "Agricultural Science", "Physics", "Chemistry", "Biology"],
    "Commercial": ["Financial Accounting", "Book Keeping", "Commerce", "Data Processing", "Office Practice", "Typewriting"],
    "Liberal Arts and Social Science": ["Economics", "Government", "Literature in English", "Christian Religion Knowledge", "Geography", "Fine Art"]
}

academic_years = {"SS1": "2022/2023", "SS2": "2023/2024", "SS3": "2024/2025"}
terms = ["First", "Second", "Third"]
grade_levels = ["SS1", "SS2", "SS3"]
class_arms = {"Basic Science and Maths": "A", "Technical and Agricultural": "B", "Commercial": "C", "Liberal Arts and Social Science": "D"}

# Score distributions
performance_profiles = {
    "Poor": {"ca_mean": 3, "ca_std_dev": 3, "exam_mean": 25, "exam_std_dev": 10},
    "Average": {"ca_mean": 8, "ca_std_dev": 3, "exam_mean": 35, "exam_std_dev": 9},
    "Above Average": {"ca_mean": 13, "ca_std_dev": 2, "exam_mean": 55, "exam_std_dev": 10}
}

# Assign probabilities for each profile
profile_probabilities = ["Poor"] * 30 + ["Average"] * 60 + ["Above Average"] * 10


# Helper function to create unique student ID
def create_student_id(year, count, stream_abbr):
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
        # Capitalize the keys for student data
        student_data.append({
            "Student ID": student_id,
            "First Name": first_name,
            "Middle Name": middle_name,
            "Last Name": last_name,
            "Gender": gender,
            "Date of Birth": date_of_birth,
            "Stream": stream_name,
            "Grade Level": "SS3",
            "Blood Group": blood_group,
            "Genotype": genotype,
            "State of Origin": state_of_origin,
            "Address": address,
            "Parent ID": parent_id,
            "Registration Date": registration_date,
            "Full Name": full_name
        })

        # Capitalize the keys for parent data
        parent_data.append({
            "Parent ID": parent_id,
            "First Name": parent_first_name,
            "Middle Name": parent_middle_name,
            "Last Name": last_name,
            "Gender": parent_gender,
            "Marital Status": fake.marital_status(),
            "Phone Number": fake.phone_number(),
            "Email": fake.email(),
            "Address": address,
            "Occupation": fake.job(),
            "Relationship to Student": "Father" if parent_gender == "Male" else "Mother",
            "Full Name": parent_full_name
        })


    return pd.DataFrame(student_data), pd.DataFrame(parent_data)


# Function to generate term scores based on performance profiles
def generate_term_scores(profile):
    ca1 = int(random.gauss(profile["ca_mean"], profile["ca_std_dev"]))
    ca2 = int(random.gauss(profile["ca_mean"], profile["ca_std_dev"]))
    exam = int(random.gauss(profile["exam_mean"], profile["exam_std_dev"]))
    return max(0, min(15, ca1)), max(0, min(15, ca2)), max(10, min(70, exam))


# Function to generate session data with attendance and teacher remarks for each subject
def generate_session_data(student_df, grade_level, term_name):
    subjects = core_subjects + streams[student_df["Stream"].iloc[0]]
    columns = ["Student ID", "Name", "Stream", "Academic Year", "Class Arm", "Grade Level", "Term"]
    
    # Extend columns to include CA1, CA2, Exam, Total, Attendance %, and Teacher Remarks
    for subject in subjects:
        columns.extend([f"{subject} (CA1)", f"{subject} (CA2)", f"{subject} (Exam)", f"{subject} (Total)", "Attendance %", "Teacher Remarks"])

    data = []
    for _, row in student_df.iterrows():
        student_id = row["Student ID"]
        full_name = row["Full Name"]
        stream_name = row["Stream"]
        academic_year = academic_years[grade_level]
        class_arm = class_arms[stream_name]
        profile = performance_profiles[random.choice(profile_probabilities)]

        # Generate attendance, scores, and teacher remarks for each subject
        term_row = [student_id, full_name, stream_name, academic_year, class_arm, grade_level, term_name]
        for subject in subjects:
            ca1, ca2, exam = generate_term_scores(profile)
            total_score = ca1 + ca2 + exam
            attendance_percentage = round(random.uniform(40, 100), 2)
            remarks = fake.remark()
            term_row.extend([ca1, ca2, exam, total_score, attendance_percentage, remarks])

        data.append(term_row)

    return pd.DataFrame(data, columns=columns)


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
        hire_date = fake.date_between(start_date=date(2014, 1, 1), end_date=date(2023, 10, 31))
        subject = fake.subject()
        qualification = fake.qualification()
        years_of_experience = random.randint(1, 35)

        # Store teacher data
        teacher_data.append({
            "Teacher ID": teacher_id,
            "First Name": first_name,
            "Middle Name": middle_name,
            "Last Name": last_name,
            "Gender": gender,
            "Date of Birth": date_of_birth,
            "Phone Number": phone_number,
            "Email": email,
            "Address": address,
            "Hire Date": hire_date,
            "Subject": subject,
            "Qualification": qualification,
            "Years of Experience": years_of_experience,
            "Full Name": full_name
        })


    return pd.DataFrame(teacher_data)

def generate_extracurricular_activities(student_df, teacher_df, num_records_per_student=2):
    """
    Generate extracurricular activities data for students and assign a unique teacher to each activity.
    Each activity will have a specific teacher assigned, ensuring no overlapping teacher assignments.

    Parameters:
    student_df (pd.DataFrame): DataFrame containing student data.
    teacher_df (pd.DataFrame): DataFrame containing teacher data.
    num_records_per_student (int): Number of activities per student (default is 2).

    Returns:
    pd.DataFrame: DataFrame containing generated extracurricular activities data.
    """
    # Define extracurricular activities and participation levels
    activities_list = ["Soccer", "Basketball", "Chess Club", "Debate Club", "Drama", 
                       "Music Band", "Art Club", "Science Club", "Coding Club", "Math Olympiad", 
                       "Literature Club", "Environment Club", "Culinary Club", "Photography Club"]
    participation_levels = ["Beginner", "Intermediate", "Advanced"]

    # Randomly select teachers to match with activities
    teachers = teacher_df.sample(len(activities_list), random_state=42)  # Ensure unique teacher assignment
    activity_teacher_map = dict(zip(activities_list, teachers["Teacher ID"].tolist()))

    # Generate extracurricular activity data for each student
    activity_data = []
    for _, student in student_df.iterrows():
        student_id = student["Student ID"]

        # Assign a number of activities to each student
        selected_activities = random.sample(activities_list, num_records_per_student)

        for activity in selected_activities:
            activity_id = f"ACT{random.randint(1000, 9999)}"
            teacher_id = activity_teacher_map[activity]
            participation_level = random.choice(participation_levels)
            date_joined = fake.date_between(start_date=date(2022, 8, 1), end_date=date(2022, 12, 31))

            activity_data.append({
                "Activity ID": activity_id,
                "Activity Name": activity,
                "Student ID": student_id,
                "Participation Level": participation_level,
                "Teacher ID": teacher_id,
                "Date Joined": date_joined
            })


    return pd.DataFrame(activity_data)

def generate_health_records(student_df, num_records=3):
    # Define sample health issues paired with likely treatments
    health_issue_treatment_pairs = {
        "Asthma": "Inhaler and regular checkups",
        "Diabetes": "Insulin therapy and diet management",
        "Allergy": "Antihistamines and allergen avoidance",
        "Malaria": "Antimalarial medication",
        "Flu": "Rest, hydration, and flu medication",
        "Vision Problems": "Prescription glasses",
        "Hearing Issues": "Hearing aid or therapy"
    }

    doctors_list = ["Dr. Adebayo", "Dr. Ojo", "Dr. Eze", "Dr. Ibrahim", "Dr. Williams", "Dr. Okafor"]

    health_data = []

    # Select 40% of the students to generate health records for
    selected_students = student_df.sample(frac=0.4, random_state=42)

    # Generate health records for the selected students only
    for _, student in selected_students.iterrows():
        student_id = student["Student ID"]

        # Create a specified number of health records for each selected student
        for _ in range(random.randint(1, num_records)):
            record_id = f"HR{random.randint(1000, 9999)}"  # Unique record ID
            checkup_date = fake.date_between(start_date=date(2022, 8, 1), end_date=date(2022, 12, 31))
            
            # Assign health issue and treatment (excluding "None")
            health_issue = random.choice(list(health_issue_treatment_pairs.keys()))
            treatment = health_issue_treatment_pairs[health_issue]
            
            doctor = random.choice(doctors_list)

            # Admission status and dates
            admitted = "Yes" if random.random() < 0.3 else "No"
            admission_date = checkup_date if admitted == "Yes" else None
            discharge_date = fake.date_between(start_date=admission_date, end_date=date(2023, 1, 31)) if admitted == "Yes" else None
            follow_up_date = fake.date_between(start_date=checkup_date, end_date=date(2023, 3, 31)) if random.random() < 0.5 else None

            health_data.append({
                "Record ID": record_id,
                "Student ID": student_id,
                "Checkup Date": checkup_date,
                "Health Issues": health_issue,
                "Treatment": treatment,
                "Admitted": admitted,
                "Admission Date": admission_date,
                "Discharge Date": discharge_date,
                "Doctor": doctor,
                "Follow Up Date": follow_up_date
            })


    return pd.DataFrame(health_data)

# Function to update Google Sheets with generated data for each term
def update_google_sheet(worksheet_name, dataframe, sheet_url):
    sh = gc.open_by_url(sheet_url)
    try:
        worksheet = sh.worksheet(worksheet_name)
    except gspread.exceptions.WorksheetNotFound:
        worksheet = sh.add_worksheet(title=worksheet_name, rows=dataframe.shape[0] + 1, cols=dataframe.shape[1])
    worksheet.clear()
    worksheet.update([dataframe.columns.values.tolist()] + dataframe.values.tolist())
    print(f"Updated Google Sheet: {worksheet_name}")
    # Add delay to prevent quota exceeded error
    time.sleep(3) 

def main():
    # Initialize DataFrames for consolidated storage
    all_students_df = pd.DataFrame()
    all_parents_df = pd.DataFrame()

    # 1. Generate and update 'results', 'students', and 'parents' sheets for each stream, grade, and term
    for stream in streams.keys():
        for grade in grade_levels:
            for term in terms:
                student_df, parent_df = generate_student_parent_pairs(stream, num_students=30)
                results_df = generate_session_data(student_df, grade, term)

                # Append generated data to master DataFrames
                all_students_df = pd.concat([all_students_df, student_df], ignore_index=True)
                all_parents_df = pd.concat([all_parents_df, parent_df], ignore_index=True)

                # Create sheet names and update Google Sheets
                sheet_name = f"{grade}_{stream}_{term}".replace(" ", "_")
                update_google_sheet(sheet_name, results_df, SHEET_CONFIG["results"]["url"])
                update_google_sheet("Students Bio", student_df, SHEET_CONFIG["students"]["url"])
                update_google_sheet("Parents Bio", parent_df, SHEET_CONFIG["parents"]["url"])

    # 2. Generate and update 'teachers' sheet
    teacher_df = generate_teachers(num_teachers=50)
    update_google_sheet("Teachers Bio", teacher_df, SHEET_CONFIG["teachers"]["url"])

    # 3. Generate and update 'extracurricular_activities' sheet
    extracurricular_df = generate_extracurricular_activities(all_students_df, teacher_df)
    update_google_sheet("Extracurricular Activities", extracurricular_df, SHEET_CONFIG["extracurricular_activities"]["url"])

    # 4. Generate and update 'health_records' sheet
    health_records_df = generate_health_records(all_students_df)
    update_google_sheet("Student Health Records", health_records_df, SHEET_CONFIG["health_records"]["url"])

if __name__ == "__main__":
    main()



# Sample Execution
# student_df, parent_df = generate_student_parent_pairs("Basic Science and Maths", num_students=10)
# term_scores_df = generate_session_data(student_df, "SS3", "First")
# teacher_df = generate_teachers(num_teachers=30)
# extracurricular_df = generate_extracurricular_activities(student_df, teacher_df)
# health_records_df = generate_health_records(student_df)


# print(f"Teachers Data (Shape: {teacher_df.shape}):\n", teacher_df.head())
# print(f"\nTerm Results (Shape: {term_scores_df.shape}):\n", term_scores_df.head())
# print(f"\nStudents Data (Shape: {student_df.shape}):\n", student_df.head())
# print(f"\nParents Data (Shape: {parent_df.shape}):\n", parent_df.head())
# print(f"\nExtracurricular Data (Shape: {extracurricular_df.shape}):\n", extracurricular_df.head())
# print(f"\nHealth Records (Shape: {health_records_df.shape}):\n", health_records_df.head())





