import streamlit as st
import random
from math import floor

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

st.markdown("""<h1 style= 'text-align: center;font-family: 'Cera CY', Helvetica, Arial, sans-serif;color:white'>"Justice" Kelompok Generator</h1>""", unsafe_allow_html=True)
st.markdown("")

kelas_option = st.selectbox(
    "Choose an Kelas:",
    ["X-1", "X-2", "X-3", "X-4", "X-5", "X-6"]
)

find_what = st.radio(
    "blud mw cari apa:",
    ["Jika tau total kelompok", "Jika tau total member di kelompok"]
)

member = 0
total_kelompok = 0
if find_what == "Jika tau total kelompok":
    total_kelompok = st.number_input("Masukan berapa kelompok:", min_value=0)
elif find_what == "Jika tau total member di kelompok":
    member = st.number_input("Masukan berapa member di kelompok:", min_value=0)

kelompok = list()
if st.button("Lakuin pencarian kelompok 3000! 🎲") and (member > 0 or total_kelompok > 0):
    kelompok = randomize(total_kelompok, person[int(kelas_option[2:])-1], member)

counter = 1
for i in kelompok:
    kell_buff = list()
    for j in i:
        if j[1] == "L":
            kell_buff.append(f"**:red[{j[0]:02d}]**")
        elif j[1] == "P":
            kell_buff.append(f"**:violet[{j[0]:02d}]**")

    st.write(f"{counter:02d} | {", ".join(sorted(kell_buff))}")
    counter += 1
