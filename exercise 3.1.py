import streamlit as st

st.title("Name and Sum App")

# Name input
name = st.text_input("Enter your name:")

# Number inputs
num1 = st.number_input("Enter first number:", value=0)
num2 = st.number_input("Enter second number:", value=0)

# Button to calculate and display
if st.button("Submit"):
    if name:
        st.write(f"Hello, {name}!")
    else:
        st.write("Hello, stranger!")
    
    st.write(f"The sum is {num1 + num2}.")