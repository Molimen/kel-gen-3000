import streamlit as st
import random
from math import floor
import base64
from streamlit_extras.stylable_container import stylable_container
import requests

# future TO-DO
# None!

# TO-DO
# remake about and icon rework


# INIT START!

def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def randomize(kelompok_total, person, member):
    if (kelompok_total > 0 and member > 0) or (kelompok_total <= 0 and member <= 0): raise TypeError("Invalid input!")
    if member > len(person): raise TypeError("More member than data that available")

    if member > 0: kelompok_total = floor(len(person)/member)

    if kelompok_total > len(person): raise TypeError("Are you trying to make more Kelompok than the amount of person?")
    if kelompok_total <= 0: raise TypeError("There is NO kelompok less than 1")

    total_person = len(person)
    kelompok = list()
    complete = 0

    # randomizer
    for i in range(kelompok_total):
        selected = list()
        counter = 0
        for j in range(floor(total_person/kelompok_total)):
            if len(person) <= 0:
                complete = 1
                break

            selected.append(random.choice(person))
            person.remove(selected[counter])

            counter += 1
        kelompok.append(selected)
        if complete: break

    total_person = len(person)
    selected_kel_stop = list()

    # for odd amount of kelompok / person
    for i in range(total_person):
        while 1:
            selected_kel = random.randint(0,kelompok_total-1)
            if selected_kel not in selected_kel_stop:
                break
        
        selected = random.choice(person)
        person.remove(selected)

        kelompok[selected_kel] += [selected]
        selected_kel_stop.append(selected_kel)


    flat = [item for row in kelompok for item in row]
    girl = [x for x in flat if x[1] == 'P']
    boy = [x for x in flat if x[1] == 'L']

    random.shuffle(girl)
    random.shuffle(boy)

    # for "justice"
    new_data = []
    for row in kelompok:
        row_size = len(row)
        num_girl_needed = round((len(girl) / (len(girl) + len(boy))) * row_size)
        num_boy_needed = row_size - num_girl_needed

        new_row = []
        for _ in range(num_girl_needed):
            if girl: new_row.append(girl.pop())
        for _ in range(num_boy_needed):
            if boy: new_row.append(boy.pop())

        random.shuffle(new_row)
        new_data.append(new_row)
    kelompok = new_data

    return kelompok

PRIMARYCOLOR = "#181818"
BACKGROUNDCOLOR="#232324"
TEXTCOLOR="#ffffff"

params = st.query_params


#if "req1" not in st.session_state:
#    st.session_state.req1 = requests.get("https://api.github.com/users/Molimen")
#st.session_state.req1.raise_for_status()
#if "req2" not in st.session_state:
#    st.session_state.req2 = requests.get("https://api.github.com/users/ce21plozz")
#st.session_state.req2.raise_for_status()
#data_acc_1 = st.session_state.req1.json()
#data_acc_2 = st.session_state.req2.json()

data_acc_1 = {"login": "Molimen", "html_url": "https://github.com/Molimen", "avatar_url": "https://avatars.githubusercontent.com/u/95009791?v=4"}
data_acc_2 = {"login": "Ce21plozz", "html_url": "https://github.com/ce21plozz", "avatar_url": "https://avatars.githubusercontent.com/u/230108871?v=4"}

if "toggle" not in st.session_state:
    st.session_state.toggle = False

if st.session_state.toggle:
    st.session_state.toggle = False
else:
    st.session_state.toggle = True

st.markdown(f"""
<style>
[data-testid="stSidebar"] {{
    width: 100px;
    min-width: 100px;
    max-width: 100px;
    overflow-x: hidden;
    overflow-y: auto;
}}
            
[data-testid="stExpandSidebarButton"] [data-testid="stIconMaterial"],
[data-testid="stSidebarCollapseButton"] [data-testid="stIconMaterial"] {{
    position: relative;
    color: {"#00000000"} !important;
}}

[data-testid="stExpandSidebarButton"] [data-testid="stIconMaterial"]::after {{
    content: "Menu";
    color: {"#fafafa99"}; !important;
    font-size: 24px;
    position: absolute;
    top: 0;
    left: 0;
}}

[data-testid="stSidebarCollapseButton"] [data-testid="stIconMaterial"]::after {{
    content: "Menu";
    color: {"#fafafa99"}; !important;
    font-size: 24px;
    position: absolute;
    top: 0;
    left: 0;

}}
</style>
""", unsafe_allow_html=True)

button_sidebar_kelompok = f"""
button {{
    width: 60px;
    height: 60px; 
    background-image: url('data:image/png;base64,{get_base64("assets/kelompok.png")}');
    background-repeat: no-repeat;
    background-size: 40px;
    background-position: center;
    background-color: {"#2b74d4"};
    transition: 0.3s;
}}
"""

button_sidebar_tempat_duduk = f"""
button {{
    width: 60px;
    height: 60px;
    background-image: url('data:image/png;base64,{get_base64("assets/tempat_duduk.png")}');
    background-repeat: no-repeat;
    background-size: 40px;
    background-position: center;
    background-color: {"#2b74d4"};
    transition: 0.3s;
}}
"""

button_sidebar_about = f"""
button {{
    width: 60px;
    height: 60px;
    background-image: url('data:image/png;base64,{get_base64("assets/about.png")}');
    background-repeat: no-repeat;
    background-size: 40px;
    background-position: center;
    background-color: {"#2b74d4"};
    transition: 0.3s;
}}
"""

st.set_page_config(page_title="Kelompok Generator", page_icon="assets/icon.png")

st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=Amaranth:ital,wght@0,400;0,700;1,400;1,700&family=Anta&family=Convergence&family=Fredoka:wght@550&family=Patrick+Hand&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Arima:wght@100..700&family=BBH+Sans+Bogle&family=Momo+Trust+Display&display=swap');            
            </style>""", unsafe_allow_html=True)

st.markdown("""
<style>
.fredoka-e {
  font-family: "Fredoka", sans-serif;
  font-optical-sizing: auto;
  font-weight: 550;
  font-style: normal;
  font-size: 3rem;
  font-variation-settings:
    "wdth" 100;
}
.patrick-hand-regular {
  font-family: "Patrick Hand", cursive;
  font-weight: 400;
  font-style: normal;
}
.anta-regular {
  font-family: "Anta", sans-serif;
  font-weight: 400;
  font-style: normal;
}
.amaranth-regular {
  font-family: "Amaranth", sans-serif;
  font-weight: 400;
  font-style: normal;
}
.convergence-regular {
  font-family: "Convergence", sans-serif;
  font-weight: 400;
  font-style: normal;
}

.bbh-sans-bogle-regular {
    font-family: "BBH Sans Bogle", sans-serif;
    font-weight: 400;
    font-style: normal;
}

@media (max-width: 768px) {
    .mobile-only {display: block;}
    .desktop-only {display: none;}
}
@media (min-width: 769px) {
    .mobile-only {display: none;}
    .desktop-only {display: block;}
}         
</style>""", unsafe_allow_html=True)

person = [
    # kelas x-1
    [[1, 'L', 0.0], 
     [2, 'L', 0.0], 
     [3, 'L', 0.0], 
     [4, 'P', 0.0], 
     [5, 'P', 0.0], 
     [6, 'L', 0.0], 
     [7, 'P', 0.0], 
     [8, 'P', 0.0], 
     [9, 'L', 0.0], 
     [10, 'L', 0.0], 
     [11, 'L', 0.0], 
     [12, 'P', 0.0], 
     [13, 'L', 0.0], 
     [14, 'L', 0.0], 
     [15, 'P', 0.0], 
     [16, 'P', 0.0], 
     [17, 'P', 0.0], 
     [18, 'L', 0.0], 
     [19, 'P', 0.0], 
     [20, 'L', 0.0], 
     [21, 'L', 0.0], 
     [22, 'L', 0.0], 
     [23, 'P', 0.0], 
     [24, 'P', 0.0], 
     [25, 'L', 0.0], 
     [26, 'P', 0.0], 
     [27, 'L', 0.0], 
     [28, 'L', 0.0], 
     [29, 'P', 0.0], 
     [30, 'P', 0.0], 
     [31, 'P', 0.0], 
     [32, 'L', 0.0]], 
    # kelas x-2
    [[1, 'L', 0.0], 
     [2, 'P', 0.0], 
     [3, 'P', 0.0], 
     [4, 'L', 0.0], 
     [5, 'L', 0.0], 
     [6, 'P', 0.0], 
     [7, 'L', 0.0], 
     [8, 'P', 0.0], 
     [9, 'P', 0.0], 
     [10, 'P', 0.0], 
     [11, 'P', 0.0], 
     [12, 'P', 0.0], 
     [13, 'P', 0.0], 
     [14, 'P', 0.0], 
     [15, 'L', 0.0], 
     [16, 'P', 0.0], 
     [17, 'L', 0.0], 
     [18, 'L', 0.0], 
     [19, 'L', 0.0], 
     [20, 'L', 0.0], 
     [21, 'L', 0.0], 
     [22, 'P', 0.0], 
     [23, 'L', 0.0], 
     [24, 'P', 0.0], 
     [25, 'L', 0.0], 
     [26, 'L', 0.0], 
     [27, 'P', 0.0], 
     [28, 'L', 0.0], 
     [29, 'P', 0.0], 
     [30, 'L', 0.0], 
     [31, 'L', 0.0], 
     [32, 'L', 0.0]], 
    # kelas x-3
    [[1, 'L', 0.0], 
     [2, 'L', 0.0], 
     [3, 'L', 0.0], 
     [4, 'L', 0.0], 
     [5, 'L', 0.0], 
     [6, 'L', 0.0], 
     [7, 'L', 0.0], 
     [8, 'P', 0.0], 
     [9, 'P', 0.0], 
     [10, 'P', 0.0], 
     [11, 'P', 0.0], 
     [12, 'L', 0.0], 
     [13, 'L', 0.0], 
     [14, 'P', 0.0], 
     [15, 'L', 0.0], 
     [16, 'L', 0.0], 
     [17, 'P', 0.0], 
     [18, 'L', 0.0], 
     [19, 'L', 0.0], 
     [20, 'L', 0.0], 
     [21, 'P', 0.0], 
     [22, 'P', 0.0], 
     [23, 'L', 0.0], 
     [24, 'P', 0.0], 
     [25, 'P', 0.0], 
     [26, 'P', 0.0], 
     [27, 'L', 0.0], 
     [28, 'P', 0.0], 
     [29, 'P', 0.0], 
     [30, 'P', 0.0], 
     [31, 'L', 0.0], 
     [32, 'P', 0.0]], 
    # kelas x-4
    [[1, 'L', 0.0], 
     [2, 'P', 0.0], 
     [3, 'L', 0.0], 
     [4, 'P', 0.0], 
     [5, 'P', 0.0], 
     [6, 'L', 0.0], 
     [7, 'L', 0.0], 
     [8, 'L', 0.0], 
     [9, 'P', 0.0], 
     [10, 'L', 0.0], 
     [11, 'L', 0.0], 
     [12, 'P', 0.0], 
     [13, 'P', 0.0], 
     [14, 'P', 0.0], 
     [15, 'P', 0.0], 
     [16, 'P', 0.0], 
     [17, 'L', 0.0], 
     [18, 'P', 0.0], 
     [19, 'P', 0.0], 
     [20, 'L', 0.0], 
     [21, 'L', 0.0], 
     [22, 'L', 0.0], 
     [23, 'L', 0.0], 
     [24, 'P', 0.0], 
     [25, 'L', 0.0], 
     [26, 'L', 0.0], 
     [27, 'L', 0.0], 
     [28, 'L', 0.0], 
     [29, 'P', 0.0], 
     [30, 'P', 0.0], 
     [31, 'L', 0.0], 
     [32, 'P', 0.0]], 
    # kelas x-5
    [[1, 'P', 0.0], 
     [2, 'L', 0.0], 
     [3, 'L', 0.0], 
     [4, 'P', 0.0], 
     [5, 'P', 0.0], 
     [6, 'P', 0.0], 
     [7, 'L', 0.0], 
     [8, 'P', 0.0], 
     [9, 'L', 0.0], 
     [10, 'P', 0.0], 
     [11, 'L', 0.0], 
     [12, 'P', 0.0], 
     [13, 'L', 0.0], 
     [14, 'P', 0.0], 
     [15, 'P', 0.0], 
     [16, 'L', 0.0], 
     [17, 'L', 0.0], 
     [18, 'L', 0.0], 
     [19, 'P', 0.0], 
     [20, 'L', 0.0], 
     [21, 'L', 0.0], 
     [22, 'L', 0.0], 
     [23, 'L', 0.0], 
     [24, 'L', 0.0], 
     [25, 'P', 0.0], 
     [26, 'L', 0.0], 
     [27, 'L', 0.0], 
     [28, 'P', 0.0], 
     [29, 'P', 0.0], 
     [30, 'P', 0.0], 
     [31, 'L', 0.0], 
     [32, 'P', 0.0]], 
    # kelas x-6
    [[1, 'P', 0.0], 
     [2, 'P', 0.0], 
     [3, 'L', 0.0], 
     [4, 'L', 0.0], 
     [5, 'L', 0.0], 
     [6, 'P', 0.0], 
     [7, 'L', 0.0], 
     [8, 'L', 0.0], 
     [9, 'L', 0.0], 
     [10, 'P', 0.0], 
     [11, 'P', 0.0], 
     [12, 'L', 0.0], 
     [13, 'L', 0.0], 
     [14, 'L', 0.0], 
     [15, 'P', 0.0], 
     [16, 'P', 0.0], 
     [17, 'L', 0.0], 
     [18, 'L', 0.0], 
     [19, 'P', 0.0], 
     [20, 'P', 0.0], 
     [21, 'P', 0.0], 
     [22, 'P', 0.0], 
     [23, 'L', 0.0], 
     [24, 'L', 0.0], 
     [25, 'L', 0.0], 
     [26, 'L', 0.0], 
     [27, 'P', 0.0], 
     [28, 'P', 0.0], 
     [29, 'P', 0.0], 
     [30, 'P', 0.0], 
     [31, 'L', 0.0], 
     [32, 'P', 0.0]]]

def play_error_sound():
    with st.sidebar:
        if st.session_state.toggle:
            st.audio("assets/error.wav", format="audio/wav", autoplay=True, width=1)
        else:
            st.audio("assets/error.wav", format="audio/wav", autoplay=True, width=2)

# INIT STOP

with st.sidebar:
    with stylable_container(key="sidebar_kelompok", css_styles=button_sidebar_kelompok):
        if st.button(""):
            st.query_params.clear()
            st.query_params["apps"] = "kelompok"

    st.markdown(
        """
        <div style='display:flex; justify-content:center; align-items:center; padding:10px;'>
                <span style='text-align: center;font-size:0.8rem;'>Kelompok</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    with stylable_container(key="sidebar_tempat_duduk", css_styles=button_sidebar_tempat_duduk):
        if st.button("",key="sidebar_btn_tempat_duduk"):
            st.query_params.clear()
            st.query_params["apps"] = "tempat_duduk"

    st.markdown(
        """
        <div style='display:flex; justify-content:center; align-items:center; padding:10px;'>
                <span style='text-align: center;font-size:0.8rem;'>Tempat Duduk</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()


    with stylable_container(key="sidebar_about", css_styles=button_sidebar_about):
        if st.button("",key="sidebar_about"):
            st.query_params.clear()
            st.query_params["apps"] = "about"

    st.markdown(
        """
        <div style='display:flex; justify-content:center; align-items:center; padding:10px;'>
                <span style='text-align: center;font-size:0.8rem;'>About Us</span>
        </div>
        """,
        unsafe_allow_html=True
    )

if params:
    if params.get("apps") == "kelompok":
        st.markdown(f"""
                    <div style="background-color:{PRIMARYCOLOR};border-radius:8px;padding:10px;line-height:0.95;">
                        <div class="fredoka-e" style= 'text-align: center;font-size:2.5rem;'>Kelompok Generator</div>
                        <br style="margin-top:0px;line-height:0.625;">
                        <div class="anta-regular" style= 'text-align: center;font-size:1.525rem;'>khusus untuk semua kelas 10</div>
                    </div>""", unsafe_allow_html=True)

        st.divider()

        kelas_option = st.selectbox(
            "Pilih Kelas:",
            ["Kosong", "X-1", "X-2", "X-3", "X-4", "X-5", "X-6"]
        )

        find_what = ""
        if not kelas_option == "Kosong": 
            find_what = st.radio(
            "Opsi:",
            ["Jika hanya tau total kelompok", "Jika hanya tau total member di kelompok"]
            )

        member = 0
        total_kelompok = 0
        if find_what == "Jika hanya tau total kelompok":
            total_kelompok = st.number_input("Masukan berapa kelompok:", min_value=0)
        elif find_what == "Jika hanya tau total member di kelompok":
            member = st.number_input("Masukan berapa member di kelompok:", min_value=0)

        if kelas_option == "X-6":
            st.toggle("Smart Finder (Coming Soon!)")

        kelompok = list()
        if st.button("Lakuin pencarian kelompok! 🎲"):
            if total_kelompok > 0 or member > 0:
                try:
                    if (member == 11037 or total_kelompok == 11037) or (
                        member == 5500800 or total_kelompok == 5500800):
                        raise ReferenceError
                    kelompok = randomize(total_kelompok, person[int(kelas_option[2:])-1], member)
                except ReferenceError:
                    if (member == 11037 or total_kelompok == 11037): st.error("LEON!")
                    elif (member == 5500800 or total_kelompok == 5500800): st.error("Someone forgot to pay that debt...")
                    play_error_sound()
                except:
                    st.error("Cek penulisannya!")
                    play_error_sound()
            elif not kelas_option == "kosong":
                st.error("Mohon di isi Bagian atas!")
                play_error_sound()
        counter = 1
        for i in kelompok:
            kell_buff = list()
            for j in i:
                if j[1] == "L":
                    kell_buff.append(f"""<span style='color:{"#0059ff"};margin:0px;font-weight:bold'>{j[0]:02d}</span>""")
                elif j[1] == "P":
                    kell_buff.append(f"""<span style='color:{"#df017c"};margin:0px;font-weight:bold'>{j[0]:02d}</span>""")

            st.markdown(f"""<div style="background-color:{PRIMARYCOLOR};border-radius:8px;padding:10px;line-height:0.95;">
                        {counter:02d} | {', '.join(sorted(kell_buff))}
                        </div><br>""", unsafe_allow_html=True)
            counter += 1

    elif params.get("apps") == "tempat_duduk":
        st.write("Work in progress...")

    if params.get("apps") == "about":
        st.html(f"""
                <style>
                /* From Uiverse.io by kennyotsu */ 
                /*works janky on mobile :<*/
                .card-container {{
                flex-shrink: 0;
                position: relative;
                width: 150px;
                height: 200px;
                transition: 200ms;
                }}
                
                .card-image-layout-gen {{
                    background-image: url(data:image/jpg;base64,{get_base64(r"assets/kel_gen.png")});
                    background-position: top;
                    background-size: cover;
                }}

                .card-image-spelling-bee {{
                    background-image: url(data:image/jpg;base64,{get_base64(r"assets/spelling_bee.png")});
                    background-position: top;
                    background-size: cover;
                }}

                .card-container:active {{
                transform: scale(0.95);
                }}

                #card {{
                position: absolute;
                inset: 0;
                z-index: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                border-radius: 20px;
                transition: 700ms;
                }}

                .card-title {{
                opacity: 0;
                transition-duration: 300ms;
                transition-timing-function: ease-in-out-out;
                transition-delay: 100ms;
                position: absolute;
                font-size: x-large;
                font-weight: bold;
                color: white;
                }}

                .card-tracker:hover ~ #card .card-title {{
                opacity: 1;
                }}

                #card-prompt {{
                z-index: 20;
                transform: translateY(7.6rem);
                font-size: 16px;
                font-weight: bold;
                transition: 200ms;
                position: absolute;
                max-width: 110px;
                color: rgb(255, 255, 255);
                }}

                .card-tracker {{
                position: absolute;
                z-index: 200;
                width: 100%;
                height: 100%;
                }}

                .card-tracker:hover {{
                cursor: pointer;
                }}

                .card-tracker:hover ~ #card #card-prompt {{
                opacity: 0;
                transition: 200ms;
                }}

                .card-tracker:hover ~ #card {{
                transition: 300ms;
                filter: brightness(1.1);
                }}

                .card-container:hover #card::before {{
                transition: 200ms;
                content: '';
                opacity: 80%;
                }}

                .card-canvas {{
                perspective: 800px;
                inset: 0;
                z-index: 200;
                position: absolute;
                display: grid;
                grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
                grid-template-rows: 1fr 1fr 1fr 1fr 1fr;
                gap: 0px 0px;
                grid-template-areas: "tr-1 tr-2 tr-3 tr-4 tr-5"
                    "tr-6 tr-7 tr-8 tr-9 tr-10"
                    "tr-11 tr-12 tr-13 tr-14 tr-15"
                    "tr-16 tr-17 tr-18 tr-19 tr-20"
                    "tr-21 tr-22 tr-23 tr-24 tr-25";
                }}

                .tr-1 {{
                grid-area: tr-1;
                }}

                .tr-2 {{
                grid-area: tr-2;
                }}

                .tr-3 {{
                grid-area: tr-3;
                }}

                .tr-4 {{
                grid-area: tr-4;
                }}

                .tr-5 {{
                grid-area: tr-5;
                }}

                .tr-6 {{
                grid-area: tr-6;
                }}

                .tr-7 {{
                grid-area: tr-7;
                }}

                .tr-8 {{
                grid-area: tr-8;
                }}

                .tr-9 {{
                grid-area: tr-9;
                }}

                .tr-10 {{
                grid-area: tr-10;
                }}

                .tr-11 {{
                grid-area: tr-11;
                }}

                .tr-12 {{
                grid-area: tr-12;
                }}

                .tr-13 {{
                grid-area: tr-13;
                }}

                .tr-14 {{
                grid-area: tr-14;
                }}

                .tr-15 {{
                grid-area: tr-15;
                }}

                .tr-16 {{
                grid-area: tr-16;
                }}

                .tr-17 {{
                grid-area: tr-17;
                }}

                .tr-18 {{
                grid-area: tr-18;
                }}

                .tr-19 {{
                grid-area: tr-19;
                }}

                .tr-20 {{
                grid-area: tr-20;
                }}

                .tr-21 {{
                grid-area: tr-21;
                }}

                .tr-22 {{
                grid-area: tr-22;
                }}

                .tr-23 {{
                grid-area: tr-23;
                }}

                .tr-24 {{
                grid-area: tr-24;
                }}

                .tr-25 {{
                grid-area: tr-25;
                }}

                .tr-1:hover ~ #card {{
                transition: 125ms ease-in-out;
                transform: rotateX(20deg) rotateY(-10deg) rotateZ(0deg);
                }}

                .tr-2:hover ~ #card {{
                transition: 125ms ease-in-out;
                transform: rotateX(20deg) rotateY(-5deg) rotateZ(0deg);
                }}

                .tr-3:hover ~ #card {{
                transition: 125ms ease-in-out;
                transform: rotateX(20deg) rotateY(0deg) rotateZ(0deg);
                }}

                .tr-4:hover ~ #card {{
                transition: 125ms ease-in-out;
                transform: rotateX(20deg) rotateY(5deg) rotateZ(0deg);
                }}

                .tr-5:hover ~ #card {{
                transition: 125ms ease-in-out;
                transform: rotateX(20deg) rotateY(10deg) rotateZ(0deg);
                }}

                .tr-6:hover ~ #card {{
                transition: 125ms ease-in-out;
                transform: rotateX(10deg) rotateY(-10deg) rotateZ(0deg);
                }}

                .tr-7:hover ~ #card {{
                transition: 125ms ease-in-out;
                transform: rotateX(10deg) rotateY(-5deg) rotateZ(0deg);
                }}

                .tr-8:hover ~ #card {{
                transition: 125ms ease-in-out;
                transform: rotateX(10deg) rotateY(0deg) rotateZ(0deg);
                }}

                .tr-9:hover ~ #card {{
                transition: 125ms ease-in-out;
                transform: rotateX(10deg) rotateY(5deg) rotateZ(0deg);
                }}

                .tr-10:hover ~ #card {{
                transition: 125ms ease-in-out;
                transform: rotateX(10deg) rotateY(10deg) rotateZ(0deg);
                }}

                .tr-11:hover ~ #card {{
                transition: 125ms ease-in-out;
                transform: rotateX(0deg) rotateY(-10deg) rotateZ(0deg);
                }}

                .tr-12:hover ~ #card {{
                transition: 125ms ease-in-out;
                transform: rotateX(0deg) rotateY(-5deg) rotateZ(0deg);
                }}

                .tr-13:hover ~ #card {{
                transition: 125ms ease-in-out;
                transform: rotateX(0deg) rotateY(0deg) rotateZ(0deg);
                }}

                .tr-14:hover ~ #card {{
                transition: 125ms ease-in-out;
                transform: rotateX(0deg) rotateY(5deg) rotateZ(0deg);
                }}

                .tr-15:hover ~ #card {{
                transition: 125ms ease-in-out;
                transform: rotateX(0deg) rotateY(10deg) rotateZ(0deg);
                }}

                .tr-16:hover ~ #card {{
                transition: 125ms ease-in-out;
                transform: rotateX(-10deg) rotateY(-10deg) rotateZ(0deg);
                }}

                .tr-17:hover ~ #card {{
                transition: 125ms ease-in-out;
                transform: rotateX(-10deg) rotateY(-5deg) rotateZ(0deg);
                }}

                .tr-18:hover ~ #card {{
                transition: 125ms ease-in-out;
                transform: rotateX(-10deg) rotateY(0deg) rotateZ(0deg);
                }}

                .tr-19:hover ~ #card {{
                transition: 125ms ease-in-out;
                transform: rotateX(-10deg) rotateY(5deg) rotateZ(0deg);
                }}

                .tr-20:hover ~ #card {{
                transition: 125ms ease-in-out;
                transform: rotateX(-10deg) rotateY(10deg) rotateZ(0deg);
                }}

                .tr-21:hover ~ #card {{
                transition: 125ms ease-in-out;
                transform: rotateX(-20deg) rotateY(-10deg) rotateZ(0deg);
                }}

                .tr-22:hover ~ #card {{
                transition: 125ms ease-in-out;
                transform: rotateX(-20deg) rotateY(-5deg) rotateZ(0deg);
                }}

                .tr-23:hover ~ #card {{
                transition: 125ms ease-in-out;
                transform: rotateX(-20deg) rotateY(0deg) rotateZ(0deg);
                }}

                .tr-24:hover ~ #card {{
                transition: 125ms ease-in-out;
                transform: rotateX(-20deg) rotateY(5deg) rotateZ(0deg);
                }}

                .tr-25:hover ~ #card {{
                transition: 125ms ease-in-out;
                transform: rotateX(-20deg) rotateY(10deg) rotateZ(0deg);
                }}

                .noselect {{
                -webkit-touch-callout: none;
                /* iOS Safari */
                -webkit-user-select: none;
                /* Safari */
                /* Konqueror HTML */
                -moz-user-select: none;
                /* Old versions of Firefox */
                -ms-user-select: none;
                /* Internet Explorer/Edge */
                user-select: none;
                /* Non-prefixed version, currently
                                                    supported by Chrome, Edge, Opera and Firefox */
                }}
                </style>""")

        st.html(f"""
                <style>
                .divider-container {{
                display: flex;
                align-items: center;
                justify-content: center;
                z-index: 1;
                width: 100%;
                height: .5rem;
                position: relative;
                }}
                
                .divider-container::before, .divider-container::after {{
                transition: all 1s ease;
                }}

                .divider-container::before {{
                content: "";
                top: -197%;
                width: 40px;
                height: 40px;
                background-color: {PRIMARYCOLOR};
                position: absolute;
                transform: rotate(45deg);
                animation: bg-divider-scale 7s ease-out infinite;
                }}

                .divider-container::after {{
                content: "";
                width: 20px;
                height: 20px;
                background-color: {"#ffffff"};
                position: absolute;
                transform: rotate(45deg);
                animation: divider-spin 7s ease infinite;
                }}


                .divider {{
                height: .35rem;
                width: 100%;
                background-image: linear-gradient(90deg, {"#00000000"}, {"#ffffff"}, {"#ffffff"}, {"#00000000"});
                margin: 1.5em;
                }}

                @keyframes divider-spin {{
                0% {{ transform: rotate(0deg); }}
                5.88% {{ transform: rotate(0deg); }}
                11.76% {{ transform: rotate(45deg); }}
                17.64% {{ transform: rotate(45deg); }}
                23.52% {{ transform: rotate(90deg); }}
                29.4% {{ transform: rotate(90deg); }}
                35.28% {{ transform: rotate(135deg); }}
                41.16% {{ transform: rotate(135deg); }}
                47.04% {{ transform: rotate(180deg); }}
                52.92% {{ transform: rotate(180deg); }}
                58.8% {{ transform: rotate(225deg); }}
                64.68% {{ transform: rotate(225deg); }}
                70.56% {{ transform: rotate(270deg); }}
                76.44% {{ transform: rotate(270deg); }}
                82.32% {{ transform: rotate(315deg); }}
                88.2% {{ transform: rotate(315deg); }}
                100% {{ transform: rotate(360deg); }}
                }}
            @keyframes bg-divider-scale {{
                0% {{ transform:  scale(1); }}
                5.88% {{ transform:  scale(1); }}
                11.76% {{ transform:  scale(1.25); }}
                17.64% {{ transform:  scale(1.25); }}
                23.52% {{ transform:  scale(1); }}
                29.4% {{ transform:  scale(1); }}
                35.28% {{ transform:  scale(1.25); }}
                41.16% {{ transform:  scale(1.25); }}
                47.04% {{ transform:  scale(1); }}
                52.92% {{ transform:  scale(1); }}
                58.8% {{ transform:  scale(1.25); }}
                64.68% {{ transform:  scale(1.25); }}
                70.56% {{ transform:  scale(1); }}
                76.44% {{ transform:  scale(1); }}
                82.32% {{ transform:  scale(1.25); }}
                88.2% {{ transform: scale(1.25); }}
                94.08% {{ transform: scale(1); }}
                100% {{ transform: scale(1); }}
                }}
                </style>""")

        st.html(f"""
                <style>
                .hover-image {{
                    transition: transform 0.3s ease;
                }}

                .hover-image:hover {{
                    transform: scale(1.1);
                }}



                .imagecontainer img {{
                    box-sizing: border-box;
                    height: 4.5em;
                    border: 5px solid {"#303031"};
                    border-radius: 20px 0 20px 0;
                }}

                .title-image img {{
                    height: 2.8em;
                    border: 4px solid {"#FFFFFF"};
                    border-radius: 9999px;
                }}

                .about-grid {{
                    display:grid;
                    grid-template-columns:repeat(2, 1fr);
                    grid-template-rows: repeat(2, 1fr);
                    gap: 1rem;
                }}

                .about-grid-block {{
                    background-color:{PRIMARYCOLOR};
                    border-radius:8px;
                    padding:0 15px 8px 15px;
                }}

                .about-grid-1 {{
                    grid-area: 1 / 1 / 3 / 2;
                }}

                .about-grid-2 {{
                    grid-area: 1 / 2 / 2 / 3;
                }}

                .about-grid-3 {{
                    grid-area: 2 / 2 / 3 / 3;
                }}

                @media (max-width: 768px) {{
                    .about-grid {{
                        grid-template-columns: 1fr;
                        grid-template-rows: repeat(3, 1fr);
                    }}

                    .about-grid-1 {{
                        grid-area: 1 / 1 / 2 / 2;
                    }}

                    .about-grid-2 {{
                        grid-area: 2 / 1 / 3 / 2;
                    }}

                    .about-grid-3 {{
                        grid-area: 3 / 1 / 4 / 2;
                    }}
                }}
                </style>""")

        st.markdown(f"""
                    <div style="display:flex;align-items:center;justify-content:left;margin:0 0 0.3rem 0">
                        <div class="title-image">
                            <img src="data:image/jpg;base64,{get_base64(r"assets/about.png")}">
                        </div>
                        <div style="font-size:2.5rem;margin:0 0 0 .8rem"><span style='font-weight:bold;'>ABOUT</span></div>
                    </div>

                    <div class="about-grid">
                        <div class="about-grid-block about-grid-1">
                            <div style="display:flex;">
                                <div class="card-container noselect" style="margin: .8rem 0 0 0;">
                                    <a href="https://layout-tempat-duduk-generator.streamlit.app/" target="_self">
                                        <div class="card-canvas">
                                            <div class="card-tracker tr-1"></div>
                                            <div class="card-tracker tr-2"></div>
                                            <div class="card-tracker tr-3"></div>
                                            <div class="card-tracker tr-4"></div>
                                            <div class="card-tracker tr-5"></div>
                                            <div class="card-tracker tr-6"></div>
                                            <div class="card-tracker tr-7"></div>
                                            <div class="card-tracker tr-8"></div>
                                            <div class="card-tracker tr-9"></div>
                                            <div class="card-tracker tr-10"></div>
                                            <div class="card-tracker tr-11"></div>
                                            <div class="card-tracker tr-12"></div>
                                            <div class="card-tracker tr-13"></div>
                                            <div class="card-tracker tr-14"></div>
                                            <div class="card-tracker tr-15"></div>
                                            <div class="card-tracker tr-16"></div>
                                            <div class="card-tracker tr-17"></div>
                                            <div class="card-tracker tr-18"></div>
                                            <div class="card-tracker tr-19"></div>
                                            <div class="card-tracker tr-20"></div>
                                            <div class="card-tracker tr-21"></div>
                                            <div class="card-tracker tr-22"></div>
                                            <div class="card-tracker tr-23"></div>
                                            <div class="card-tracker tr-24"></div>
                                            <div class="card-tracker tr-25"></div>
                                            <div id="card" class="card-image-layout-gen">
                                                <p id="card-prompt">HOVER OVER :D</p>
                                            </div>
                                        </div>
                                    </a>
                                </div>
                                <div style="margin: .3rem 0 0 .6rem;display:flex; flex-direction: column;">
                                    <div style="font-size:1.5rem;"><span style='font-weight:bold;'>layout-gen</span></div>
                                    <p style="margin:0px;font-weight:400;font-size:1rem;">This is state of the art "layout-tempat-duduk-generator" for class of 2025-2026.</p>
                                </div>
                            </div>
                            <div style="margin: 2.5rem 0 1rem 0"><div class="divider-container"><div class="divider"></div></div></div>
                            <div style="display:flex;">
                                <div class="card-container noselect" style="margin: .8rem 0 0 0;">
                                    <a href="https://spelling-bee-100.streamlit.app/" target="_self">
                                        <div class="card-canvas">
                                            <div class="card-tracker tr-1"></div>
                                            <div class="card-tracker tr-2"></div>
                                            <div class="card-tracker tr-3"></div>
                                            <div class="card-tracker tr-4"></div>
                                            <div class="card-tracker tr-5"></div>
                                            <div class="card-tracker tr-6"></div>
                                            <div class="card-tracker tr-7"></div>
                                            <div class="card-tracker tr-8"></div>
                                            <div class="card-tracker tr-9"></div>
                                            <div class="card-tracker tr-10"></div>
                                            <div class="card-tracker tr-11"></div>
                                            <div class="card-tracker tr-12"></div>
                                            <div class="card-tracker tr-13"></div>
                                            <div class="card-tracker tr-14"></div>
                                            <div class="card-tracker tr-15"></div>
                                            <div class="card-tracker tr-16"></div>
                                            <div class="card-tracker tr-17"></div>
                                            <div class="card-tracker tr-18"></div>
                                            <div class="card-tracker tr-19"></div>
                                            <div class="card-tracker tr-20"></div>
                                            <div class="card-tracker tr-21"></div>
                                            <div class="card-tracker tr-22"></div>
                                            <div class="card-tracker tr-23"></div>
                                            <div class="card-tracker tr-24"></div>
                                            <div class="card-tracker tr-25"></div>
                                            <div id="card" class="card-image-spelling-bee">
                                                <p id="card-prompt">HOVER OVER :D</p>
                                            </div>
                                        </div>
                                    </a>
                                </div>
                                <div style="margin: .3rem 0 0 .6rem;display:flex; flex-direction: column;">
                                    <div style="font-size:1.5rem;"><span style='font-weight:bold;'>Spell Bee</span></div>
                                    <p style="margin:0px;font-weight:400;font-size:1rem;">This is for my tugas.</p>
                                </div>
                            </div>
                            <br>
                        </div>
                        <div class="about-grid-block about-grid-2">
                            Comming soon!
                        </div>
                        <div class="about-grid-block about-grid-3">
                            <div style="font-size:1.5rem;margin:.2rem 0 0 0"><span style='font-weight:bold;'>Credits</span></div>
                            <p style="margin:0px;font-weight:bold;font-size:1rem;">These people that help or make this.</p>
                            <div style="display:flex;margin: .8rem 0 0 0;">
                                <div class="imagecontainer">
                                    <a href="{data_acc_1["html_url"]}" target="_self">
                                    <img src="{data_acc_1["avatar_url"]}" class="hover-image">
                                    </a>
                                </div>
                                <div style="margin: 0 0 0 .8rem;">
                                    <span style="font-size:1.25rem;line-height:1.75rem;font-weight:600;">{data_acc_1["login"]}</span>
                                    <p style="font-size:.875rem;line-height:1.55rem;font-weight:400;">Developer</p>
                                </div>
                            </div>
                            <div style="display:flex;margin: .8rem 0 0 0;">
                                <div class="imagecontainer">
                                    <a href="{data_acc_2["html_url"]}" target="_self">
                                    <img src="{data_acc_2["avatar_url"]}" class="hover-image">
                                    </a>
                                </div>
                                <div style="margin: 0 0 0 .8rem;">
                                    <span style="font-size:1.25rem;line-height:1.75rem;font-weight:600;">{data_acc_2["login"]}</span>
                                    <p style="font-size:.875rem;line-height:1.55rem;font-weight:400;">UI idea</p>
                                </div>
                            </div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)


        
else:
    # Temporary
    st.write("redirected...")
    st.query_params.clear()
    st.query_params["apps"] = "kelompok"
    st.rerun()