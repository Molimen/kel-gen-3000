import streamlit as st
import random
from math import floor
import base64
from streamlit_javascript import st_javascript
from streamlit_extras.stylable_container import stylable_container

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

theme = st_javascript("window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'")

params = st.query_params

st.markdown("""
<style>
[data-testid="stSidebar"] {
    width: 100px;
    min-width: 100px;
    max-width: 100px;
    overflow-x: hidden;
    overflow-y: auto;
}
</style>
""", unsafe_allow_html=True)

button_sidebar_kelompok = f"""
button {{
    width: 60px;
    height: 60px; 
    background-image: url('data:image/png;base64,{get_base64("kelompok.png")}');
    background-repeat: no-repeat;
    background-size: 40px;
    background-position: center;
    background-color: #2b74d4;
    transition: 0.3s;
}}
button:hover {{
    background-color: #1b4f91;
}}
"""

button_sidebar_tempat_duduk = f"""
button {{
    width: 60px;
    height: 60px;
    background-image: url('data:image/png;base64,{get_base64("tempat_duduk.png")}');
    background-repeat: no-repeat;
    background-size: 40px;
    background-position: center;
    background-color: #2b74d4;
    transition: 0.3s;
}}
button:hover {{
    background-color: #1b4f91;
}}
"""

button_sidebar_settings = f"""
button {{
    width: 60px;
    height: 60px;
    background-image: url('data:image/png;base64,{get_base64("settings.png")}');
    background-repeat: no-repeat;
    background-size: 40px;
    background-position: center;
    background-color: #2b74d4;
    transition: 0.3s;
}}
button:hover {{
    background-color: #1b4f91;
}}
"""

button_sidebar_about = f"""
button {{
    width: 60px;
    height: 60px;
    background-image: url('data:image/png;base64,{get_base64("about.png")}');
    background-repeat: no-repeat;
    background-size: 40px;
    background-position: center;
    background-color: #2b74d4;
    transition: 0.3s;
}}
button:hover {{
    background-color: #1b4f91;
}}
"""

st.set_page_config(page_title="Kelompok Generator", page_icon="icon.png")

st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=Amaranth:ital,wght@0,400;0,700;1,400;1,700&family=Anta&family=Convergence&family=Fredoka:wght@550&family=Patrick+Hand&display=swap');
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

</style>""", unsafe_allow_html=True)

person = [
    # kelas x-1
    [[1, 'L'], [2, 'L'], [3, 'L'], [4, 'P'], [5, 'P'], [6, 'L'], [7, 'P'], [8, 'P'], [9, 'L'], [10, 'L'], [11, 'L'], [12, 'P'], [13, 'L'], [14, 'L'], [15, 'P'], [16, 'P'], [17, 'P'], [18, 'L'], [19, 'P'], [20, 'L'], [21, 'L'], [22, 'L'], [23, 'P'], [24, 'P'], [25, 'L'], [26, 'P'], [27, 'L'], [28, 'L'], [29, 'P'], [30, 'P'], [31, 'P'], [32, 'L']], 
    # kelas x-2
    [[1, 'L'], [2, 'P'], [3, 'P'], [4, 'L'], [5, 'L'], [6, 'P'], [7, 'L'], [8, 'P'], [9, 'P'], [10, 'P'], [11, 'P'], [12, 'P'], [13, 'P'], [14, 'P'], [15, 'L'], [16, 'P'], [17, 'L'], [18, 'L'], [19, 'L'], [20, 'L'], [21, 'L'], [22, 'P'], [23, 'L'], [24, 'P'], [25, 'L'], [26, 'L'], [27, 'P'], [28, 'L'], [29, 'P'], [30, 'L'], [31, 'L'], [32, 'L']], 
    # kelas x-3
    [[1, 'L'], [2, 'L'], [3, 'L'], [4, 'L'], [5, 'L'], [6, 'L'], [7, 'L'], [8, 'P'], [9, 'P'], [10, 'P'], [11, 'P'], [12, 'L'], [13, 'L'], [14, 'P'], [15, 'L'], [16, 'L'], [17, 'P'], [18, 'L'], [19, 'L'], [20, 'L'], [21, 'P'], [22, 'P'], [23, 'L'], [24, 'P'], [25, 'P'], [26, 'P'], [27, 'L'], [28, 'P'], [29, 'P'], [30, 'P'], [31, 'L'], [32, 'P']], 
    # kelas x-4
    [[1, 'L'], [2, 'P'], [3, 'L'], [4, 'P'], [5, 'P'], [6, 'L'], [7, 'L'], [8, 'L'], [9, 'P'], [10, 'L'], [11, 'L'], [12, 'P'], [13, 'P'], [14, 'P'], [15, 'P'], [16, 'P'], [17, 'L'], [18, 'P'], [19, 'P'], [20, 'L'], [21, 'L'], [22, 'L'], [23, 'L'], [24, 'P'], [25, 'L'], [26, 'L'], [27, 'L'], [28, 'L'], [29, 'P'], [30, 'P'], [31, 'L'], [32, 'P']], 
    # kelas x-5
    [[1, 'P'], [2, 'L'], [3, 'L'], [4, 'P'], [5, 'P'], [6, 'P'], [7, 'L'], [8, 'P'], [9, 'L'], [10, 'P'], [11, 'L'], [12, 'P'], [13, 'L'], [14, 'P'], [15, 'P'], [16, 'L'], [17, 'L'], [18, 'L'], [19, 'P'], [20, 'L'], [21, 'L'], [22, 'L'], [23, 'L'], [24, 'L'], [25, 'P'], [26, 'L'], [27, 'L'], [28, 'P'], [29, 'P'], [30, 'P'], [31, 'L'], [32, 'P']], 
    # kelas x-6
    [[1, 'P'], [2, 'P'], [3, 'L'], [4, 'L'], [5, 'L'], [6, 'P'], [7, 'L'], [8, 'L'], [9, 'L'], [10, 'P'], [11, 'P'], [12, 'L'], [13, 'L'], [14, 'L'], [15, 'P'], [16, 'P'], [17, 'L'], [18, 'L'], [19, 'P'], [20, 'P'], [21, 'P'], [22, 'P'], [23, 'L'], [24, 'L'], [25, 'L'], [26, 'L'], [27, 'P'], [28, 'P'], [29, 'P'], [30, 'P'], [31, 'L'], [32, 'P']]]

# INIT STOP

with st.sidebar:
    with stylable_container(key="sidebar_kelompok", css_styles=button_sidebar_kelompok):
        if st.button("", key="sidebar_btn_kelompok"):
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

    with stylable_container(key="sidebar_settings", css_styles=button_sidebar_settings):
        if st.button("",key="sidebar_btn_settings"):
            st.query_params.clear()
            st.query_params["settings"] = "set1"

    st.markdown(
        """
        <div style='display:flex; justify-content:center; align-items:center; padding:10px;'>
                <span style='text-align: center;font-size:0.8rem;'>Settings</span>
        </div>
        """,
        unsafe_allow_html=True
    )


    with stylable_container(key="sidebar_about", css_styles=button_sidebar_about):
        if st.button("",key="sidebar_btn_about"):
            st.query_params.clear()
            st.query_params["about"] = ""

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
                    <div style="background-color:{"#171C26" if theme == "dark" else "#f0f2f6"};border-radius:8px;padding:10px;line-height:0.95;">
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
        if not kelas_option == "Kosong": find_what = st.radio(
            "Opsi:",
            ["Jika hanya tau total kelompok", "Jika hanya tau total member di kelompok"]
        )

        member = 0
        total_kelompok = 0
        if find_what == "Jika hanya tau total kelompok":
            total_kelompok = st.number_input("Masukan berapa kelompok:", min_value=0)
        elif find_what == "Jika hanya tau total member di kelompok":
            member = st.number_input("Masukan berapa member di kelompok:", min_value=0)

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
                except:
                    st.error("Cek penulisannya!")
            elif not kelas_option == "kosong":
                st.error("Mohon di isi Bagian atas!")

        counter = 1
        for i in kelompok:
            kell_buff = list()
            for j in i:
                if j[1] == "L":
                    kell_buff.append(f"""<span style='color:{"#0059ff"};margin:0px;font-weight:bold'>{j[0]:02d}</span>""")
                elif j[1] == "P":
                    kell_buff.append(f"""<span style='color:{"#df017c"};margin:0px;font-weight:bold'>{j[0]:02d}</span>""")

            st.markdown(f"""<div style="background-color:{"#171C26" if theme == "dark" else "#f0f2f6"};border-radius:8px;padding:10px;line-height:0.95;">
                        {counter:02d} | {', '.join(sorted(kell_buff))}
                        </div><br>""", unsafe_allow_html=True)
            counter += 1

    elif params.get("apps") == "tempat_duduk":
        st.write("Work in progress...")

    if params.get("settings") == "set1":
        st.write("Work in progress...")

    if params.get("about") == "":
        st.markdown(f"""
                    <div style="text-align:center;font-size:1.6rem;background-color:{"#171C26" if theme == "dark" else "#f0f2f6"};border-radius:8px;padding:10px;">
                        <span style='margin:0px;font-weight:bold'>🏗️ Project lain</span>
                    </div>
                    <br>
                    <div style="background-color:{"#171C26" if theme == "dark" else "#f0f2f6"};border-radius:8px;padding:20px;line-height:0.95;">
                    <div class="convergence-regular" style='font-weight:bold;font-size:1.2rem;text-align:center'>Tempat Duduk Generator</div> 
                    <br>
                    <div style="text-align:center">
                        <span class="convergence-regular" style='font-weight:bold;font-size:0.9rem'>(Pembuat Tempat duduk yang adil, pencet gambar dibawah!)</span>
                    </div>
                    
                    <br>
                    <div style="text-align:center">
                        <a href="https://layout-tempat-duduk-generator.streamlit.app/">
                            <img src="data:image/jpg;base64,{get_base64(r"image.jpg")}"
                            alt = "placeholder"
                            title="PENCET INI GAMBAR!!"
                            target = "_blank"
                            style="border-radius:20px;
                            cursor:pointer;
                            width:250px;
                            border: 5px solid black;
                            ">               
                        </a>
                    </div></div>""", unsafe_allow_html=True)

        st.markdown("""
                <br>
                <span style='margin:0px;font-weight:bold'>Credits:</span>
                <br>
                <pre>
                <span style='font-weight:bold'>1.) Gw yang tukang elektronik/komputer itu (Pembuat proyek)<br>2.) si namanya cuma satu kata (design menu    )</span>
                </pre>""", unsafe_allow_html=True)
        
else:
    # Temporary
    st.write("redirected...")
    st.query_params.clear()
    st.query_params["apps"] = "kelompok"