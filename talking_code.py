#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pyttsx3

Reading_Intro = True
Reading_Credits =  True
Reading_Steps = True 
Reading_Terms = True 
Talking_Code = False
Talking_Voice_Male_Gender = True     

def set_talking_code_Settings(Intro_Setting, Credits_Setting, Steps_Setting, Terms_Setting, Talking_Code_Setting, Talking_Gender ):
    global Reading_Intro 
    global Reading_Credits 
    global Reading_Steps 
    global Reading_Terms 
    global Talking_Code 
    global Talking_Voice_Male_Gender 
    Reading_Intro = Intro_Setting
    Reading_Credits = Credits_Setting  
    Reading_Steps = Steps_Setting
    Reading_Terms = Terms_Setting
    Talking_Code = Talking_Code_Setting
    Talking_Voice_Male_Gender = Talking_Gender 
 
    
def Initialize_Text_to_Speach():
    Text_to_Speech = pyttsx3.init()
    Text_to_Speech.setProperty('Rate',187)
    voices = Text_to_Speech.getProperty('voices')
    if Talking_Voice_Male_Gender:
        Text_to_Speech.setProperty('voice', voices[0].id)    # Default Male voice registered as 'Dave'
    else: 
        Text_to_Speech.setProperty('voice', voices[1].id)    # Alternate Female voice registered as 'Tina'
    speech = 'The text to speech engine is initialized using pythons pyttsx3 engine'
    Text_to_Speech.say(speech)
    Text_to_Speech.runAndWait()
    return Text_to_Speech

    
def initialize_text_to_speech():
    Text_to_Speech = pyttsx3.init()
    Text_to_Speech.setProperty('Rate',187)
    voices = Text_to_Speech.getProperty('voices')
    if Talking_Voice_Male_Gender:
        Text_to_Speech.setProperty('voice', voices[0].id)    # Default Male voice registered as 'Dave'
    else: 
        Text_to_Speech.setProperty('voice', voices[1].id)    # Alternate Female voice registered as 'Tina'
    speech = 'The text to speech engine is initialized using pythons pyttsx3 engine'
    Text_to_Speech.say(speech)
    Text_to_Speech.runAndWait()
    return Text_to_Speech
    
# Say Whatever the user wants 
def say(speech):
    Text_to_Speech = pyttsx3.init()
    Text_to_Speech.say(speech)
    Text_to_Speech.runAndWait()     
    
def print_say(speech):
    print(speech) 
    say(speech)
     
# Introduction - Overview of CSV to SQL Import Process Steps 
def read_credits(): 
    Dialog = 'This Jupiter Notebook Was  : '
    Dialog = Dialog + 'Developed in Collaboration by Joe Eberle, Alan Calhoun, Helmi (Al) Seoud  '
    Dialog = Dialog + 'Developed in Python starting on 9/20/2022 '
    Dialog = Dialog + 'This package is free AND Open Source and the code is openly available for general Use. '    
    say(Dialog)         
    
# Introduction - Overview of CSV to SQL Import Process Steps 
def read_terms(): 
    Dialog = 'The terminology for this process is : '
    Dialog = Dialog + 'Python. Python is a general-purpose programming language that is widely used for data science.  '
    Dialog = Dialog + 'Structured Query Language (SQL) is one of the worlds most widely used programming languages for manipulating and querying data. '
    Dialog = Dialog + 'CSV. A Comma-Separated Values (CSV)  file is a text file in which information is separated by commas. '
    Dialog = Dialog + 'PANDAS. Pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language.  '
    Dialog = Dialog + 'OS PACKAGE - The OS python library provides a portable way of using operating system dependent functionality to allow your python code to run on all platforms '
    say(Dialog)  
    
# Process Steps - Overview of CSV to SQL Import Process Steps 
def read_process_steps():
    Dialog = 'The data flow for this process is : '
    Dialog = Dialog + 'Precursor Step 1: The clinician or administrator enters the patients data into the Electronic Medical Record (EMR). '
    Dialog = Dialog + 'Precursor Step 2: At the end of the day the EMR data is exported into Comma Seperated Values (CSV) files and shared via SFTP. '
    Dialog = Dialog + 'Step 1: Establish The Root Directory. '
    Dialog = Dialog + 'Step 2: Walk the directory structure discovering data to discover all data directories  '
    Dialog = Dialog + 'Step 3: Read the CSV data from each directory into python a PANDAS Dataframe. '
    Dialog = Dialog + 'Step 4: Clean the data and make it consistent in the PANDAS Dataframe. ' 
    Dialog = Dialog + 'Step 5: Check the consistency of the data and perform change control if there are differences. ' 
    Dialog = Dialog + 'Step 6: Convert the pandas dataframes into SQL table Create Statements  '
    Dialog = Dialog + 'Step 7: Creates the SQL tables in the target Database   '
    Dialog = Dialog + 'Step 8: Insert the the PANDAS Rows into SQL using the to_SQL Method.  '
    Dialog = Dialog + 'Step 9: Add event logging to capture the performance of the entire process.  '
    Dialog = Dialog + 'Step 10: Document the SCHEMA into an easy to use Excel Spreadsheet.  '
    Dialog = Dialog + 'Step 11: Check the total number of records imported via SQL to the total raw record count to make sure no data is Left Behind.    '
    say(Dialog)    
    
    
# Introduction - Overview of NoteBooks  
def read_introduction():
    Dialog = 'This jupiter notebook will import all of the CSV files under a specific root directory into a database. '
    Dialog = Dialog +  'This python code will take the CSV files exported froms an Electronic Medical Record platform. '
    Dialog = Dialog + 'and import them into a faster database such as PostgreSQL or SQL Server or SNOW Flake. '
    Dialog = Dialog + 'the data is then available for anaylsis using query tools or ready for visualizations in Power BI or Tableau. '
    say(Dialog)  
    
    
def column_create_SQL (import_df):
    column_name_List = [x.title() for x in import_df.columns] # Create a List of Columns 
    column_Str =  (', '.join(column_name_List)) # Convert List into one String with commas 
    out('Columns =',column_Str)  
    return column_Str            
    
    
def out(dialog):
    if printing_output: 
        print(dialog) 
    if Talking_Code:
        say(dialog)     
        
def list_all_xlsx_files(path):
    extension = 'xlsx'
    os.chdir(path)
    csv_file_count = 0
    for file in glob.glob('*.{}'.format(extension)):
        csv_file_count += 1 
        out('File #{}   is {} '.format(csv_file_count,file))             
        
def explain_the_project():
    if Reading_Intro:
        read_introduction()
    if Reading_Credits:    
        read_credits() 
    if Reading_Steps:
        read_process_steps()
    if Reading_Terms:
        read_terms()        
        
        

