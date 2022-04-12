import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

# Header 
st.write('''
# Himani Chauhan
##### *Resume* 
''')

image = Image.open('dp.png')
st.image(image, width=250)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Strategically-minded data analyst with 4+ years’ experience in interpreting and analyzing data for driving business solutions. 
- Proficient in developing data pipelines, building data visualizations, and communicating data-driven solutions.
''')

# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://www.linkedin.com/in/himanichauhan05/" target="_blank">Himani Chauhan</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#skills">Skilla</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#certifications">Certifications</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([2,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

#####################
st.markdown('''
## Education
''')

txt('**Master of Information Systems**, *University of Arkansas*, Fayetteville, AR',
'Aug 2020')
st.markdown('''
- Specialization in `Business Analytics`
- GPA: `4.00`
- Honors: Member of Beta Gamma Sigma, Outstanding MIS Student 2020
- Courses: Data Management, Business Intelligence, Data Analytics, Decision Support Systems, IT Management
''')

txt('**Bachelor of Technology**, *Galgotias College of Engineering and Technology*, Noida, India',
'July 2017')
st.markdown('''
- Specialization in `Computer Science`
- GPA: `3.8`
- Courses: Data Mining, Database Management, Artificial Intelligence, Programming
''')

#####################
st.markdown('''
## Work Experience
''')

txt('**Customer Operations Analyst**, *Bulb*, Austin, TX',
'Nov 2020-Present')
st.markdown('''
- Created and maintained standardized BigQuery tables and views from JSON data
- Collaborated with cross functional teams and designed ad-hoc SQL queries to support multiple campaigns
- Optimized billing process via back-end automations including Google Apps Script, SQL, and Zapier, improving team efficiency by 5%
- Wrote technical specifications in JIRA for product team to implement billing system improvements
- Performed research on the new data flows using SQL and Looker to identify and support product enhancements
- Implemented an automated communications platform in Google Sheets, driving closed account dunning recovery up by 8%
- Developed and tracked revenue KPIs through building data pipelines and revenue dashboard in Looker
- Spearheaded revenue initiatives to revamp payment success rate by 10%
- Built customers credit profile by integrating Experian data with Bulb platform using DBT – facilitating data driven decisions 
- Designed controlled A/B tests to validate hypotheses derived from data trends
''')

txt('**Customer Insight Analyst Intern**, *E2Open*, Rogers, AR',
'May 2020-July 2020')
st.markdown('''
- Analyzed Sam’s Club data and designed week-over-week forecast dashboards in MicroStrategy for customers
- Performed ad-hoc pre and post COVID analysis on sales data and developed monthly KPI tracking reports
- Optimized MicroStrategy reports by ensuring optimal joins of queries and minimum SQL passes
''')

txt('**Graduate Assistant**, *University of Arkansas*, Fayetteville, AR',
'Aug 2019-May 2020')
st.markdown('''
- Tutored a graduate level class of 50+ students and assisted with advanced MS Excel, MS Word and MS Access concepts
- Conducted exploratory data analysis on students’ results using Python and implemented instructional changes to boost student performance by 5%
''')

txt('**Business Intelligence Analyst**, *Infosys*, Mysore, India',
'Oct 2017-July 2019')
st.markdown('''
- Gathered business requirements and designed SSIS packages to implement transformation logic for SunTrust bank.
- Wrote Python scripts to automate the monthly tasks during deployment, resulting in 10% reduction in manual work
- Executed nuanced SQL queries to extract, manipulate and validate the data reports
- Collaborated with internal and external business users and developers to assist with development of Tableau reports
''')

#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `JavaScript`, `SQL`')
txt3('Analytics', '`SSIS`, `SAS`, `numpy`,`Pandas`, `SciPy`, `Matplotlib`,`Seaborn`, `PowerBI`, `MS Excel`, `Google Sheets`, `Tableau`, `Looker`,`SSIS`, `MicroStrategy`,`Google Analytics`')
txt3('IDEs', '`Jupyter`, `Sublime Text`, `Visual Studio Code`, `PyCharm`')
txt3('Model Deployment', '`Streamlit`')
txt3('Database', '`MySQL`,`Microsoft SQL Server`, `MS Access`, `IBM DB2`, `BigQuery`')
txt3('Other tools', '`MS PowerPoint`, `MS Word`, `JIRA`, `Confluence`, `Asana`, `Zendesk`,`Zapier`, `MailChimp`, `Git`, `DBT`')

#####################
st.markdown('''
## Certifications
''')
txt2('Python', 'https://www.udemy.com/certificate/UC-17N0DYF1/')
txt2('Tableau Basics', 'https://www.udemy.com/certificate/UC-LA3K0173/')
txt2('Tableau Advanced', 'https://www.udemy.com/certificate/UC-S5Z8NOID/')
txt2('Google Analytics', 'https://analytics.google.com/analytics/academy/certificate/kCdkk0jjTbqnnNFgxtl8tQ')

####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/himanichauhan05/')
txt2('GitHub', 'https://github.com/Himani512')
txt2('Tableau', 'https://public.tableau.com/app/profile/himani3018')