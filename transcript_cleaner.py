import re

def read_transcript(file_path):
    with open(file_path, 'r') as file:
        transcript = file.read()
    return transcript

def clean_zoom_transcript(transcript):
    # Split the transcript into lines
    lines = transcript.split('\n')
    
    # Pattern to match lines that start with a name (a letter followed by a colon)
    pattern = re.compile(r'^[A-Za-z]+:.*')
    
    cleaned_lines = []

    for line in lines:
        match = pattern.match(line)
        if match:
            cleaned_lines.append(line.strip())

    # Join cleaned lines with proper formatting
    cleaned_transcript = '\n\n'.join(cleaned_lines)
    return cleaned_transcript

def remove_names_from_transcript(transcript, names_to_remove):
    lines = transcript.split('\n\n')
    no_name_lines = []
    current_paragraph = []

    for line in lines:
        # Remove the first word and colon from lines that start with a specified name
        if any(line.startswith(name + ":") for name in names_to_remove):
            no_name_line = re.sub(r'^[A-Za-z]+:\s*', '', line)
            current_paragraph.append(no_name_line)
        else:
            if current_paragraph:
                no_name_lines.append(' '.join(current_paragraph))
                current_paragraph = []
            no_name_lines.append(line)

    # Append any remaining text
    if current_paragraph:
        no_name_lines.append(' '.join(current_paragraph))

    clean_no_name = '\n\n'.join(no_name_lines)
    return clean_no_name

# Path to the transcript file
file_path = 'data/transcript.txt'

# Read the transcript file
transcript = read_transcript(file_path)

# Clean the transcript
cleaned_transcript = clean_zoom_transcript(transcript)

# Print the cleaned transcript (basically don't need this anymore - keep commented out)
# print("Cleaned Transcript:")
# print(cleaned_transcript)

# Names to be removed from the transcript
names_to_remove = ['Elli']  #  specify the names you want to remove

# Remove names from the cleaned transcript
clean_no_name = remove_names_from_transcript(cleaned_transcript, names_to_remove)

print("Transcript without Specified Names:")
print(clean_no_name)








