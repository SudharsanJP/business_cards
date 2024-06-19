#)modules
import pytesseract
from PIL import Image
import cv2
import pandas as pd
import streamlit as st

#)title
st.title(':orange[Extracting text from image - Bcardz]')

#) tesseract app path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img1 = Image.open(r"D:\Sudharsan\Guvi_Data science\DS101_Sudharsan\Mainboot camp\capstone project\business_cardz\1.png")
#img1.show()

#) 21. checkbox with text
st.markdown("\n#### :green[1. Bcard Images]\n")
if (st.checkbox("image 1")):
    #)displaying the image1
    st.markdown("\n#### :red[1.1 image 1:]\n")
    image = Image.open("1.png")
    st.image(image, caption='Bcard 1')
    
    #) text from img1
    st.markdown("\n#### :red[1.2 text from image 1:]\n")
    st.code(pytesseract.image_to_string(img1))

#) converting the information into dictionary format and dataframe
text_dict1 = [{'name':'Selva','designation':'DATA MANAGER',"phone_num1":"+123-456-7890",
              "phone_num2":"+123-456-7891","mail":"hello@XYZ1.com", 'website':"www.XYZ1.com",'local_address':"9 123 ABC St",
             "city":"Chennai","state":"TamilNadu",'pincode':600113}]
df1 = pd.DataFrame(text_dict1)


#) img2
img2 = Image.open(r"D:\Sudharsan\Guvi_Data science\DS101_Sudharsan\Mainboot camp\capstone project\business_cardz\2.png")
#img2.show()


#) 21. checkbox with text
if (st.checkbox("image 2")):
    #)displaying the image2
    st.markdown("\n#### :red[2.1 image 2:]\n")
    image = Image.open("2.png")
    st.image(image, caption='Bcard 2')
    
    #) text from img2
    st.markdown("\n#### :red[2.2 text from image 2:]\n")
    st.code(pytesseract.image_to_string(img2))


text_dict2 = [{'name':'Amit kumar','designation':'CEO & FOUNDER',"phone_num1":"123-456-7569",
              "mail":"Bj hello@global.com", 'website':"www.global.com",'local_address':"123 global St",
             "city":"Erode","state":"TamilNadu",'pincode':600115,"company_name":"GLOBAL INSURANCE"}]
df2 = pd.DataFrame(text_dict2)


#) img3
img3 = Image.open(r"D:\Sudharsan\Guvi_Data science\DS101_Sudharsan\Mainboot camp\capstone project\business_cardz\3.png")
#img3.show()

#) 21. checkbox with text
if (st.checkbox("image 3")):
    #)displaying the image2
    st.markdown("\n#### :red[3.1 image 3:]\n")
    image = Image.open("3.png")
    st.image(image, caption='Bcard 3')
    
    #) text from img3
    st.markdown("\n#### :red[3.2 text from image 3:]\n")
    st.code(pytesseract.image_to_string(img3))



text_dict3 = [{'name':'KARTHICK','designation':'General Manager',"phone_num1":" +123-456-7890",
              "mail":'E3 _hello@Borcelle.com', 'website':'www.Borcelle.com','local_address':"123 ABC St",
             "city":" Salem","state":"TamilNadu",'pincode':6004513}]

df3 = pd.DataFrame(text_dict3)


#) img4
img4 = Image.open(r"D:\Sudharsan\Guvi_Data science\DS101_Sudharsan\Mainboot camp\capstone project\business_cardz\4.png")
#img4.show()

#) 21. checkbox with text
if (st.checkbox("image 4")):
    #)displaying the image2
    st.markdown("\n#### :red[1.4(a) image 4:]\n")
    image = Image.open("4.png")
    st.image(image, caption='Bcard 4')
    
    #) text from img4
    st.markdown("\n#### :red[1.4(b) text from image 4:]\n")
    st.code(pytesseract.image_to_string(img4))

text_dict4 = [{'name':'REVANTH',"phone_num1":"+91-456-1234",
              "mail":'hello@CHRISTMAS.com', 'website':'www.CHRISTMAS.com','local_address':"123 ABC St",
             "city":" HYDRABAD","state":"TamilNadu",'pincode':600001}]

df4 = pd.DataFrame(text_dict4)


#) img5
img5 = Image.open(r"D:\Sudharsan\Guvi_Data science\DS101_Sudharsan\Mainboot camp\capstone project\business_cardz\5.png")
#img5.show()

#) 21. checkbox with text
if (st.checkbox("image 5")):
    #)displaying the image2
    st.markdown("\n#### :red[1.5(a) image 5:]\n")
    image = Image.open("5.png")
    st.image(image, caption='Bcard 5')
    
    #) text from img2
    st.markdown("\n#### :red[1.5(b) text from image 5:]\n")
    st.code(pytesseract.image_to_string(img5))

text_dict5 = [{'name':'SANTHOSH',"designation":"Technical Manager","phone_num1":"+123-456-1234",
              "mail":'hello@Sun.com', 'website':'www.Sun.com','local_address':"19 | 123 ABC St",
             "city":"Tirupur","state":"TamilNadu",'pincode':641603}]

df5 = pd.DataFrame(text_dict5)


st.markdown("\n#### :blue[2. text information dataframe:]\n")
if (st.button(':red[click here]')):
    #)concatenation of dataframes(1-4)
    df = pd.concat([df1, df2, df3,df4,df5], axis=0, ignore_index=True)

    # Sample data
    data = df.head()

    # Display the table with highlighting
    st.dataframe(data.style.applymap(lambda x: 'color:red'))


