import streamlit as st

def convert_units(value, unit_from, unit_to):
    conversions = {
        "meters_kilometers": 0.001,
        "kilometers_meters": 1000,
        "grams_kilograms": 0.001,
        "kilograms_grams": 1000,
        "celsius_fahrenheit": lambda c: (c * 9/5) + 32,
        "fahrenheit_celsius": lambda f: (f - 32) * 5/9
    }
    
    key = f"{unit_from}_{unit_to}"
    
    if key in conversions:
        conversion = conversions[key]
        return conversion(value) if callable(conversion) else value * conversion
    else:
        return "Conversion not supported"

# Streamlit UI
st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")

st.markdown("""
    <h2 style='text-align: center; color: #4CAF50;'>🔄 Unit Converter</h2>
    <p style='text-align: center;'>Convert length, weight, and temperature units easily!</p>
""", unsafe_allow_html=True)

st.divider()

col1, col2 = st.columns([1, 1])

with col1:
    value = st.number_input("Enter the value:", min_value=0.0, step=0.1, format="%.2f")
    unit_from = st.selectbox("Convert from:", ["meters", "kilometers", "grams", "kilograms", "celsius", "fahrenheit"])

with col2:
    unit_to = st.selectbox("Convert to:", ["meters", "kilometers", "grams", "kilograms", "celsius", "fahrenheit"])
    result = convert_units(value, unit_from, unit_to)

st.divider()

st.markdown(f"""
    <h3 style='text-align: center; color: #2196F3;'>Result: <span style='color: #FF5722;'>{result}</span></h3>
""", unsafe_allow_html=True)

# Refresh Button
if st.button("🔄 Refresh"):
    st.experimental_rerun()
