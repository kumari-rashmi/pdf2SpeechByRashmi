pdf2SpeechByRashmi

Description : Reading textbook can be difficult sometimes , use this utility to convert the pdf text to a mp3 format to be heard as audio.

Git Repo : https://github.com/kumari-rashmi/pdf2SpeechByRashmi.git

Steps to run it locally :

1. Clone the repo locally :
 
 ```
    git clone https://github.com/kumari-rashmi/pdf2SpeechByRashmi.git
 ```
 
2. Include any PDF file in your local project directory , the hierarchy of your folder would look like below :

```
  pdf2SpeechByRashmi
    |
    |____ .gitignore
    |
    |____ sample.txt
    |
    |____ README.md
    |
    |____ t2s.py
    |
    |____ t2s4rmfile.py
    |
    |____ t2spdf.py
    |
    |____ (your pdf file)
```

3. Open the python file t2spdf.py and change line number 54 to your pdf file name you choose to read 

4. Line number has the start index of page number and end index of page number we want to read in audio format
```
    49 startPage = 14
    50 endPage = 18
```

5. After modifing these flags , hit the the run button in your code editor  ( ensure python is installed ) or alternatively
open a Terminal  perform below steps:

```
    cd pdf2SpeechByRashmi
    python t2spdf.py
```


