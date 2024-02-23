# nomination_pytk {#mainpage}
## Application Overview
This app can nominate people random that you input to nominate.

## Requirement definition
### ①Write nominate people on A column in csv.  
![draft_csv](doc/draft/draft_csv.jpg)

### ②Create a GUI similar to the following:  
![draft_GUI](doc/draft/draft_GUI.jpg)  
・Click the "Nominate" button to nominate.  
・There are no duplicate nominations.  
・Click the "Reset" button to reset to a state where no one is named.  

## How to use
1. Clone by specifying a branch.  
git clone -b {branch name} {URL of the copied repository}  
2. Open "{cloned folder}/nominate_list.csv".  
Write nominate people on A column in csv.  
3. Execute "{cloned folder}/main.py".  
python main.py or  
python3 main.py  
4. After the app window opens,  
one person is nominated by click the nomination button.  
5. When everyone has been nominated, the "終了" message appears.  
6. If you want to reset, click the reset button and go back to step 4.  

## Author
yukinagata3184