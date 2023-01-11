import streamlit as st
st.write("# salary prediction")
#write() inbuilt function of streamlit
#to accept data from user (numeric type data)
#numeric_input() inbuilt function which float type data from user 
#text_input() inbuilt to accept string type data
exp=st.number_input("enter year of experience : - ") # float type 
#if inter type
#age=st.number_input("enter age :- ",format='%d',value=0)
import numpy as np
import pickle
#to open exiting file in read mode
file1=open("model.pkl","rb")#rb means read binary

#to read data from file1, use load() inbuilt method of pickle
model=pickle.load(file1) #model is user defined object

#to open exiting file in read mode
file2=open("scale.pkl","rb")#rb means read binary

#to read data from file1, use load() inbuilt method of pickle
scale=pickle.load(file2) #model is user defined object

if st.button("predict salary"):#button() inbuilt of streamlit
    #convert variable exp into 2D numpy arra
    exp=np.array([[exp]])
    #st.write(exp.ndim,type(exp))
    #apply scaling on input exp
    exp=scale.transform(exp)
    
    Y_pred=model.predict(exp)[0].round(2) #use [0] to remove matix 
    st.write("predicted salary : - ",Y_pred)