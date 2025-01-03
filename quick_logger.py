# Establish the Python Logger  
import logging # built in python library that does not need to be installed 
import time    
from datetime import datetime
import os 
import talking_code as tc  
speaking_log = False
speaking_steps = False 

def set_speaking_log(on_off_setting = False): 
    global speaking_log
    speaking_log = on_off_setting

def get_speaking_log(): 
    return speaking_log  

def set_speaking_steps(on_off_setting = False): 
    global speaking_steps    
    speaking_steps = on_off_setting

def get_speaking_steps(): 
    return speaking_steps  

def talk(speech): 
    tc.say(speech) 
    return  

def set_start_time():
    start_time = time.time()
    return(start_time)

def create_logger_Start(solution_name, start_time):
    logging.basicConfig(level=logging.INFO, filename=solution_name + '.log',
                    filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')    
    process_start_time_stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'[:-3])
    logging.info(f'START {solution_name} ' + ('=' * 45) ) 
    logging.info(f'START {solution_name} Start Time = {process_start_time_stamp}')  
    logging.info(f'{solution_name} Step 0 - Initialize the configuration file parser')
#     return f'logger_started for {solution_name} at {process_start_time_stamp}'
    return logging

def create_logger_start(solution_name, start_time):
    logging.basicConfig(level=logging.INFO, filename=solution_name + '.log',
                    filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')    
    process_start_time_stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'[:-3])
    logging.info(f'START {solution_name} ' + ('=' * 45) ) 
    logging.info(f'START {solution_name} Start Time = {process_start_time_stamp}')  
    logging.info(f'{solution_name} Step 0 - Initialize the configuration file parser')
#     return f'logger_started for {solution_name} at {process_start_time_stamp}'
    return logging

def append_log_file(solution_name): 
    log_filename=solution_name + '.log'
    historical_log_filename=solution_name + '_history.log'

    with open(log_filename) as log_file:
        log_content = log_file.read()

    with open(historical_log_filename,'a') as historical_log_file:
        print(120*' ', file=historical_log_file)        
        print(120*'>', file=historical_log_file)       
        print(log_content, file=historical_log_file)  
        print(120*'<', file=historical_log_file)  
        print(120*' ', file=historical_log_file)    
    return(log_content)  

def calculate_process_performance(solution_name, process_start_time):
    import time
    stop_time = time.time() # establish the stop time of the overall process.
    process_duration = stop_time - process_start_time
    process_stop_time_stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'[:-3])
    
    logging.info(f'PERFORMANCE {solution_name} The total process duration was:{process_duration:.2f}') 
    logging.info(f'PERFORMANCE {solution_name} Stop Time = {process_stop_time_stamp}')  
    status = f'END   {solution_name} Duration Classification Error - Process Duration UNKNOWN' 
    if process_duration > 600.0:
        logging.info(f'PERFORMANCE {solution_name} LONG process duration greater than 10 Minutes:{process_duration:.2f}') 
        logging.info(f'PERFORMANCE {solution_name} Performance optimization is required')        
    elif process_duration > 120.0:
        logging.info(f'PERFORMANCE {solution_name} Medium process duration greater than 3 minutes:{process_duration:.2f}') 
        logging.info(f'PERFORMANCE {solution_name} Performance optimization is optional')           
    elif process_duration > 3.0:
        logging.info(f'PERFORMANCE {solution_name} Low process duration less than 3 minutes:{process_duration:.2f}') 
        logging.info(f'PERFORMANCE {solution_name} Performance optimization is optional')           
    elif process_duration < 3.0:
        logging.info(f'PERFORMANCE {solution_name} Short process duration less than 3 Seconds:{process_duration:.2f}') 
        logging.info(f'PERFORMANCE {solution_name} Performance optimization is not reccomended')           
    else:  
        status = f'PERFORMANCE {solution_name} Duration Classification Error - Process Duration UNKNOWN' 
        
    logging.info(f'END {solution_name} ' + ('=' * 45) )             
    return(status)

def set_start_time():
    start_time = time.time()
    return(start_time)

def pvlog(log_level, log_string):
    global speaking_log
    global speaking_steps    
    
    print(log_string)
    if speaking_log:
        tc.say(log_string)

    if speaking_steps:
        if log_string.find("Step") > -1:
            tc.say(log_string)        
        
    if log_level == 'debug':
        logging.debug(log_string)  
    if log_level == 'info':
        logging.info(log_string)  
    if log_level == 'warn':
        logging.warn(log_string)    
    if log_level == 'error':
        logging.error(log_string)    
    if log_level == 'critical':
        logging.critical(log_string)
      


 