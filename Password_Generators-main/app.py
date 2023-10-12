import string
import random
import streamlit as st

def password(s_len):
   s1= string.ascii_lowercase
   
    #https://docs.python.org/3/library/string.html 
   
   s2=string.ascii_uppercase
   s3=string.digits
   s4=string.hexdigits
   s5=string.octdigits
   s6=string.punctuation
   s7=string.printable

    # define a length

    #s_len=int(input("enter a number"))

   s=[]
   s.extend(list(s1))
   s.extend(list(s2))
   s.extend(list(s3))
   s.extend(list(s4))
   s.extend(list(s5))
   s.extend(list(s6))
   s.extend(list(s7))
   random.shuffle(s)
   a="".join(s[0:s_len])

   return a



def main():

    html_temp = """
   <div class="" style="background-color:blue;" >
   <div class="clearfix">           
   <div class="col-md-12">
   <center><p style="font-size:40px;color:white;margin-top:10px;">Password Generator </p></center> 

   </div>
   """
    st.markdown(html_temp,unsafe_allow_html=True)
    
    st.header("Choose the length of password")

    #s_len = 10 #@param {type:"slider", min:10, max:100, step:1}
    s_len = st.slider(' ', 0, 130, 15)





    if st.button("Get password"):
          result=password(s_len)
          #st.image(result)
          st.write("Your Password is \n ")
          st.write( result)
    if st.button("About"):
          st.subheader("Developed by Ishu kumar")
          st.subheader(" Department of Computer Engineering")




if __name__=='__main__':
  main()