#Naive Bayes Classifier 
#Vishnu Karnam A01962610
import glob
import re
import math
from collections import OrderedDict
def TrainingData(path,x):
    WordsDict={}
    filecount=0
    for filename in path:
        if(filecount<=x):
            fref=open(filename,'r')
            tokens=fref.read().split()
            cleandata=[]
            for words in tokens:
                temp=re.sub("[\W_]+", "", words) #Cleaning Data
                if(len(temp)>0):
                    cleandata.append(temp.lower()) #Making case insensitive and to lower case
            cleandata.sort()
            for words in cleandata:
                if(WordsDict.has_key(words)==1):
                    WordsDict[words]+=1
                else:
                    WordsDict[words]=1
            filecount+=1
        else:
            break;
    return WordsDict
def TestingData(path):
    TestData={}
    for filename in path:
        fref=open(filename,'r')
        tokens=fref.read().split()
        cleandata=[]
        for words in tokens:
                temp=re.sub("[\W_]+", "", words)
                if(len(temp)>0):
                    cleandata.append(temp.lower())
        cleandata.sort()
        for words in cleandata:
            if(TestData.has_key(words)==1):
                TestData[words]+=1
            else:
                TestData[words]=1
    return TestData    
if __name__=="__main__":
    PosDir="C:/txt_sentoken/pos/*.txt" #Change Dicrectory Accordingly
    NegDir="C:/txt_sentoken/neg/*.txt" #Change Directory Accordingly
    PosDict=TrainingData(glob.glob(PosDir),700) #Positive Dictionary
    NegDict=TrainingData(glob.glob(NegDir),700) #Negative Dictionary
    Total_Words_PosDict=0
    Total_Words_NegDict=0
for key,value in PosDict.items():
    Total_Words_PosDict+=value
for key,value in NegDict.items():
    Total_Words_NegDict+=value
Total_DistWords_Dict={}  #Dictionary that has unique words by combining positive and negative Dictionary
for key,value in PosDict.items():
    Total_DistWords_Dict[key]=value
for key,value in NegDict.items():
    if(Total_DistWords_Dict.has_key(key)==1):
        continue
    else:
        Total_DistWords_Dict[key]=value
a=0;
b=0;
c=0;
d=0;
for i in range(700,1000):
    Test_Pos_Dir="C:/txt_sentoken/pos/cv"+str(i)+"_*.txt" #Change Directory Accordingly
    testposData=TestingData(glob.glob(Test_Pos_Dir))
    prior_pos_prob=0.5
    prior_neg_prob=0.5
    pos_value=1
    neg_value=1
    post_pos_prob=math.log10(prior_pos_prob)
    post_neg_prob=math.log10(prior_neg_prob)
    for key,value in testposData.items():
        if PosDict.has_key(key):
            pos_value+=PosDict[key] #if word in Dictionary value +1
        else:
            pos_value=1 #if word not in Dictionary value is 1
        post_pos_prob+=value*(math.log10(pos_value)-math.log10(Total_Words_PosDict+len(Total_DistWords_Dict))) # Taking log10 as it is monotonically increasing
        if NegDict.has_key(key):
            neg_value+=NegDict[key]
        else:
            neg_value=1
        post_neg_prob+=value*(math.log10(neg_value)-math.log10(Total_Words_NegDict+len(Total_DistWords_Dict))) #Total words in negative Dictionary + Distinct Words in both Dictionaries
    if(post_pos_prob>post_neg_prob):
        a=a+1
        print"File "+ Test_Pos_Dir +"is Positive Review"
    else:
        b=b+1
        print "File"+ Test_Pos_Dir+"is a Negative Review"
    print a,b
for i in range(700,1000):
    Test_Neg_Dir="C:/txt_sentoken/neg/cv"+str(i)+"_*.txt" #change directory Accordingly
    testNegData=TestingData(glob.glob(Test_Neg_Dir))
    prior_pos_prob=0.5 #prior probabilities
    prior_neg_prob=0.5 #prior probabilities
    pos_value=1
    neg_value=1
    post_pos_prob=math.log10(prior_pos_prob)
    post_neg_prob=math.log10(prior_neg_prob)
    for key,value in testNegData.items():
        if(NegDict.has_key(key)):
            neg_value+=NegDict[key]
        else:
            neg_value=1
        post_neg_prob+=value*(math.log10(neg_value)-math.log10(Total_Words_NegDict + len(Total_DistWords_Dict)))
        if(PosDict.has_key(key)):
            pos_value+=PosDict[key]
        else:
            pos_value=1
        post_pos_prob+=value*(math.log10(pos_value)-math.log10(Total_Words_PosDict + len(Total_DistWords_Dict)))
    if(post_pos_prob>post_neg_prob):
        c+=1
        print "File"+Test_Neg_Dir+" is Positive Review"
    else:
        d+=1
        print "File"+Test_Neg_Dir+" is Negative Review"
    print c,d
print "Final Values of a,b,c,d are",a,b,c,d
Accuracy=float(a+d)/(a+b+c+d)
print "Accuracy is ", Accuracy
sort_negDict=OrderedDict(sorted(NegDict.items(),key=lambda t: t[1]))
sort_posDict=OrderedDict(sorted(PosDict.items(),key=lambda t: t[1]))
print "Top Ten in Positive Dictionary"
itemcount=0
for key,value in sort_posDict.items():
    if(itemcount>len(sort_posDict)-11):
        print key+" Conditional probability log10 is"+str(math.log10(value+1)-math.log10(Total_Words_PosDict + len(Total_DistWords_Dict)))
        itemcount+=1
    else:
        itemcount+=1
print "Top Ten in Negative Dictionary"
itemcount=0
for key,value in sort_negDict.items():
    if(itemcount>len(sort_negDict)-11):
        print key+" Conditional Probability log10 is"+str(math.log10(value+1)-math.log10(Total_Words_NegDict + len(Total_DistWords_Dict)))
        itemcount+=1
    else:
        itemcount+=1
    
    
        
        
            
        
    
    
    

    
    