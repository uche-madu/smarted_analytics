from datetime import date, datetime, timedelta
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
        states_of_origin = [
            "Abia", "Adamawa", "Akwa Ibom", "Anambra", "Bauchi", "Bayelsa", "Benue",
            "Borno", "Cross River", "Delta", "Ebonyi", "Edo", "Ekiti", "Enugu",
            "FCT", "Gombe", "Imo", "Jigawa", "Kaduna", "Kano", "Katsina", "Kebbi",
            "Kogi", "Kwara", "Lagos", "Nasarawa", "Niger", "Ogun", "Ondo", "Osun",
            "Oyo", "Plateau", "Rivers", "Sokoto", "Taraba", "Yobe", "Zamfara"
        ]
        return self.random_element(states_of_origin)

    def home_language(self):
        languages = [
            "English", "Yoruba", "Igbo", "Hausa", "Efik", "Ibibio", "Ijaw", "Tiv",
            "Edo", "Fulfulde", "Kanuri", "Nupe", "Gwari", "Itsekiri", "Urhobo",
            "Ikwere", "Jukun", "Idoma"
        ]
        return self.random_element(languages)

    def income_bracket(self):
        brackets = [
            "Below 100,000 Naira",        # Low income
            "100,000 - 500,000 Naira",    # Lower-middle income
            "500,000 - 1,000,000 Naira",  # Middle income
            "1,000,000 - 3,000,000 Naira", # Upper-middle income
            "Above 3,000,000 Naira"       # High income
        ]
        return self.random_element(brackets)


    def education_level(self):
        education_levels = [
            "Primary School", "Secondary School", "Technical/Vocational", "Diploma",
            "Bachelor", "Master", "PhD", "None"
        ]
        return self.random_element(education_levels)

    def employment_type(self):
        employment_types = [
            "Full-Time", "Part-Time", "Self-Employed", "Unemployed", "Contract",
            "Freelancer", "Informal Sector"
        ]
        return self.random_element(employment_types)

    def industry(self):
        industries = [
            "Education", "Healthcare", "Finance", "Retail", "Construction",
            "Agriculture", "Transportation", "Technology", "Hospitality",
            "Telecommunications", "Oil & Gas", "Government", "Manufacturing",
            "Entertainment", "Mining", "Legal", "Other"
        ]
        return self.random_element(industries)

    def nigerian_job(self):
        jobs = [
            "Teacher", "Doctor", "Engineer", "Accountant", "Nurse", "Banker", 
            "Civil Servant", "Lawyer", "Pharmacist", "Lecturer", "Police Officer", 
            "Journalist", "Entrepreneur", "Software Developer", "Mechanic", 
            "Electrician", "Farmer", "Tailor", "Fashion Designer", "Chef", 
            "Driver", "Plumber", "Architect", "Scientist", "Environmentalist",
            "Social Worker", "Graphic Designer", "Consultant", "Data Analyst",
            "Digital Marketer", "Project Manager", "HR Manager", "Business Analyst",
            "Sales Representative", "Real Estate Agent", "Photographer", 
            "Event Planner", "Security Officer", "Financial Advisor", 
            "Fitness Trainer", "Insurance Agent", "Bank Teller", "Medical Lab Scientist", 
            "Radiologist", "Administrative Assistant", "Procurement Officer",
            "Public Relations Officer", "Community Health Worker", "Veterinarian", 
            "Public Health Specialist", "Trader", "Clergy"
        ]
        return self.random_element(jobs)
    
    def nigerian_phone_number(self):
        # Nigerian phone number prefixes
        prefixes = ["070", "080", "081", "090", "091"]
        # Select a random prefix and append 8 random digits
        phone_number = f"{random.choice(prefixes)}{random.randint(10000000, 99999999)}"
        return phone_number
    
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
terms_sessions = [
    {"term": term, "session": grade}
    for grade in grade_levels
    for term in terms
    if not (grade == "SS3" and term == "Third")
]

# Score distributions
performance_profiles = {
    "Poor": {"ca_mean": 5, "ca_std_dev": 3, "exam_mean": 25, "exam_std_dev": 10},
    "Average": {"ca_mean": 8, "ca_std_dev": 3, "exam_mean": 35, "exam_std_dev": 10},
    "Above Average": {"ca_mean": 12, "ca_std_dev": 3, "exam_mean": 45, "exam_std_dev": 10}
}

# Assign probabilities for each profile
profile_probabilities = ["Poor"] * 15 + ["Average"] * 65 + ["Above Average"] * 20


# Helper function to create unique student ID
def create_student_id(year, count, stream_abbr):
    return f"{year}{count:04d}{stream_abbr}"

# Helper: Add Timestamps
def current_timestamp():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

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
        parent_gender = random.choice(["Male", "Female"])

        # Generate additional details
        gender = random.choice(["Male", "Female"])
        date_of_birth = fake.date_of_birth(minimum_age=13, maximum_age=20)
        address = fake.nigerian_address()
        blood_group = fake.blood_group()
        genotype = fake.genotype()
        state_of_origin = fake.state_of_origin()
        registration_date = fake.date_between(start_date=date(2022, 8, 1), end_date=date(2022, 10, 31))
        profile = performance_profiles[random.choice(profile_probabilities)]

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
            "Full Name": full_name,
            "Profile": profile,
            "Created At": current_timestamp(),
            "Updated At": current_timestamp()
        })

        # Additional parent socio-economic and engagement details
        engagement_level = random.randint(1, 10)  # Engagement score based on school interactions
        relationship_type = random.choice(["Parent", "Relative", "Guardian"])
        number_of_children = random.randint(1, 5)
        email = f"{parent_first_name.lower()}.{last_name.lower()}{random.randint(10, 99)}@example.com"
       
        # Interaction metrics
        parent_teacher_meeting_attendance = random.randint(0, 5)
        volunteer_activities_count = random.randint(0, 3)
        timestamp = datetime.strptime(current_timestamp(), "%Y-%m-%d %H:%M:%S")
        recent_interaction_date = timestamp - timedelta(days=random.randint(1, 180))

        # Store parent data with additional engagement and contact fields
        parent_data.append({
            "Parent ID": parent_id,
            "First Name": parent_first_name,
            "Middle Name": parent_middle_name,
            "Last Name": last_name,
            "Gender": parent_gender,
            "Marital Status": random.choice(["Married", "Single", "Separated", "Divorced", "Widowed"]),
            "Phone Number": fake.nigerian_phone_number(),
            "Email": email,
            "Address": address,
            "Relationship to Student": relationship_type,
            "Income Bracket": fake.income_bracket(),
            "Education Level": fake.education_level(),
            "Occupation": fake.nigerian_job(),
            "Employment Type": fake.employment_type(),
            "Industry": fake.industry(),
            "Engagement Level": engagement_level,
            "Home Language": fake.home_language(),
            "Number of Children": number_of_children,
            "Alternate Contact Number": fake.nigerian_phone_number(),
            "Parent-Teacher Meeting Attendance": parent_teacher_meeting_attendance,
            "Volunteer Activities Count": volunteer_activities_count,
            "Recent Interaction Date": recent_interaction_date,
            "Created At": current_timestamp(),
            "Updated At": current_timestamp()
        })

    return pd.DataFrame(student_data), pd.DataFrame(parent_data)


# Function to generate term scores based on performance profiles
def generate_term_scores(profile):
    ca1 = int(random.gauss(profile["ca_mean"], profile["ca_std_dev"]))
    ca2 = int(random.gauss(profile["ca_mean"], profile["ca_std_dev"]))
    exam = int(random.gauss(profile["exam_mean"], profile["exam_std_dev"]))
    return max(0, min(15, ca1)), max(0, min(15, ca2)), max(10, min(70, exam))

def generate_student_teacher_mapping(subjects, teacher_df):
    """
    Randomly assign teachers to subjects for a given session.
    Each subject will have a unique teacher.
    """
    assigned_teachers = teacher_df.sample(len(subjects))
    return dict(zip(subjects, assigned_teachers["Teacher ID"].tolist()))

# Function to generate session data with extracurricular and health data for each term
def generate_session_data(student_df, grade_level, term_name, teacher_mapping):
    """
    Generate detailed session data including CA scores, attendance, teacher remarks,
    extracurricular activities (aggregated), and health records (incidence count) for each student.
    """
    subjects = core_subjects + streams[student_df["Stream"].iloc[0]]
    columns = ["Student ID", "Name", "Stream", 
               "Academic Year", "Grade Level", "Term"]

    # Extend columns to include CA1, CA2, Exam, Total, Attendance %, Teacher Remarks, and Teacher ID
    for subject in subjects:
        columns.extend([
            f"{subject} (CA1)", f"{subject} (CA2)", f"{subject} (Exam)", 
            f"{subject} (Total)", f"{subject} Attendance %", 
            f"{subject} Teacher Remarks", f"{subject} Teacher ID"])

    # Add columns for aggregated extracurricular activities and health records
    columns.extend([
        "Extracurricular Activities", "Extracurricular Activity Feedback", "Health Incidences", "Health Remarks",
        "Created At", "Updated At"
    ])

    data = []
    for _, student in student_df.iterrows():
        student_id = student["Student ID"]
        full_name = student["Full Name"]
        stream_name = student["Stream"]
        academic_year = academic_years[grade_level]
        profile = student["Profile"]

        # Initialize row for the student
        term_row = [student_id, full_name, stream_name, academic_year, grade_level, term_name]

        # Generate scores, attendance, remarks, and assign teacher for each subject
        for subject in subjects:
            ca1, ca2, exam = generate_term_scores(profile)
            total_score = ca1 + ca2 + exam
            attendance_percentage = round(random.uniform(40, 100), 2)
            remarks = fake.remark()

            # Generate the mapping key using stream and academic_year
            mapping_key = f"{academic_year}_{stream_name}_{subject}"
            teacher_id = teacher_mapping[mapping_key]

            # Extend the row with subject-specific data
            term_row.extend([ca1, ca2, exam, total_score, attendance_percentage, remarks, teacher_id])

        # Generate term-level extracurricular data
        activity_names = []
        activity_feedback = []
        num_activities = random.randint(1, 3)  # Random number of activities per student for the term

        for _ in range(num_activities):
            activity = random.choice(["Soccer", "Debate Club", "Art Club", "Science Club"])
            feedback = fake.sentence(nb_words=8)
            activity_names.append(activity)
            activity_feedback.append(feedback)

        # Join activities and feedback lists into strings
        activities = "; ".join(activity_names)
        feedback_combined = "; ".join(activity_feedback)

        # Generate term-level health data
        health_incidences = random.randint(0, 3)  # Simulated count of health incidences in the term
        health_remarks = fake.sentence(nb_words=10) if health_incidences > 0 else ""

        # Add extracurricular and health data to the row
        term_row.extend([
            activities, feedback_combined, health_incidences, health_remarks,
            current_timestamp(), current_timestamp()
        ])
        
        data.append(term_row)

    return pd.DataFrame(data, columns=columns)



def generate_teacher(subject):
    """
    Generate a teacher with relevant details.
    """
    teacher_id = f"TEA{random.randint(1000, 9999)}"
    first_name = fake.nigerian_first_name()
    middle_name = random.choice([fake.nigerian_first_name(), fake.first_name()])
    last_name = fake.nigerian_last_name()
    gender = random.choice(["Male", "Female"])
    date_of_birth = fake.date_of_birth(minimum_age=25, maximum_age=60)
    address = fake.nigerian_address()
    phone_number = fake.nigerian_phone_number()
    email = email = f"{first_name.lower()}.{last_name.lower()}{random.randint(10, 99)}@example.com"
    hire_date = fake.date_between(start_date=date(2014, 1, 1), end_date=date(2023, 10, 31))
    qualification = fake.qualification()
    years_of_experience = random.randint(1, 35)

    return {
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
        "Created At": current_timestamp(),
        "Updated At": current_timestamp()
    }

def generate_teachers(subjects, num_teachers_per_subject=3, core_subject_teachers=4):
    """
    Generates teachers with appropriate subject assignment, ensuring core subjects 
    have at least 4 teachers and other subjects have 1-3 teachers.
    """
    teacher_data = []
    assigned_teachers = {}

    for subject in subjects:
        # Determine the number of teachers needed for core vs non-core subjects
        num_teachers = core_subject_teachers if subject in core_subjects else random.randint(1, num_teachers_per_subject)

        # Generate the required number of teachers for the subject
        for _ in range(num_teachers):
            teacher = generate_teacher(subject)
            teacher_data.append(teacher)
            assigned_teachers.setdefault(subject, []).append(teacher["Teacher ID"])

    return pd.DataFrame(teacher_data), assigned_teachers

def generate_teacher_mapping(teacher_df, academic_year, stream):
    """
    Generate a mapping of teachers to subjects for a specific academic year and stream.
    The same teacher teaches the same subject across all students in the stream.
    """
    subjects = core_subjects + streams[stream]  # Combine core subjects with stream-specific subjects
    assigned_teachers = {}

    for subject in subjects:
        # Use the stream and academic_year to generate the correct key
        key = f"{academic_year}_{stream}_{subject}"
        if key not in assigned_teachers:
            # Randomly assign a teacher who teaches this subject
            teacher_id = random.choice(teacher_df[teacher_df["Subject"] == subject]["Teacher ID"].tolist())
            assigned_teachers[key] = teacher_id  # Assign this teacher to the subject for the stream

    return assigned_teachers


# Function to update Google Sheets with generated data for each term
def update_google_sheet(worksheet_name, dataframe, sheet_url):

    # Convert all date columns to string format
    dataframe = dataframe.astype(str)

    # Open Google Sheets
    sh = gc.open_by_url(sheet_url)
    try:
        worksheet = sh.worksheet(worksheet_name)
    except gspread.exceptions.WorksheetNotFound:
        worksheet = sh.add_worksheet(title=worksheet_name, rows=dataframe.shape[0] + 1, cols=dataframe.shape[1])
    worksheet.clear()
    worksheet.update([dataframe.columns.values.tolist()] + dataframe.values.tolist())
    print(f"Updated Google Sheet: {worksheet_name}")
    # Add delay to prevent quota exceeded error
    time.sleep(2) 

def main():
    # Initialize DataFrames for consolidated storage
    all_students_df = pd.DataFrame()
    all_parents_df = pd.DataFrame()

    # Generate and update 'teachers' sheet
    teacher_df, _ = generate_teachers(subjects=list(core_subjects + sum(streams.values(), [])), num_teachers_per_subject=3)
    update_google_sheet("Teachers Bio", teacher_df, SHEET_CONFIG["teachers"]["url"])

    # Loop through streams and generate student-parent pairs for each stream
    for stream in streams.keys():
        student_df, parent_df = generate_student_parent_pairs(stream, num_students=30)
        all_students_df = pd.concat([all_students_df, student_df], ignore_index=True)
        all_parents_df = pd.concat([all_parents_df, parent_df], ignore_index=True)

        # For each grade level and term, generate session data
        for grade in grade_levels:
            for term in terms:
                if grade == "SS3" and term == "Third":
                    continue

                # Generate teacher mapping for the current academic year and stream
                teacher_mapping = generate_teacher_mapping(teacher_df, academic_year=academic_years[grade], stream=stream)
                
                # Generate session data for students in the current grade, term, and stream
                results_df = generate_session_data(student_df, grade, term, teacher_mapping)
                sheet_name = f"{grade} {stream} {term} Term"
                update_google_sheet(sheet_name, results_df, SHEET_CONFIG["results"]["url"])
    
    all_students_df = all_students_df.drop(columns=["Profile", "Full Name"])

    # Generate and update 'students' and 'parents' sheet
    update_google_sheet("Students Bio", all_students_df, SHEET_CONFIG["students"]["url"])
    update_google_sheet("Parents Bio", all_parents_df, SHEET_CONFIG["parents"]["url"])

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
