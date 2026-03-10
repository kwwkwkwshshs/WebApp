import streamlit as st
import datetime


def home():
    st.title("Tara Kape Tayo ☕")
    st.header("Welcome to our Cozy Cafe!")
    st.image("Tara Kape Tayo.png")
    st.write("""
    Tara Kape Tayo is your cozy digital café — a place where tradition meets technology.
    Inspired by the Filipino phrase 'Let's have coffee', our café celebrates the joy of sharing a cup.
   
    What We Offer
    - Coffee lovers can explore our natural blends.
    - Non-coffee drinkers can enjoy matcha, chocolate, or fruity milk drinks.
    - Pastry pairings are available to complete your café experience.
   
    How to Navigate
    Use the sidebar to:
    - Home → Discover our café's story.
    - Menu → Choose coffee, non-coffee, and pastries.
    - Order → Place your personalized order.
    - About → Learn more about the app.
    """)
    st.metric("Cups served today", 80, delta="+15")


def menu():
    st.title("Kape Menu")
    st.write("Enjoy our specialties")


    drinktype = st.radio("Would you like coffee or non-coffee?", ["Coffee", "Non-Coffee"])


    if drinktype == "Coffee":
        coffee = st.radio("Choose your coffee drink:",
                          ["Espresso", "Americano", "Latte", "Spanish Latte",
                           "Caramel", "Seasalt Caramel", "Mocha", "Tiramisu"])
        size = st.selectbox("Size:", ["Small", "Medium", "Large"])
        extras = st.multiselect("Extras:", ["Oat Milk", "Soy Milk", "Whipped Cream", "Caramel Syrup", "None"])
        sugar = st.slider("Sugar level (%)", 0, 100, 50)


        want_pastry = st.checkbox("Would you like to add a pastry?")
        if want_pastry:
            pastry = st.selectbox("Choose your pastry:", ["Croffle", "Muffin", "Bagel", "Brownie"])
            warm = st.checkbox("Warm it up?")
           
            if warm:
                roast = st.select_slider("Preferred roast level", options=["Light", "Medium", "Dark"])


        if st.button("Add to Tray"):
            if want_pastry:
                if warm:
                    st.success(f"Added {size} {coffee} with {extras}, sugar {sugar}%, plus {pastry} ({roast} roast)")
                else:
                    st.success(f"Added {size} {coffee} with {extras}, sugar {sugar}%, plus {pastry}")
            else:
                st.success(f"Added {size} {coffee} with {extras}, sugar {sugar}%")


    else:
        non_coffee = st.radio("Choose your non-coffee drink:", ["Matcha Latte", "Chocolate", "Oreo Milk", "Strawberry Milk"])
        size = st.selectbox("Size:", ["Small", "Medium", "Large"])
        extras = st.multiselect("Extras:", ["Oat Milk", "Soy Milk", "Whipped Cream", "None"])
        ice_level = st.slider("Ice level (%)", 0, 100, 50)


        want_pastry = st.checkbox("Would you like to add a pastry?")
        if want_pastry:
            pastry = st.selectbox("Choose your pastry:", ["Croffle", "Muffin", "Bagel", "Brownie"])
            warm = st.checkbox("Warm it up?")
           
            if warm:
                roast = st.select_slider("Preferred roast level", options=["Light", "Medium", "Dark"])


        if st.button("Add Non-Coffee to Tray"):
            if want_pastry:
                if warm:
                    st.success(f"Added {size} {non_coffee} with {extras}, ice {ice_level}%, plus {pastry} ({roast} roast)")
                else:
                    st.success(f"Added {size} {non_coffee} with {extras}, ice {ice_level}%, plus {pastry}")
            else:
                st.success(f"Added {size} {non_coffee} with {extras}, ice {ice_level}%")


def order():
    st.title("Place Your Order")


    with st.form("order_form"):
        name = st.text_input("Your Name")
        pickup_date = st.date_input("Pickup date")
        pickup_time = st.time_input("Pickup time")
        drinks = st.number_input("Number of drinks", min_value=1, max_value=100, value=1)
        notes = st.text_area("Special Instructions")


        tip = st.radio("Would you like to leave a tip", ["10%", "15%", "20%", "No Tip"])
       
        submitted = st.form_submit_button("Confirm Order")


    if submitted:
        st.success(f"Order confirmed for {name} on {pickup_date} at {pickup_time} with {tip} tip!")
        st.progress(80)
        st.download_button("Download Receipt", f"Order for {name}", file_name="receipt.txt")
        st.camera_input("Snap a photo with your drink!")


def about():
    st.title("About Tara Kape Tayo")
    st.write("""
    ### What the app does
    This app is a digital cafe experience using Streamlit UI components.
    As you explore the website, you can browse the menu (Coffee or Non-Coffee), place an order, and learn about the app.


    ### Target Users
    - Students that want to learn how to use Streamlit
    - Individuals exploring UI components of Streamlit
    - Coffee and non-coffee lovers who want to experience digital demos of a cafe


    ### Inputs Collected
    - Drink Selections (Coffee and Non-Coffee) and Pastry
    - User details (name, pickup date and time, notes, number of drinks and tip)
    - Various interactive inputs (sliders, checkboxes, radios, and others)


    ### Outputs Shown
    - Order Confirmations
    - Interactive UI Feedback
    """)


st.sidebar.title("Cafe Navigation")
page = st.sidebar.radio("Choose a section", ["Home", "Menu", "Order", "About"])


if page == "Home":
    home()
elif page == "Menu":
    menu()
elif page == "Order":
    order()
elif page == "About":
    about()

