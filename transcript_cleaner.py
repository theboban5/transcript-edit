import re

def read_transcript(file_path):
    with open(file_path, 'r') as file:
        transcript = file.read()
    return transcript

def clean_zoom_transcript(transcript):
    # Split the transcript into lines
    lines = transcript.split('\n')
    
    # Remove empty lines, lines that do not contain text, and lines with timestamps
    cleaned_lines = [line for line in lines if line.strip() and '-->' not in line and not line.strip().isdigit()]
    
    # Join cleaned lines with proper formatting
    cleaned_transcript = '\n'.join(cleaned_lines)
    return cleaned_transcript

def remove_names_from_transcript(transcript, names_to_remove):
    # Split the transcript into lines
    lines = transcript.split('\n')
    
    # Initialize an empty list to store lines without the names
    no_name_lines = []

    for line in lines:
        # Check if the line starts with any of the names to remove
        if any(line.startswith(name + ":") for name in names_to_remove):
            # Remove the name and colon from the line
            no_name_line = re.sub(r'^[A-Za-z\s]+:\s*', '', line)
            no_name_lines.append(no_name_line)
        else:
            no_name_lines.append(line)

    clean_no_name = '\n'.join(no_name_lines)
    return clean_no_name

# Path to the transcript file
file_path = 'data/transcript.txt'

transcript = read_transcript(file_path)

cleaned_transcript = clean_zoom_transcript(transcript)

# Names to be removed from the transcript
names_to_remove = ['NAME']  # specify the name(s) you want to remove

clean_no_name = remove_names_from_transcript(cleaned_transcript, names_to_remove)

print("Transcript without Specified Names:")
print(clean_no_name)









