import time
import pandas as pd
import random
import gspread
from faker import Faker
from faker.providers import BaseProvider
import os
from dotenv import load_dotenv

# Define a custom provider for Nigerian names
class NigerianNameProvider(BaseProvider):
    def nigerian_name(self):
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

        return f"{self.random_element(first_names)} {self.random_element(last_names)}"

# Initialize Faker and add the custom provider
fake = Faker()
fake.add_provider(NigerianNameProvider)

load_dotenv(dotenv_path=".google_sheet.env")

# Retrieve variables from the .env file
GOOGLE_SHEET_URL = os.getenv("GOOGLE_SHEET_URL")
SERVICE_ACCOUNT_FILE = os.getenv("SERVICE_ACCOUNT_FILE")
gc = gspread.service_account(filename=SERVICE_ACCOUNT_FILE)

# Define core and elective subjects for each stream
core_subjects = ["English Language", "Mathematics", "Civic Education"]
streams = {
    "Basic Science and Maths": ["Biology", "Physics", "Chemistry", "Further Mathematics", "Health Education", "Computer Science"],
    "Technical and Agricultural": ["Technical Drawing", "Food and Nutrition", "Agricultural Science", "Physics", "Chemistry", "Biology"],
    "Commercial": ["Financial Accounting", "Book Keeping", "Commerce", "Data Processing", "Office Practice", "Typewriting"],
    "Liberal Arts and Social Science": ["Economics", "Government", "Literature in English", "Christian Religion Knowledge", "Geography", "Fine Art"]
}

# Performance profile distributions
performance_profiles = {
    "Poor": {"ca_mean": 6, "ca_std_dev": 3, "exam_mean": 30, "exam_std_dev": 10},
    "Average": {"ca_mean": 10, "ca_std_dev": 3, "exam_mean": 40, "exam_std_dev": 5},
    "Above Average": {"ca_mean": 13, "ca_std_dev": 2, "exam_mean": 55, "exam_std_dev": 6}
}

# Map class arms to each stream
class_arms = {"Basic Science and Maths": "A", "Technical and Agricultural": "B", "Commercial": "C", "Liberal Arts and Social Science": "D"}

# Define grade levels, academic years, and terms
grade_levels = ["SS1", "SS2", "SS3"]
academic_years = {"SS1": "2022/2023", "SS2": "2023/2024", "SS3": "2024/2025"}
terms = ["First", "Second", "Third"]

# Assign probabilities for each profile
profile_probabilities = ["Poor"] * 20 + ["Average"] * 60 + ["Above Average"] * 20

# Function to generate master student lists for each stream
def generate_master_student_list_per_stream(stream_name, num_students=30):
    student_data = []
    for _ in range(num_students):
        student_id = f"{stream_name[:2].upper()}{random.randint(100, 999)}"
        name = fake.nigerian_name()  # Use Nigerian names here
        performance_profile = random.choice(profile_probabilities)
        student_data.append({"Student ID": student_id, "Name": name, "Stream": stream_name, "Profile": performance_profile})
    return pd.DataFrame(student_data)

# Create master student lists for each stream
master_student_lists = {stream: generate_master_student_list_per_stream(stream) for stream in streams.keys()}

# Function to generate term scores based on performance profiles
def generate_term_scores(profile):
    ca1 = int(random.gauss(profile["ca_mean"], profile["ca_std_dev"]))
    ca2 = int(random.gauss(profile["ca_mean"], profile["ca_std_dev"]))
    exam = int(random.gauss(profile["exam_mean"], profile["exam_std_dev"]))
    return max(0, min(15, ca1)), max(0, min(15, ca2)), max(10, min(70, exam))

# Function to generate session data from master list using performance profiles
def generate_session_data_from_master(stream_name, grade_level, term_name, master_df):
    columns = ["Student ID", "Name", "Stream", "Academic Year", "Class Arm", "Grade Level", "Term"]
    subjects = core_subjects + streams[stream_name]
    for subject in subjects:
        columns.extend([f"{subject} (CA1)", f"{subject} (CA2)", f"{subject} (Exam)"])
    data = []
    for _, row in master_df.iterrows():
        student_id = row["Student ID"]
        name = row["Name"]
        academic_year = academic_years[grade_level]
        class_arm = class_arms[stream_name]
        profile = performance_profiles[row["Profile"]]
        term_row = [student_id, name, stream_name, academic_year, class_arm, grade_level, term_name]
        for _ in subjects:
            ca1, ca2, exam = generate_term_scores(profile)
            term_row.extend([ca1, ca2, exam])
        data.append(term_row)
    return pd.DataFrame(data, columns=columns)

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

if __name__ == "__main__":   
    # Generate data for each stream, grade level, and term, and update Google Sheets
    for stream in streams.keys():
        master_df = master_student_lists[stream]
        for grade in grade_levels:
            for term in terms:
                term_df = generate_session_data_from_master(stream_name=stream, grade_level=grade, term_name=term, master_df=master_df)
                sheet_name = f"{grade}_{stream}_{term}".replace(" ", "_")
                update_google_sheet(sheet_name, term_df, GOOGLE_SHEET_URL)
