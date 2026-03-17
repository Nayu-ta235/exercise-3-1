import streamlit as st

st.title("Welcome GUI App")
st.text("This is my first Graphical Interface :)")

name = st.text_input("Enter your name:")

num1 = st.number_input("Enter first number:", value=0)
num2 = st.number_input("Enter second number:", value=0)

show_greeting = st.checkbox("Show Greeting")

if st.button("Submit"):

    if name:
        st.write(f"Hello, {name}!")
    else:
        st.write("Hello, stranger!")
    
    st.write(f"The sum of two number is {num1 + num2}.")
    

    if show_greeting:
        st.write("Have a nice day!")