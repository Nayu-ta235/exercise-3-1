import streamlit as st

# Question 1
st.title("Welcome GUI App")
st.write("This is my first graphical interface")

# Question 2
name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}!")

# Question 3
if st.button("Click Me"):
    st.write("Button clicked!")

# Question 4
st.subheader("Add Two Numbers")
num1 = st.number_input("Number 1", value=0)
num2 = st.number_input("Number 2", value=0)
if st.button("Add Numbers"):
    st.write(f"Sum: {num1 + num2}")

# Question 5
show_greeting = st.checkbox("Show Greeting")
if show_greeting:
    st.write("Have a nice day!")

# Question 6 - Mini combined app
st.markdown("---")
st.subheader("Mini Combined App")

# Inputs
name_combined = st.text_input("Enter your name (combined app):")
num1_combined = st.number_input("Enter first number (combined app):", value=0)
num2_combined = st.number_input("Enter second number (combined app):", value=0)
show_greeting_combined = st.checkbox("Show Greeting (combined app)")

if st.button("Submit"):
    if name_combined:
        st.write(f"Hello, {name_combined}!")
    else:
        st.write("Hello, stranger!")
    
    st.write(f"The sum of your numbers is {num1_combined + num2_combined}.")
    
    if show_greeting_combined:
        st.write("Have a nice day!")