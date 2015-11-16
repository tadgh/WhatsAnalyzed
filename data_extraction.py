import pandas as pd

file = "WhatsApp Chat with The Squad.txt" 

HEADERS = ["DATE", "TIME", "AUTHOR", "MESSAGE"]

df = pd.DataFrame(columns=HEADERS)

with open(file) as f:
    for line in f:
        initial_split = line.split('-')
        if len(initial_split) == 2:
            times = (initial_split[0]).split(',')

            if len(times) != 2:
                continue

            date = times[0]
            time = times[1]
    
            author = ""
            message = ""

            # Deal with messages separately
            if ":" not in initial_split[1]:
                # Keywords 'added' and 'changed'
                author = "System"
                message = initial_split[1]
            else:
                # Split on the *first* colon
                first_colon = initial_split[1].find(":")
                author = initial_split[1][:first_colon]
                message = initial_split[1][first_colon + 2:]
        
            # Add to the dataframe
            df.loc[len(df)+1] = [date, time, author, message]            

print df
        

