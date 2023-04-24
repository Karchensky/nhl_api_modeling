from datetime import datetime

# Define a function to convert the time string to seconds
def time_text_to_seconds(time_str):
    if time_str is None:
        return None
    if not time_str:
        return None
    dt = datetime.strptime(time_str, '%M:%S')
    return (dt.minute * 60 + dt.second)