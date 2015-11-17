import pandas as pd
import datetime
import plots


def is_date(potential_date):
    # Thanks StackOverflow!
    # http://stackoverflow.com/questions/16870663/how-do-i-validate-a-date-string-format-in-python
    try:
        datetime.datetime.strptime(potential_date, "%d/%m/%Y")
        return True
    except ValueError:
        return False


def build_dataframe(filename):
    # Headers for the dataframe
    HEADERS = ["DATE", "TIME", "AUTHOR", "MESSAGE"]

    # Store data as we go so we only dump into the data frame once. This way the 
    # data frame doesn't constantly waste time resizing itself.
    data_dump = [] 

    with open(filename) as f:
        for line in f:
            # All message lines begin with a date
            potential_date = line[:line.find(',')]
            if is_date(potential_date):
                first_dash = line.find('-')
                initial_split = [line[:first_dash], line[first_dash + 2:]] 

                initial_split[0] = initial_split[0].replace(".", "")
                formatted_date = datetime.datetime.strptime(initial_split[0], "%d/%m/%Y, %I:%M %p ")
                date = formatted_date.date()
                time = formatted_date.time()
           
                author = ""
                message = ""

                if ":" not in initial_split[1]:
                    # Keywords 'added' and 'changed'
                    author = "System"
                    message = initial_split[1]
                else:
                    # Split on the *first* colon
                    first_colon = initial_split[1].find(":")
                    author = initial_split[1][:first_colon]
                    message = initial_split[1][first_colon + 2:]
               
                # Add to the temporary data list
                data_dump.append([date, time, author, message])
            else:
                # Some messages are funny and the lines get split (see lines
                # 363 in the file). Add any loner lines to the message of the previous line
                data_dump[-1][-1] += line
                continue

    return pd.DataFrame(data = data_dump, columns=HEADERS)

file = "WhatsApp Chat with The Squad.txt" 
df = build_dataframe(file)
print df
plots.author_counts(df)

