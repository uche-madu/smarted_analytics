from datetime import date, datetime, timedelta
import time
import pandas as pd
import random
import gspread
from faker import Faker
from faker.providers import BaseProvider
from configs import SERVICE_ACCOUNT_FILE, SHEET_CONFIG


# Custom Provider for Nigerian Names and Addresses
class NigerianSchoolDataProvider(BaseProvider):
    """
    A custom provider to generate Nigerian-specific data for school-related information,
    such as student and teacher names, addresses, and demographic details. This provider
    extends the Faker library by adding culturally relevant methods specific to Nigerian contexts.
    """

    def nigerian_first_name(self):
        """
        Generates a Nigerian first name.

        This method provides culturally specific first names commonly found in Nigeria, covering
        diverse regions and ethnic backgrounds. It is useful for data generation in applications
        requiring Nigerian names or simulated datasets for Nigerian populations.

        Returns:
            str: A string representing a Nigerian first name.
        """
        first_names = [
            "Chinedu",
            "Ngozi",
            "Yemi",
            "Bola",
            "Ifeanyi",
            "Uche",
            "Amina",
            "Emeka",
            "Nkechi",
            "Tope",
            "Chika",
            "Bisi",
            "Femi",
            "Kunle",
            "Gbenga",
            "Tolu",
            "Funmi",
            "Ada",
            "Olu",
            "Sade",
            "Dapo",
            "Kehinde",
            "Nnamdi",
            "Kemi",
            "Chinonso",
            "Ebele",
            "Obinna",
            "Amara",
            "Chidera",
            "Olumide",
            "Bankole",
            "Ezinne",
            "Chimamanda",
            "Yinka",
            "Ayo",
            "Dele",
            "Chiamaka",
            "Omotola",
            "Segun",
            "Kolawole",
            "Sikiru",
            "Maryam",
            "Fatimah",
            "Toyin",
            "Kudirat",
            "Abdul",
            "Rukayat",
            "Efe",
            "Mfon",
            "Oghenekaro",
            "Adebisi",
            "Khadijah",
            "Ahmed",
            "Yusuf",
            "Jide",
            "Temitope",
            "Tosin",
            "Nafisat",
            "Hadiza",
            "Aisha",
            "Taiwo",
            "Bimbo",
            "Gbadebo",
            "Simisola",
            "Zainab",
            "Saheed",
            "Ifeoma",
            "Ndidi",
            "Tajudeen",
            "Emmanuella",
            "Chukwuemeka",
            "Onyeka",
            "Ndubisi",
            "Oluwatobiloba",
            "Yemisi",
            "Oluwasegun",
            "Eunice",
            "Suliat",
            "Anike",
            "Usman",
            "Adebola",
            "Oluwanifemi",
            "Ayodeji",
            "Mojirayo",
            "Chisom",
            "Efeoma",
            "Muna",
            "Obiageli",
            "Yewande",
        ]
        return self.random_element(first_names)

    def nigerian_last_name(self):
        """
        Generates a Nigerian last name.

        This method provides Nigerian last names reflective of various ethnic backgrounds,
        supporting data simulations that require surnames common across Nigeria. It serves
        well for databases or test data tailored for Nigerian user bases.

        Returns:
            str: A string representing a Nigerian last name.
        """
        last_names = [
            "Okafor",
            "Balogun",
            "Olawale",
            "Eze",
            "Ibrahim",
            "Adesina",
            "Ogunleye",
            "Nwosu",
            "Osagie",
            "Okonkwo",
            "Chukwu",
            "Alabi",
            "Onyejekwe",
            "Obi",
            "Ojo",
            "Adeola",
            "Adebayo",
            "Anyanwu",
            "Ajayi",
            "Ogbemudia",
            "Awolowo",
            "Ikenna",
            "Akintola",
            "Oni",
            "Odugbemi",
            "Adeyemi",
            "Ikechukwu",
            "Etuk",
            "Okorie",
            "Amaechi",
            "Ogbonna",
            "Agbaje",
            "Chukwuma",
            "Adegoke",
            "Ogunmola",
            "Musa",
            "Sanusi",
            "Oyeleke",
            "Opeoluwa",
            "Bello",
            "Obafemi",
            "Danjuma",
            "Adamu",
            "Muhammad",
            "Ozor",
            "Gadzama",
            "Oboh",
            "Ekechukwu",
            "Olaniyan",
            "Olojede",
            "Orji",
            "Nwachukwu",
            "Umeh",
            "Uzor",
            "Anosike",
            "Odeleye",
            "Olatunji",
            "Falade",
            "Dare",
            "Bakare",
            "Fashola",
            "Jaiyeola",
            "Adigun",
            "Adewole",
            "Orjiakor",
            "Onochie",
            "Adeyinka",
            "Olubiyi",
            "Omoruyi",
            "Idowu",
            "Omoyeni",
            "Obasanya",
            "Olaide",
            "Oluwole",
            "Ogunsanwo",
            "Oshin",
            "Kasim",
            "Obiano",
            "Ejiogu",
        ]
        return self.random_element(last_names)

    def nigerian_address(self):
        """
        Randomly generates a Nigerian address to simulate a residential or business location.

        Addresses cover various cities and well-known streets, reflecting a mix of metropolitan
        and regional areas across Nigeria. This is useful for creating localized data for testing
        or simulation within Nigerian settings.

        Returns:
            str: A string representing a Nigerian address.
        """
        addresses = [
            "12 Adeola Avenue, Lagos",
            "45 Ibrahim Street, Abuja",
            "23 Balogun Close, Ikeja, Lagos",
            "9 Aminu Kano Crescent, Wuse, Abuja",
            "17 Glover Road, Ikoyi, Lagos",
            "32 Nnamdi Azikiwe Drive, Enugu",
            "18 Oluwole Street, Ibadan",
            "15 Ogbemudia Street, Benin",
            "22 Oniru Crescent, Victoria Island, Lagos",
            "1 Awolowo Road, Ikoyi, Lagos",
            "33 Ogundana Street, Ikeja, Lagos",
            "10 Marina Road, Victoria Island, Lagos",
            "14 Opebi Road, Ikeja, Lagos",
            "27 Ahmadu Bello Way, Victoria Island, Lagos",
            "5 Okonjo-Iweala Street, Abuja",
            "30 Asokoro Avenue, Asokoro, Abuja",
            "7 Maitama Crescent, Maitama, Abuja",
            "8 Aguiyi Ironsi Street, Maitama, Abuja",
            "21 Awka Road, Onitsha, Anambra",
            "35 New Haven Road, Enugu",
            "42 Ngwo Street, Enugu",
            "15 Herbert Macaulay Way, Yaba, Lagos",
            "12 Bankole Street, Lagos Island, Lagos",
            "19 Alimosho Road, Egbeda, Lagos",
            "6 Surulere Avenue, Surulere, Lagos",
            "2 Allen Avenue, Ikeja, Lagos",
            "25 Bode Thomas Street, Surulere, Lagos",
            "11 Wetheral Road, Owerri, Imo",
            "16 Tetlow Road, Owerri, Imo",
            "23 Egbu Road, Owerri, Imo",
            "9 Olu Obasanjo Road, Port Harcourt, Rivers",
            "22 Old Aba Road, Port Harcourt, Rivers",
            "17 Elelenwo Street, Port Harcourt, Rivers",
            "4 Sani Abacha Way, Kano",
            "29 Yankari Close, Kano",
            "7 Shehu Shagari Way, Kano",
            "18 Makurdi Road, Kaduna",
            "33 Yakubu Gowon Way, Kaduna",
            "12 Tafawa Balewa Way, Bauchi",
            "19 Ahmadu Bello Street, Bauchi",
            "15 Jos Road, Bauchi",
            "23 Muhammadu Buhari Way, Minna",
            "27 Paiko Road, Minna",
            "14 Airport Road, Benin",
            "32 Ugbor Road, Benin",
            "8 Boundary Road, Benin",
            "5 Orelope Street, Osogbo, Osun",
            "17 Gbongan Road, Osogbo, Osun",
            "30 Mokola Road, Ibadan, Oyo",
            "9 Dugbe Street, Ibadan, Oyo",
            "11 Ring Road, Ibadan, Oyo",
            "7 Iwo Road, Ibadan, Oyo",
            "3 Queen Elizabeth Road, Ilorin, Kwara",
            "16 Taiwo Road, Ilorin, Kwara",
            "25 Asa Dam Road, Ilorin, Kwara",
            "8 Stadium Road, Calabar, Cross River",
            "13 Marian Road, Calabar, Cross River",
            "21 Moore Road, Calabar, Cross River",
        ]
        return self.random_element(addresses)

    def state_of_origin(self):
        """
        Randomly selects a Nigerian state as a state of origin for an individual.

        States are representative of all geopolitical regions within Nigeria, providing a diverse
        range for regional distribution of data, which may be useful for simulations or testing
        localized demographic information.

        Returns:
            str: A string representing a Nigerian state.
        """
        states_of_origin = [
            "Abia",
            "Adamawa",
            "Akwa Ibom",
            "Anambra",
            "Bauchi",
            "Bayelsa",
            "Benue",
            "Borno",
            "Cross River",
            "Delta",
            "Ebonyi",
            "Edo",
            "Ekiti",
            "Enugu",
            "FCT",
            "Gombe",
            "Imo",
            "Jigawa",
            "Kaduna",
            "Kano",
            "Katsina",
            "Kebbi",
            "Kogi",
            "Kwara",
            "Lagos",
            "Nasarawa",
            "Niger",
            "Ogun",
            "Ondo",
            "Osun",
            "Oyo",
            "Plateau",
            "Rivers",
            "Sokoto",
            "Taraba",
            "Yobe",
            "Zamfara",
        ]
        return self.random_element(states_of_origin)

    def home_language(self):
        """
        Randomly selects a language commonly spoken at home in Nigeria, representing
        cultural and linguistic diversity.

        Languages include major regional languages and dialects, supporting data
        generation for projects that require linguistic demographics or simulate multilingual
        settings in Nigeria.

        Returns:
            str: A string representing a home language.
        """
        languages = [
            "English",
            "Yoruba",
            "Igbo",
            "Hausa",
            "Efik",
            "Ibibio",
            "Ijaw",
            "Tiv",
            "Edo",
            "Fulfulde",
            "Kanuri",
            "Nupe",
            "Gwari",
            "Itsekiri",
            "Urhobo",
            "Ikwere",
            "Jukun",
            "Idoma",
        ]
        return self.random_element(languages)

    def income_bracket(self):
        """
        Randomly selects an income bracket that represents the socio-economic
        status of individuals based on annual income levels in Nigeria.

        Brackets range from low to high income, with descriptions:
            - "Below 100,000 Naira": Low income
            - "100,000 - 500,000 Naira": Lower-middle income
            - "500,000 - 1,000,000 Naira": Middle income
            - "1,000,000 - 3,000,000 Naira": Upper-middle income
            - "Above 3,000,000 Naira": High income

        Returns:
            str: A string representing an income bracket.
        """
        brackets = [
            "Below 100,000 Naira",
            "100,000 - 500,000 Naira",
            "500,000 - 1,000,000 Naira",
            "1,000,000 - 3,000,000 Naira",
            "Above 3,000,000 Naira",
        ]
        return self.random_element(brackets)

    def education_level(self):
        """
        Randomly selects an education level to represent the highest educational
        attainment of individuals, capturing a range from primary to doctoral levels.

        Levels include:
            - "Primary School": Basic education
            - "Secondary School": Intermediate education
            - "Technical/Vocational": Specialized non-academic training
            - "Diploma": Post-secondary but pre-bachelor's education
            - "Bachelor": Undergraduate degree
            - "Master": Graduate degree
            - "PhD": Doctoral degree
            - "Uneducated": No formal education

        Returns:
            str: A string representing an education level.
        """
        education_levels = [
            "Primary School",
            "Secondary School",
            "Technical/Vocational",
            "Diploma",
            "Bachelor",
            "Master",
            "PhD",
            "Uneducated",
        ]
        return self.random_element(education_levels)

    def employment_type(self):
        """
        Randomly selects an employment type to represent the employment status and
        work arrangement of individuals in various sectors.

        Types include:
            - "Full-Time": Regular, long-term employment
            - "Part-Time": Reduced hours
            - "Self-Employed": Own business or freelance work
            - "Unemployed": Not currently employed
            - "Contract": Short-term or project-based employment
            - "Freelancer": Independent contractor with variable projects
            - "Informal Sector": Non-traditional or unregulated work

        Returns:
            str: A string representing an employment type.
        """
        employment_types = [
            "Full-Time",
            "Part-Time",
            "Self-Employed",
            "Unemployed",
            "Contract",
            "Freelancer",
            "Informal Sector",
        ]
        return self.random_element(employment_types)

    def industry(self):
        """
        Randomly selects an industry representing the professional sector
        in which individuals are employed.

        Common industries include:
            - "Education": Schools, colleges, universities, etc.
            - "Healthcare": Hospitals, clinics, pharmaceuticals
            - "Finance": Banks, insurance, financial services
            - "Retail": Shopping, sales, consumer goods
            - "Technology": IT, software, telecommunications
            - "Agriculture": Farming, livestock, forestry
            - "Government": Public administration and services
            - "Manufacturing": Production of goods
            - "Entertainment": Media, film, music, sports

        Returns:
            str: A string representing an industry sector.
        """
        industries = [
            "Education",
            "Healthcare",
            "Finance",
            "Retail",
            "Construction",
            "Agriculture",
            "Transportation",
            "Technology",
            "Hospitality",
            "Telecommunications",
            "Oil & Gas",
            "Government",
            "Manufacturing",
            "Entertainment",
            "Mining",
            "Legal",
            "Other",
        ]
        return self.random_element(industries)

    def nigerian_job(self):
        """
        Randomly selects a job title from a wide range of common professions in Nigeria.

        Jobs cover various sectors and roles, including:
            - "Teacher", "Doctor", "Engineer" for professional roles
            - "Civil Servant", "Banker" for institutional roles
            - "Trader", "Farmer", "Tailor" for informal sector jobs
            - "Software Developer", "Data Analyst" for modern industry roles

        Returns:
            str: A string representing a job title.
        """
        jobs = [
            "Teacher",
            "Doctor",
            "Engineer",
            "Accountant",
            "Nurse",
            "Banker",
            "Civil Servant",
            "Lawyer",
            "Pharmacist",
            "Lecturer",
            "Police Officer",
            "Journalist",
            "Entrepreneur",
            "Software Developer",
            "Mechanic",
            "Electrician",
            "Farmer",
            "Tailor",
            "Fashion Designer",
            "Chef",
            "Driver",
            "Plumber",
            "Architect",
            "Scientist",
            "Environmentalist",
            "Social Worker",
            "Graphic Designer",
            "Consultant",
            "Data Analyst",
            "Digital Marketer",
            "Project Manager",
            "HR Manager",
            "Business Analyst",
            "Sales Representative",
            "Real Estate Agent",
            "Photographer",
            "Event Planner",
            "Security Officer",
            "Financial Advisor",
            "Fitness Trainer",
            "Insurance Agent",
            "Bank Teller",
            "Medical Lab Scientist",
            "Radiologist",
            "Administrative Assistant",
            "Procurement Officer",
            "Public Relations Officer",
            "Community Health Worker",
            "Veterinarian",
            "Public Health Specialist",
            "Trader",
            "Clergy",
        ]
        return self.random_element(jobs)

    def nigerian_phone_number(self):
        """
        Generates a realistic Nigerian phone number.

        The phone number consists of a randomly selected Nigerian prefix followed by
        eight random digits. Common Nigerian prefixes include "070", "080", "081", "090",
        and "091".

        Returns:
            str: A string representing a Nigerian phone number in the format "0XXXXXXXXX".
        """
        # Nigerian phone number prefixes
        prefixes = ["070", "080", "081", "090", "091"]
        # Select a random prefix and append 8 random digits
        phone_number = f"{random.choice(prefixes)}{random.randint(10000000, 99999999)}"
        return phone_number

    def blood_group(self):
        """
        Randomly selects a blood group from the commonly known blood types.

        Blood groups include both positive and negative types for groups A, B, AB, and O.

        Returns:
            str: A string representing a blood group (e.g., "A+", "O-").
        """
        blood_groups = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
        return self.random_element(blood_groups)

    def subject(self):
        """
        Randomly selects a subject from a predefined list of school subjects.

        Subjects cover a range of areas, including core subjects (e.g., English, Mathematics)
        and specialized areas (e.g., Technical Drawing, Commerce).

        Returns:
            str: A string representing the name of a school subject.
        """
        subjects = [
            "English Language",
            "Mathematics",
            "Civic Education",
            "Biology",
            "Physics",
            "Chemistry",
            "Further Mathematics",
            "Health Education",
            "Computer Science",
            "Technical Drawing",
            "Food and Nutrition",
            "Agricultural Science",
            "Financial Accounting",
            "Book Keeping",
            "Commerce",
            "Data Processing",
            "Office Practice",
            "Typewriting",
            "Economics",
            "Government",
            "Literature in English",
            "Christian Religion Knowledge",
            "Geography",
            "Fine Art",
        ]
        return self.random_element(subjects)

    def genotype(self):
        """
        Randomly selects a genotype from a list of common human genotypes.

        Genotypes include "AA", "AS", "SS", and "AC", representing possible genetic
        traits for blood.

        Returns:
            str: A string representing a human genotype (e.g., "AA", "SS").
        """
        genotypes = ["AA", "AS", "SS", "AC"]
        return self.random_element(genotypes)

    def marital_status(self):
        """
        Randomly selects a marital status from common options.

        This includes statuses like "Married", "Single", "Divorced", "Separated", and "Widowed".

        Returns:
            str: A string representing a marital status.
        """
        marital_status = ["Married", "Single", "Divorced", "Separated", "Widowed"]
        return self.random_element(marital_status)

    def qualification(self):
        """
        Randomly selects a professional or educational qualification from common levels.

        Qualifications include various academic degrees like "B.Ed.", "M.Sc.", "B.Sc.",
        and other certifications relevant to professional fields.

        Returns:
            str: A string representing an educational or professional qualification.
        """
        qualifications = ["B.Ed.", "M.Sc.", "B.Sc.", "PGDE", "M.A.", "M.Ed."]
        return self.random_element(qualifications)

    def stream_name(self):
        """
        Randomly selects a stream (academic focus area) from a predefined list of streams
        representing different areas of study in secondary education.

        Each stream includes a list of subjects associated with it. Examples of streams include:
            - "Basic Science and Maths": Focused on scientific and mathematical subjects like Biology and Physics.
            - "Technical and Agricultural": Focused on technical skills and agricultural knowledge.
            - "Commercial": Centered around financial and business-related subjects.
            - "Liberal Arts and Social Science": Emphasizes social sciences, arts, and humanities.

        Returns:
            str: The name of a randomly selected stream.
        """
        streams = {
            "Basic Science and Maths": [
                "Biology",
                "Physics",
                "Chemistry",
                "Further Mathematics",
                "Health Education",
                "Computer Science",
            ],
            "Technical and Agricultural": [
                "Technical Drawing",
                "Food and Nutrition",
                "Agricultural Science",
                "Physics",
                "Chemistry",
                "Biology",
            ],
            "Commercial": [
                "Financial Accounting",
                "Book Keeping",
                "Commerce",
                "Data Processing",
                "Office Practice",
                "Typewriting",
            ],
            "Liberal Arts and Social Science": [
                "Economics",
                "Government",
                "Literature in English",
                "Christian Religion Knowledge",
                "Geography",
                "Fine Art",
            ],
        }
        return self.random_element(list(streams.keys()))

    def remark(self):
        """
        Randomly selects a teacher remark from a list of possible comments to provide feedback on a student’s performance.

        Remarks are designed to capture a range of teacher observations, from high praise to areas for improvement.
        Examples include:
            - "Excellent performance!"
            - "Needs improvement"
            - "Great improvement"
            - "Struggles with some concepts"

        Returns:
            str: A string representing a teacher's feedback remark.
        """
        teacher_remarks = [
            "Excellent performance!",
            "Needs improvement",
            "Good effort",
            "Outstanding!",
            "Satisfactory",
            "Below expectations",
            "Keep up the good work",
            "Poor attendance",
            "Well done",
            "Great improvement",
            "Average performance",
            "Shows potential",
            "Struggles with some concepts",
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
    "Basic Science and Maths": [
        "Biology",
        "Physics",
        "Chemistry",
        "Further Mathematics",
        "Health Education",
        "Computer Science",
    ],
    "Technical and Agricultural": [
        "Technical Drawing",
        "Food and Nutrition",
        "Agricultural Science",
        "Physics",
        "Chemistry",
        "Biology",
    ],
    "Commercial": [
        "Financial Accounting",
        "Book Keeping",
        "Commerce",
        "Data Processing",
        "Office Practice",
        "Typewriting",
    ],
    "Liberal Arts and Social Science": [
        "Economics",
        "Government",
        "Literature in English",
        "Christian Religion Knowledge",
        "Geography",
        "Fine Art",
    ],
}

academic_years = {"SS1": "2022/2023", "SS2": "2023/2024", "SS3": "2024/2025"}
terms = ["First", "Second", "Third"]
grade_levels = ["SS1", "SS2", "SS3"]
class_arms = {
    "Basic Science and Maths": "A",
    "Technical and Agricultural": "B",
    "Commercial": "C",
    "Liberal Arts and Social Science": "D",
}
terms_sessions = [
    {"term": term, "session": grade}
    for grade in grade_levels
    for term in terms
    if not (grade == "SS3" and term == "Third")
]

# Score distributions
performance_profiles = {
    "Poor": {"ca_mean": 5, "ca_std_dev": 3, "exam_mean": 30, "exam_std_dev": 10},
    "Average": {"ca_mean": 8, "ca_std_dev": 3, "exam_mean": 40, "exam_std_dev": 5},
    "Above Average": {
        "ca_mean": 12,
        "ca_std_dev": 3,
        "exam_mean": 50,
        "exam_std_dev": 10,
    },
}

# Assign probabilities for each profile
profile_probabilities = ["Poor"] * 15 + ["Average"] * 65 + ["Above Average"] * 20


# Helper function to create unique student ID
def create_student_id(year, count, stream_abbr):
    """
    Generates a unique student ID based on the admission year, sequential count,
    and stream abbreviation.

    Args:
        year (str): Admission year in the format 'YYYY'.
        count (int): Sequential number representing the student's order in their stream.
        stream_abbr (str): Abbreviation of the stream name (e.g., 'BS' for Basic Science).

    Returns:
        str: A unique student ID.
    """
    return f"{year}{count:04d}{stream_abbr}"


# Helper: Add Timestamps
def current_timestamp():
    """
    Returns the current date and time in a standardized string format.

    Returns:
        str: Current timestamp in 'YYYY-MM-DD HH:MM:SS' format.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# Function to generate names and IDs for students and parents
def generate_student_parent_pairs(stream_name, num_students=30):
    """
    Generates data for students and their respective parents, including unique IDs,
    names, and additional demographic information for each.

    Args:
        stream_name (str): The name of the stream (e.g., 'Basic Science and Maths').
        num_students (int): The number of student-parent pairs to generate.

    Returns:
        tuple: Two DataFrames, one for student data and one for parent data.
    """
    student_data = []
    parent_data = []

    # Generate unique data for each student-parent pair
    for i in range(1, num_students + 1):
        # Abbreviate stream name to form part of student ID
        stream_abbr = "".join([word[0] for word in stream_name.split()]).upper()
        student_id = create_student_id(YEAR_OF_ADMISSION, i, stream_abbr)

        # Randomly generate Nigerian names for students
        first_name = random.choice([fake.nigerian_first_name(), fake.first_name()])
        middle_name = random.choice([fake.nigerian_first_name(), fake.first_name()])
        last_name = fake.nigerian_last_name()
        full_name = f"{first_name} {middle_name} {last_name}"

        # Generate parent ID and details
        parent_id = f"PAR{random.randint(1000, 9999)}"
        parent_first_name = fake.nigerian_first_name()
        parent_middle_name = random.choice(
            [fake.nigerian_first_name(), fake.first_name()]
        )
        parent_gender = random.choice(["Male", "Female"])

        # Generate additional demographic details for students
        gender = random.choice(["Male", "Female"])
        date_of_birth = fake.date_of_birth(minimum_age=13, maximum_age=20)
        address = fake.nigerian_address()
        blood_group = fake.blood_group()
        genotype = fake.genotype()
        state_of_origin = fake.state_of_origin()
        registration_date = fake.date_between(
            start_date=date(2022, 8, 1), end_date=date(2022, 10, 31)
        )
        profile = performance_profiles[random.choice(profile_probabilities)]

        # Append generated student data to list
        student_data.append(
            {
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
                "Updated At": current_timestamp(),
            }
        )

        # Generate additional engagement and socio-economic details for parents
        engagement_level = random.randint(
            1, 10
        )  # Engagement score based on interactions
        relationship_type = random.choice(["Parent", "Relative", "Guardian"])
        number_of_children = random.randint(1, 5)
        email = f"{parent_first_name.lower()}.{last_name.lower()}{random.randint(10, 99)}@example.com"

        # Interaction metrics for parent
        parent_teacher_meeting_attendance = random.randint(0, 5)
        volunteer_activities_count = random.randint(0, 3)
        timestamp = datetime.strptime(current_timestamp(), "%Y-%m-%d %H:%M:%S")
        recent_interaction_date = timestamp - timedelta(days=random.randint(1, 180))

        # Append generated parent data to list
        parent_data.append(
            {
                "Parent ID": parent_id,
                "First Name": parent_first_name,
                "Middle Name": parent_middle_name,
                "Last Name": last_name,
                "Gender": parent_gender,
                "Marital Status": random.choice(
                    ["Married", "Single", "Separated", "Divorced", "Widowed"]
                ),
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
                "Updated At": current_timestamp(),
            }
        )

    # Return student and parent data as DataFrames
    return pd.DataFrame(student_data), pd.DataFrame(parent_data)


# Function to generate term scores based on performance profiles
def generate_term_scores(profile):
    """
    Generates continuous assessment (CA) and exam scores based on a specified performance profile.
    Each score is capped to realistic maximum values.

    Args:
        profile (dict): Performance profile containing mean and standard deviation values for CA and exam scores.

    Returns:
        tuple: CA1 score, CA2 score, and Exam score as integers.
    """
    # Generate CA and Exam scores within defined performance profile limits
    ca1 = int(random.gauss(profile["ca_mean"], profile["ca_std_dev"]))
    ca2 = int(random.gauss(profile["ca_mean"], profile["ca_std_dev"]))
    exam = int(random.gauss(profile["exam_mean"], profile["exam_std_dev"]))

    # Return scores clamped within realistic ranges
    return max(0, min(15, ca1)), max(0, min(15, ca2)), max(10, min(70, exam))


def generate_student_teacher_mapping(subjects, teacher_df):
    """
    Randomly assigns a unique teacher for each subject in a session.

    Args:
        subjects (list): List of subjects for which teachers need to be assigned.
        teacher_df (DataFrame): DataFrame containing teacher IDs and other teacher details.

    Returns:
        dict: Mapping of each subject to a unique teacher ID.
    """
    # Randomly sample and assign teachers from the teacher DataFrame
    assigned_teachers = teacher_df.sample(len(subjects))

    # Return dictionary mapping each subject to a teacher's ID
    return dict(zip(subjects, assigned_teachers["Teacher ID"].tolist()))


# Function to generate session data with extracurricular and health data for each term
def generate_session_data(student_df, grade_level, term_name, teacher_mapping):
    """
    Generates detailed term/session data for each student, including academic performance
    metrics, extracurricular participation, and health records.

    Args:
        student_df (DataFrame): DataFrame containing student information.
        grade_level (str): Grade level (e.g., "SS1", "SS2", "SS3").
        term_name (str): Term name (e.g., "First", "Second", "Third").
        teacher_mapping (dict): Mapping of subjects to teacher IDs for the specific session.

    Returns:
        DataFrame: Generated session data including academic, extracurricular, and health details.
    """
    # Subjects for the term, combining core subjects with those specific to the student's stream
    subjects = core_subjects + streams[student_df["Stream"].iloc[0]]

    # Initialize columns to include general student and academic details
    columns = ["Student ID", "Name", "Stream", "Academic Year", "Grade Level", "Term"]

    # Expand columns to include academic performance and teacher details for each subject
    for subject in subjects:
        columns.extend(
            [
                f"{subject} (CA1)",
                f"{subject} (CA2)",
                f"{subject} (Exam)",
                f"{subject} (Total)",
                f"{subject} Attendance %",
                f"{subject} Teacher Remarks",
                f"{subject} Teacher ID",
            ]
        )

    # Add columns for extracurricular and health data
    columns.extend(
        [
            "Extracurricular Activities",
            "Extracurricular Activity Feedback",
            "Health Incidences",
            "Health Remarks",
            "Created At",
            "Updated At",
        ]
    )

    data = []  # Store each student's data row

    # Generate detailed session data for each student
    for _, student in student_df.iterrows():
        student_id = student["Student ID"]
        full_name = student["Full Name"]
        stream_name = student["Stream"]
        academic_year = academic_years[grade_level]
        profile = student["Profile"]

        # Initialize row with general student details
        term_row = [
            student_id,
            full_name,
            stream_name,
            academic_year,
            grade_level,
            term_name,
        ]

        # Generate scores, attendance, remarks, and assign teacher for each subject
        for subject in subjects:
            ca1, ca2, exam = generate_term_scores(profile)
            total_score = ca1 + ca2 + exam
            attendance_percentage = round(random.uniform(40, 100), 2)
            remarks = fake.remark()

            # Retrieve assigned teacher ID using mapping key
            mapping_key = f"{academic_year}_{stream_name}_{subject}"
            teacher_id = teacher_mapping[mapping_key]

            # Add subject-specific data to the row
            term_row.extend(
                [
                    ca1,
                    ca2,
                    exam,
                    total_score,
                    attendance_percentage,
                    remarks,
                    teacher_id,
                ]
            )

        # Generate term-level extracurricular and health data
        activity_names = []
        activity_feedback = []
        num_activities = random.randint(1, 3)  # Random number of activities per student

        for _ in range(num_activities):
            activity = random.choice(
                ["Soccer", "Debate Club", "Art Club", "Science Club"]
            )
            feedback = fake.sentence(nb_words=8)
            activity_names.append(activity)
            activity_feedback.append(feedback)

        # Concatenate activities and feedback for storage
        activities = "; ".join(activity_names)
        feedback_combined = "; ".join(activity_feedback)

        # Health data
        health_incidences = random.randint(
            0, 3
        )  # Number of health incidences in the term
        health_remarks = fake.sentence(nb_words=10) if health_incidences > 0 else ""

        # Append extracurricular and health data to the row
        term_row.extend(
            [
                activities,
                feedback_combined,
                health_incidences,
                health_remarks,
                current_timestamp(),
                current_timestamp(),
            ]
        )

        # Add the row to data list
        data.append(term_row)

    # Convert the list of rows to a DataFrame with the predefined columns
    return pd.DataFrame(data, columns=columns)


def generate_teacher(subject):
    """
    Creates a teacher record with randomly generated details, including
    personal information, qualifications, and contact information.

    Args:
        subject (str): Subject assigned to the teacher.

    Returns:
        dict: A dictionary representing a teacher's details.
    """
    teacher_id = f"TEA{random.randint(1000, 9999)}"  # Unique teacher ID
    first_name = fake.nigerian_first_name()
    middle_name = random.choice([fake.nigerian_first_name(), fake.first_name()])
    last_name = fake.nigerian_last_name()
    gender = random.choice(["Male", "Female"])
    date_of_birth = fake.date_of_birth(minimum_age=25, maximum_age=60)
    address = fake.nigerian_address()
    phone_number = fake.nigerian_phone_number()

    # Construct email from teacher's name and random number
    email = (
        f"{first_name.lower()}.{last_name.lower()}{random.randint(10, 99)}@example.com"
    )
    hire_date = fake.date_between(
        start_date=date(2014, 1, 1), end_date=date(2023, 10, 31)
    )
    qualification = fake.qualification()
    years_of_experience = random.randint(1, 35)

    # Return teacher record as a dictionary
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
        "Updated At": current_timestamp(),
    }


def generate_teachers(subjects, num_teachers_per_subject=3, core_subject_teachers=4):
    """
    Generates multiple teacher records with assignments for specified subjects.
    Ensures core subjects are assigned a higher number of teachers.

    Args:
        subjects (list): List of subjects for teacher assignments.
        num_teachers_per_subject (int): Number of teachers for non-core subjects.
        core_subject_teachers (int): Minimum number of teachers assigned to core subjects.

    Returns:
        tuple: DataFrame of teacher records and a dictionary of subject-to-teacher assignments.
    """
    teacher_data = []  # List to store generated teacher records
    assigned_teachers = {}  # Dictionary to store subject-to-teacher assignments

    for subject in subjects:
        # Determine the number of teachers for core vs non-core subjects
        num_teachers = (
            core_subject_teachers
            if subject in core_subjects
            else random.randint(1, num_teachers_per_subject)
        )

        # Generate teachers for the subject and add them to records
        for _ in range(num_teachers):
            teacher = generate_teacher(subject)
            teacher_data.append(teacher)
            assigned_teachers.setdefault(subject, []).append(teacher["Teacher ID"])

    # Convert teacher data to DataFrame and return with assignments
    return pd.DataFrame(teacher_data), assigned_teachers


def generate_teacher_mapping(teacher_df, academic_year, stream):
    """
    Creates a mapping of teachers to subjects for a given academic year and stream.
    Ensures each subject in a stream is taught by the same teacher across all students.

    Args:
        teacher_df (DataFrame): DataFrame containing teacher details.
        academic_year (str): Academic year (e.g., "2022/2023").
        stream (str): Stream name indicating specialization (e.g., "Science", "Commerce").

    Returns:
        dict: Mapping of academic year, stream, and subject to teacher IDs.
    """
    subjects = core_subjects + streams[stream]  # List of subjects in core and stream
    assigned_teachers = {}  # Store assignments with stream and academic year as key

    for subject in subjects:
        # Create unique mapping key and assign a teacher if not already assigned
        key = f"{academic_year}_{stream}_{subject}"
        if key not in assigned_teachers:
            teacher_id = random.choice(
                teacher_df[teacher_df["Subject"] == subject]["Teacher ID"].tolist()
            )
            assigned_teachers[key] = teacher_id

    # Return mapping of subjects to assigned teacher IDs
    return assigned_teachers


# Function to update Google Sheets with generated data for each term
def update_google_sheet(worksheet_name, dataframe, sheet_url):
    """
    Updates a specified Google Sheets worksheet with data from a DataFrame.
    If the worksheet does not exist, it is created. Clears existing data before updating.

    Args:
        worksheet_name (str): Name of the worksheet to update or create.
        dataframe (DataFrame): DataFrame containing data to write to the worksheet.
        sheet_url (str): URL of the Google Sheet to update.

    Returns:
        None
    """
    # Convert all date columns to string format to ensure compatibility with Google Sheets
    dataframe = dataframe.astype(str)

    # Open the specified Google Sheet using service account credentials
    sh = gc.open_by_url(sheet_url)
    try:
        # Try to access the worksheet by name
        worksheet = sh.worksheet(worksheet_name)
    except gspread.exceptions.WorksheetNotFound:
        # If not found, add a new worksheet with appropriate dimensions
        worksheet = sh.add_worksheet(
            title=worksheet_name, rows=dataframe.shape[0] + 1, cols=dataframe.shape[1]
        )
    worksheet.clear()  # Clear any existing data
    worksheet.update(
        [dataframe.columns.values.tolist()] + dataframe.values.tolist()
    )  # Write new data
    print(f"Updated Google Sheet: {worksheet_name}")

    # Add delay to prevent hitting the Google Sheets API quota
    time.sleep(2)


def main():
    """
    Main function that generates, processes, and uploads student, parent, and teacher data
    to Google Sheets.

    Workflow:
    - Generates teacher data and updates Google Sheet.
    - Iterates over each stream, generating and uploading student and parent data.
    - For each grade level and term in a stream, session data is generated and uploaded.

    Returns:
        None
    """
    # Initialize empty DataFrames to collect all students and parents data
    all_students_df = pd.DataFrame()
    all_parents_df = pd.DataFrame()

    # Generate teachers and update the 'Teachers Bio' sheet with teacher data
    teacher_df, _ = generate_teachers(
        subjects=list(core_subjects + sum(streams.values(), [])),
        num_teachers_per_subject=3,
    )
    update_google_sheet("Teachers Bio", teacher_df, SHEET_CONFIG["teachers"]["url"])

    # Iterate through each stream, generating students and parents data for the stream
    for stream in streams.keys():
        student_df, parent_df = generate_student_parent_pairs(stream, num_students=30)
        all_students_df = pd.concat([all_students_df, student_df], ignore_index=True)
        all_parents_df = pd.concat([all_parents_df, parent_df], ignore_index=True)

        # For each grade level and term, generate session data for students
        for grade in grade_levels:
            for term in terms:
                # Skip generating data for SS3 Third Term, as it may not be applicable
                if grade == "SS3" and term == "Third":
                    continue

                # Create teacher mapping specific to academic year, grade, and stream
                teacher_mapping = generate_teacher_mapping(
                    teacher_df, academic_year=academic_years[grade], stream=stream
                )

                # Generate session data, including scores and extracurricular activities
                results_df = generate_session_data(
                    student_df, grade, term, teacher_mapping
                )
                sheet_name = f"{grade} {stream} {term} Term"
                update_google_sheet(
                    sheet_name, results_df, SHEET_CONFIG["results"]["url"]
                )

    # Drop temporary columns from student DataFrame and upload student data
    all_students_df = all_students_df.drop(columns=["Profile", "Full Name"])
    update_google_sheet(
        "Students Bio", all_students_df, SHEET_CONFIG["students"]["url"]
    )

    # Upload parent data to Google Sheets
    update_google_sheet("Parents Bio", all_parents_df, SHEET_CONFIG["parents"]["url"])


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
