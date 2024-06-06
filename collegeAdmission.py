import nltk
from nltk.chat.util import Chat, reflections
nltk.download('punkt')
# Define conversational patterns with questions and answers

def main():
    pairs = [
        (r'.*steps.*college admission process.*', ["The steps involved in the college admission process may vary depending on the institution, but generally include researching colleges, completing applications, writing essays, submitting transcripts and test scores, and waiting for admission decisions."]),
        (r'.*apply.*college.*', ["To apply to a college, you typically need to complete an application form, submit transcripts and test scores, write essays, and pay an application fee."]),
        (r'.*documents.*required.*application.*', ["The documents required for a college application usually include transcripts, standardized test scores (e.g., SAT, ACT), letters of recommendation, and essays."]),
        (r'.*Common Application.*use.*', ["The Common Application is a standardized college application used by many colleges and universities. You can use it to apply to multiple colleges by filling out one application form."]),
        (r'.*submit.*application.*', ["You can usually submit your college application online through the college's website or through a centralized application system like the Common Application."]),
        (r'.*application fee.*much.*', ["The application fee for college applications varies by institution and can range from $50 to $100 or more. Some colleges may offer fee waivers for students with financial need."]),
        (r'.*apply.*multiple colleges.*', ["Yes, you can apply to multiple colleges at the same time. Many students apply to several colleges to increase their chances of acceptance."]),
        (r'.*GPA.*need.*get into college.*', ["The GPA needed to get into college varies depending on the institution and other factors. Generally, a higher GPA can improve your chances of admission."]),
        (r'.*standardized test scores.*required.*SAT.*ACT.*', ["Many colleges require standardized test scores such as the SAT or ACT for admission. The specific score requirements vary by college."]),
        (r'.*SAT Subject Tests.*', ["Some colleges may require or recommend SAT Subject Tests for admission. Check with individual colleges for their requirements."]),
        (r'.*importance.*extracurricular activities.*', ["Extracurricular activities can be important in the college application process as they demonstrate your interests, passions, and skills outside of academics."]),
        (r'.*letters of recommendation.*many.*', ["Many colleges require letters of recommendation as part of the application process. The number of letters required varies by college, but typically one to three letters are requested."]),
        (r'.*application deadlines.*colleges.*', ["Application deadlines for colleges vary, but they are typically in the fall or winter of your senior year of high school. Be sure to check the deadlines for each college you're applying to."]),
        (r'.*difference.*early action.*early decision.*regular decision.*', ["Early action, early decision, and regular decision are different types of application deadlines and admission plans. Early action and early decision have earlier deadlines and usually result in earlier admission decisions."]),
        (r'.*start preparing.*application.*', ["It's a good idea to start preparing your college application in your junior year of high school. This includes researching colleges, studying for standardized tests, and gathering materials for your application."]),
        (r'.*find out.*accepted.*', ["You will typically find out if you've been accepted to a college in the spring of your senior year of high school. Colleges will send out admission decisions by a certain date."]),
        (r'.*rolling admissions.*', ["Rolling admissions is a college admissions policy where applications are reviewed as they are received, and decisions are made on an ongoing basis. This means there is no set deadline for applying, and admissions decisions are made throughout the admissions cycle."]),
        (r'.*find colleges.*match my interests.*goals.*', ["You can find colleges that match your interests and goals by researching their academic programs, campus culture, extracurricular activities, and location. Many college search websites allow you to filter colleges based on these criteria."]),
        (r'.*factors.*consider.*choosing.*college.*', ["When choosing a college, consider factors such as academic programs, location, campus culture, size, cost, financial aid opportunities, and career services. It's important to visit campuses, talk to current students, and research each college thoroughly."]),
        (r'.*research colleges.*universities.*', ["You can research colleges and universities by visiting their websites, attending college fairs, scheduling campus tours, reading college guidebooks, and talking to current students or alumni. Additionally, you can use online resources such as college search engines and forums."]),
        (r'.*visit college campuses.*applying.*', ["Yes, you can visit college campuses before applying. Campus visits allow you to get a feel for the campus environment, interact with students and faculty, explore academic facilities, and learn more about the college's programs and services."]),
        (r'.*differences.*public.*private colleges.*', ["Public colleges are funded by state governments and tend to be larger, with lower tuition costs for in-state residents. Private colleges are funded by private sources and often have smaller class sizes, more personalized attention, and higher tuition costs."]),
        (r'.*know.*college.*accredited.*', ["You can check if a college is accredited by searching the U.S. Department of Education's Database of Accredited Postsecondary Institutions and Programs. Accreditation ensures that a college meets certain quality standards and allows students to receive federal financial aid."]),
        (r'.*transfer.*one college.*another.*', ["Yes, you can transfer from one college to another. Transfer policies vary by college, but you'll typically need to meet certain academic requirements and submit transcripts from your current college. It's important to research transfer credit policies and deadlines."]),
        (r'.*advantages.*attending.*community college.*transferring.*four-year institution.*', ["Attending a community college before transferring to a four-year institution can be advantageous because it often has lower tuition costs, smaller class sizes, and flexible scheduling options. It can also provide an opportunity to explore different academic interests before committing to a major."]),
        (r'.*college offers programs.*interested.*', ["You can find out if a college offers programs you're interested in by visiting its website, contacting the admissions office, and exploring its academic departments. Many colleges provide detailed information about their majors, minors, and special programs online."]),
        (r'.*benefits.*attending.*liberal arts college.*', ["Liberal arts colleges offer a broad-based education that emphasizes critical thinking, communication skills, and interdisciplinary learning. They often have small class sizes, close interaction with faculty, and opportunities for undergraduate research and internships."]),
        (r'.*admission requirements.*international students.*', ["Admission requirements for international students vary by college, but they typically include submitting transcripts, standardized test scores (such as the TOEFL or IELTS), proof of English proficiency, and financial documentation. Some colleges may also require essays or letters of recommendation."]),
        (r'.*homeschooled students apply to college.*', ["Yes, homeschooled students can apply to college. Admission requirements may vary for homeschooled students, but they typically include standardized test scores, transcripts or a portfolio of coursework, and letters of recommendation. Some colleges may also require interviews or additional documentation."]),
        (r'.*colleges.*require.*standardized test scores.*', ["Yes, some colleges don't require standardized test scores for admission. These colleges may use a test-optional or test-flexible admissions policy, allowing students to choose whether or not to submit their scores. It's important to check each college's admissions policies to see if test scores are required."]),
        (r'.*prepare for college entrance exams.*SAT.*ACT.*', ["You can prepare for college entrance exams like the SAT or ACT by studying test prep materials, taking practice tests, and seeking out tutoring or test prep courses. It's also important to familiarize yourself with the format and content of the exams and develop test-taking strategies."]),
        (r'.*differences.*SAT.*ACT exams.*', ["The SAT and ACT exams are both standardized tests used for college admissions, but they have some differences. The SAT focuses more on reasoning and problem-solving skills, while the ACT includes sections on English, math, reading, and science. Some students may perform better on one exam than the other, so it's important to consider your strengths and preferences."]),
        (r'.*retake.*SAT.*ACT.*improve.*score.*', ["Yes, you can retake the SAT or ACT to improve your score. Many students take these exams multiple times to achieve their desired scores. It's important to prepare thoroughly for each exam administration and focus on areas where you can improve."]),
    ]

    chatbot = Chat(pairs, reflections)
    default_response = "I'm sorry, I don't understand. Please try asking another question."
    print("Type your questions to get an answer (type 'exit' to end):")

    while True:
        try:
            user_input = input("--> ")
            if user_input.lower() == 'exit':
                print("Goodbye!")
                break
            response = chatbot.respond(user_input)
            print(response if response else default_response)
        except KeyboardInterrupt:
            print("....Exiting....")
            break
        except Exception as e:
            print(f"An error occured: {e}")
            continue


if __name__=="__main__":
    main()