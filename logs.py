import datetime as dt
import os
import pandas as pd

def checklog():
    logfile = 'logs/' + 'log-' + dt.datetime.now().strftime('%Y-%m-%d') + '.csv'
    con = os.path.exists(logfile)
    if not con:
        log_df = pd.DataFrame(columns=['user_id', 'action', 'timestamp'])
        log_df.to_csv(logfile, index=False)
    else:
        log_df = pd.read_csv(logfile)
    return log_df

def logging(user_id, action):
    global logfile
    logfile = 'logs/' + 'log-' + dt.datetime.now().strftime('%Y-%m-%d') + '.csv'
    log_df = checklog()
    new_log = pd.DataFrame({'user_id': [user_id], 'action': [action], 'timestamp': [dt.datetime.now()]})
    log_df = pd.concat([log_df, new_log], ignore_index=True)
    log_df.to_csv(logfile, index=False)


