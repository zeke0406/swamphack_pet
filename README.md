## Desktop Buddy
### Inspiration
Ever since the pandemic, people’s lives have been significantly impacted in many different ways. Especially people's distance from friends and families. It has never been more important for us to focus on people's mental wellness because all people see now are computer screens. They wake up to computer screens,  and all interactions are done online and people barely get a chance to go outside and hang out with friends. So we are bringing everyone a virtual desktop friend with our program. When the user runs this program, the program will transcribe users’ speech to text in real time. When a keyword is detected, indicating that the user is feeling depressed, down, or lonely, a little desktop friend, which will act as an emotional support, will pop out on the user’s desktop. 

### What it does
When the program detects a keyword from the keyword list, which contains the following: lonely, miss you, sad, depressed, friend, start, buddy, cry, bored, a virtual friend will pop up on the desktop

### How we built it
We used Visual Studio Code to program with Python, PyQt5, and Google cloud's speech to text api, and Paint Tool SAI to create the virtual friend)


### Challenges we ran into
- Not familiar with Python and PyQt5
- First time utilizing an API
- Unable to install PyQt5 correctly
- Different coding background among teammates: specific timeframe limited us from combinning our functions on character dynamics coded in Java with other functions coded in Python

### Accomplishments that we're proud of
- Implementing the speech recognition feature in our program
- Successfully installed PYQT5 

### Usage
- Install Python 3.9.1
- Install the dependencies with the command
```bash
pip install PyQt5
```
- Run the following command line
```bash
export GOOGLE_APPLICATION_CREDENTIALS="[PATH]"
```
- Run the program with following command
```bash
python DesktopPet.py
```
The desktop buddy will come out when they notice you are having a bad time or just simply need someone from what you say

### What's next for DesktopBuddy
- Allow the users to have conversations with the friend
- Allow the users to have more interactions with friends other than dragging

### Sources
- shimiji (e.g., http://pepeswap.com)
- https://mp.weixin.qq.com/s/4kOzdRXmrxzR88QcYYSFvQ
