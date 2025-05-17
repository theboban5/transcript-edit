# transcript-edit

a simple tool to reformat zoom transcripts -- removing the time stamps, sentence number and names of 1 or more speakers

For example
    original transcript: 

        3
        00:00:30.160 --> 00:00:37.329
        Speaker: This is a sample sentence. 

        4
        00:00:37.330 --> 00:00:37.830
        Listener: Sure, sure. 

    after running (with 'Speaker' as name to be removed): 
        
        This is a sample sentence. 

        Listener: Sure, sure. 

___________________________________________________

to run: 
    in transcript_cleaner.py -- update name(s) to be removed (line 46)
    in transcript.txt -- paste zoom transcript

    (in terminal) 
    source venv/bin/activate 
    python transcript_cleaner.py

