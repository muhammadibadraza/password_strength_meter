import streamlit as st
import re
import random

st.set_page_config(page_title="🔐Password Strength Checker", layout="wide")
st.title("🔐Password Strength Checker")
st.subheader("Checks your password strength and give suggestions to improve!!")

com_pas = ['password','Password','PASSWORD123','password125','password123','qwerty','12345678','abcd1234','abc123','12341234']

def check_password_strength(password):
    score = 0
    
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        st.error("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        st.error("❌ Include both uppercase and lowercase letters.")
        
    vowels = "aeiou"
    new_pass = "".join(char.upper() if char in vowels else char for char in password)
    print(new_pass)    
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        st.error("❌ Add at least one number (0-9).")
    index = 3
        
    pw = new_pass[:index]+"9"+new_pass[index+1:]
        # st.write(f"hint:{pw}")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        st.error("❌ Include at least one special character (!@#$%^&*).")
    special = ['@','!','#','$','&','?','%']
    num = [1,2,4,5]
    in_num = random.choice(num)
    new_special = random.choice(special)               
    sp_pass = pw[:in_num]+new_special+pw[in_num+1:]
        # st.write(f"Hint: {sp_pass}")
    
    # Strength Rating
    if score == 4:
        st.write("✅ Strong Password!")
    elif score == 3:
        st.write("⚠️ Moderate Password - Consider adding more security features.")
        st.write(f"Hint💡👉: {sp_pass}")
    else:
        st.markdown("**❌ Weak Password - Improve it using the suggestions above.**")
        st.markdown(f"**💡Hint👉: {sp_pass}**")       
        

# Get user input
password = st.text_input("Enter your Password: ", type="password")

# Feedback system
# if password ==  "password123":
#     st.error("Enter a Password")
if password in com_pas:
    st.error("Please change the Password, your Password is too common.")
else:
# elif password != "":
   check_password_strength(password)
