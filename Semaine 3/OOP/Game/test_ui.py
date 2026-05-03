import streamlit as st

# Configure sidebar
with st.sidebar:
    # Logo at the top
    st.image(
        "logo.png",
        width=200,
    )
    
    # App title and tagline
    st.markdown("""
        <h2 style='text-align: center; color: #667eea; margin: 0;'>
            LOGO
        </h2>
        <p style='text-align: center; color: #888; font-size: 14px;'>
            TESTING LOGO
        </p>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    # Navigation or filters below
    st.subheader("📊 Quick Stats")
    st.metric("Active Users", "1,234", "+12%")
    st.metric("Revenue", "$45.6K", "+8%")
