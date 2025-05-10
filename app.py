import streamlit as st

# Page setup
st.set_page_config(page_title='🎄Growth Mindset', layout='centered')

# Sidebar: Customization
st.sidebar.markdown('<p class="sidebar-title">🦅 Abdulrehman Shaikh 🦅/p>', unsafe_allow_html=True)
st.sidebar.markdown('<p class="sidebar-subheader">Welcome to my Streamlit app!</p>', unsafe_allow_html=True)

# 🎨 Color picker for custom highlight
highlight_color = st.sidebar.color_picker("Pick your highlight color", "#FFA500")

# Sidebar Inputs
st.sidebar.markdown('<p class="sidebar-title">🔰 Learning Hub 🔰</p>', unsafe_allow_html=True)
st.sidebar.markdown('<h1 class="sidebar-title">🌲 Growth Mindset Challenge 🌲</h1>', unsafe_allow_html=True)

st.sidebar.write("What's your challenge today?")
users_input = st.sidebar.text_input("Describe a challenge you're facing:")
if users_input:
    st.sidebar.success(f'You are facing: {users_input}. Keep pushing forward to your goal 💪')
else:
    st.sidebar.warning('Tell us about your challenge to get started!')

st.sidebar.write('Reflect on your learning')
users_area = st.sidebar.text_area("Describe your reflection here!")
if users_area:
    st.sidebar.success(f'💫 Great insight in your reflection: {users_area}')
else:
    st.sidebar.info('Reflecting on past experiences helps you grow! Share your thoughts.')

st.sidebar.write('Celebrate your wins')
achieve = st.sidebar.text_input("Share something you've recently accomplished:")
if achieve:
    st.sidebar.success(f'Amazing! You achieved: {achieve} 🏆')
else:
    st.sidebar.warning('Big or small — every achievement counts! Share one now 🥳')

# Apply CSS with dynamic color
st.markdown(
    f"""
    <style>
    .main-title {{
        font-size: 50px;
        color: {highlight_color};
        text-align: center;
        font-weight: bold;
    }}
    .header-text {{
        font-size: 30px;
        color: #6B5B95;
        font-weight: bold;
    }}
    .subheader-text {{
        font-size: 24px;
        color: {highlight_color};
        font-weight: bold;
    }}
    .footer-text {{
        font-size: 16px;
        color: #A52A2A;
        font-weight: bold;
        text-align: center;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Main content
st.markdown('<h1 class="main-title">🌴 GROWTH MINDSET CHALLENGE!</h1>', unsafe_allow_html=True)
st.write("A growth mindset is the belief that your abilities and intelligence can be developed through **hard work, perseverance, and learning from your mistakes**. ✈️")

st.markdown('<h2 class="header-text">💫💫💫 Why Adopt A Growth Mindset? 💫💫💫</h2>', unsafe_allow_html=True)

st.markdown('<h3 class="subheader-text">🔥 Embrace Challenges</h3>', unsafe_allow_html=True)
st.write("View obstacles as opportunities to learn rather than setbacks.")

st.markdown('<h3 class="subheader-text">❄️ Learn from Mistakes</h3>', unsafe_allow_html=True)
st.write("Making mistakes is a natural part of learning.")

st.markdown('<h3 class="subheader-text">💪 Persist Through Difficulties</h3>', unsafe_allow_html=True)
st.write("Stay determined, even when things get tough.")

st.markdown('<h3 class="subheader-text">🥳 Celebrate Effort</h3>', unsafe_allow_html=True)
st.write("Recognize and reward the effort you put into learning.")

st.markdown('<h3 class="subheader-text">🔎 Keep an Open Mind</h3>', unsafe_allow_html=True)
st.write("Stay curious and be willing to adapt.")

# Footer
st.markdown("---")
st.markdown('<h4 class="footer-text">Remember: Your journey in education is not just about proving your intelligence — it\'s about developing it! 🌟</h4>', unsafe_allow_html=True)
