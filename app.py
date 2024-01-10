import pickle
import streamlit as st
import pandas as pd

meslekler = pickle.load(open('is_liste.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))


def recommend(meslek):
    index = meslekler[meslekler['meslek'] == meslek].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    nos = []
    recommended_job_names = []
    recommended_job_tanim = []
    recommended_job_gereksinim = []
    for i in distances[1:9]:
        nos.append(meslekler.iloc[i[0]].no)
        recommended_job_names.append(meslekler.iloc[i[0]].meslek)
        recommended_job_tanim.append(meslekler.iloc[i[0]].tanim)
        recommended_job_gereksinim.append(meslekler.iloc[i[0]].gereksinim)

    return nos,recommended_job_names,recommended_job_tanim,recommended_job_gereksinim

st.markdown("""
<style>
.big-font {
    font-size:60px !important;
}
</style>
""", unsafe_allow_html=True)


st.image("Meslek.jpg")



#st.markdown('<font color="orange" class="big-font">Meslek Arama Motoru</font>', unsafe_allow_html=True)
#st.markdown('<font color="yellow" class="big-font">ARAMA</font>', unsafe_allow_html=True)
#st.markdown('<font color="blue" class="big-font">MOTORU</font>', unsafe_allow_html=True)
#st.header('Meslek Arama Motoru')
#st.header(':red[M]:blue[e]:orange[s]:violet[l]:gray[e]:red[k]:rainbow[  ]  :blue[A]:violet[r]:green[a]:red[m]:blue[a]      :orange[M]:red[o]:violet[t]:blue[o]:green[r]:orange[u]')
is_liste = meslekler['meslek'].values
selected_job = st.selectbox(
    "Bir meslek ismi ya da ilgilendiğiniz alanla ilgili bir kelime giriniz...",is_liste)



if st.button("Meslekleri Bul", type="primary"):
    st.success('Bu bilgiler, genel yönlendirmelerdir '
               've belirli işverenler '
               'farklı eğitim ve deneyim gereksinimleri isteyebilir. '
               'Bu nedenle, bireylerin kariyer hedeflerine ve '
               'yerel taleplere uygun olarak ek eğitim ve deneyim kazanmaları önemlidir.'
               'İlgili sektörlerdeki değişikliklere ve işveren tercihlerine bağlı '
               'olarak, farklı kariyer yolları ve eğitim gereksinimleri ortaya çıkabilir.')
    st.info('Gereksinimler, meslek ve sektöre bağlı olarak, özel şirket politikalarına, '
            'yerel düzenlemelere veya tercihlere göre değişiklik gösterebilir.'
            'Sektördeki teknolojik gelişmeler ve '
               'ihtiyaçlar göz önüne alındığında, sürekli '
               'eğitim ve güncellemeler de önemlidir.')
    with st.spinner(text='Aranıyor...:hourglass:'):
        nos,recommended_job_names, recommended_job_tanim,recommended_job_gereksinim= recommend(selected_job)
        for i in range(8):

            st.subheader(" :white_check_mark: " +str(recommended_job_names[i]))
            st.write('    ');

            st.subheader(":question:  *Tanım*")
            st.write(str(recommended_job_tanim[i]))
            st.write('    ');
            st.subheader(":pencil: *Kariyer Yolu*")
            st.write(str(recommended_job_gereksinim[i]))
            st.write("NO: " + str(nos[i]))
            st.write('    ');
            st.header(" ",divider = 'rainbow')
            st.write('    ');
            st.write('    ');

