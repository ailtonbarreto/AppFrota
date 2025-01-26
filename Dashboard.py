import streamlit as st
import pandas as pd
import datetime as dt
import gspread as gs
from gspread import worksheet
import streamlit.components.v1 as components
import pytz

# ---------------------------------------------------------------------------------------------
# layout

st.set_page_config(page_title="Gestão de Frota",layout="wide",initial_sidebar_state="collapsed",page_icon="🚛")


with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html = True)

st.image('img/header.png',width=1000)


# ---------------------------------------------------------------------------------------------
# Dataframe principal
@st.cache_data
def load_viagens():
    url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSLYIhif_-IpAqFzG2uZKZ2Rifj0xmdek42-wuj2mNuGWYENnZLY1gRSzh9NnUYh0f1_9xpBoMttk5a/pub?gid=2121011744&single=true&output=csv'
    df = pd.read_csv(url)
    return df


df = load_viagens()

df[["Data", "Hora"]] = df["Carimbo de data/hora"].str.split(" ", expand=True)

df["Data"] = pd.to_datetime(df["Data"])

df = df.drop(columns="Carimbo de data/hora")

df["Ano"] = df["Data"].dt.year
df["Mês"] = df["Data"].dt.month
df['Data'] = df['Data'].dt.strftime('%d/%m/%Y')
df = df.rename(columns={"Tipo:": "Tipo"})
df = df.rename(columns={"Veículo:": "Veículo"})

frame = 'https://docs.google.com/forms/d/e/1FAIpQLSeSWA0R9Bwf9t1RPnrYYHZG5dUrNyyDxbdLpevKT3lP0-5afw/viewform?embedded=true'

# ---------------------------------------------------------------------------------------------
# layout

tab1, tab2,tab3 = st.tabs(["Disponibilidade","Registros","Formulário"])


with tab1:
    st.subheader("Disponibilidade da Frota", anchor=False)
    
with tab2:
    st.subheader("Registros", anchor=False)
    
with tab3:
    st.subheader("Link Para Preencher",anchor=False)
    st.image("img/qr.png")
    components.iframe(src=frame, width=800, height=800)


# ---------------------------------------------------------------------------------------------
# Dataframe viagens

viagens = df

# ---------------------------------------------------------------------------------------------
# Dataframe motoristas

df_motoristas = df["Motorista:"].unique()

df_Veiculos = df["Veículo"].unique()


# # ---------------------------------------------------------------------------------------------

df_tipo = df.groupby("Veículo")["Tipo"].value_counts().reset_index()

df_tipo = df_tipo.groupby("Veículo")["count"].sum().reset_index()

df_tipo["disp"] = df_tipo["count"].apply(lambda x: x % 2)

rua = (df_tipo['disp'] == 1).sum()

df_status = df_tipo

df_status["status"] = df_status["disp"].replace(1,"Rua").replace(0,"Pátio")

df_status = df_status.drop(columns=["count","disp"])

max_date = df['Data'].max()


# ---------------------------------------------------------------------------------------------
# cards

df_qtd_viagens = df.query('Tipo == "Saída"')

df_qtd_viagens = df_qtd_viagens["Tipo"].count()


# -----------------------------------------------------------------------------------------------------------

qtd_motoristas = df_motoristas.shape[0]

qtd_Veiculos = df_Veiculos.shape[0]

patio = qtd_Veiculos - rua

# -----------------------------------------------------------------------------------------------------------

carros_disp = df.query('Tipo == "Saída"')

carros_disp = carros_disp["Veículo"].unique()

carros_disp = carros_disp.shape[0]


# -----------------------------------------------------------------------------------------------------------
# VIAGENS

with tab1:

    card1, card2, card3, card4, card5 = st.columns(5)


    # carro A status
  
    

    carda, cardb, cardc, cardd, carde = st.columns(5)

    df_carro = df.query('Veículo == "Veículo A"')

    contagem_saidas2 = df_carro.shape[0]

    with carda:
        ultimo_indice = df_carro.index.max()

        if contagem_saidas2 % 2 == 0:
            st.write(f"🟢 Veículo A")
            st.write(df_carro.loc[ultimo_indice, "Destino"])
            st.image("img/veiculoA.png",width=130)
            st.write(f'{df_carro.loc[ultimo_indice, "Motorista:"]}')


                
        else:
            st.write(f"🟠 Veículo A")
            st.write(df_carro.loc[ultimo_indice, "Destino"])
            st.image("img/stradA.png", width=130)
            st.write(f'{df_carro.loc[ultimo_indice, "Motorista:"]}')


            
# -----------------------------------------------------------------------------------------------------------

# Carro B status 
        df_carro = df.query('Veículo == "Veículo B"')

        contagem_saidas1 = df_carro.shape[0]

        with cardb:
            ultimo_indice = df_carro.index.max()

            if contagem_saidas1 % 2 == 0:
                st.write(f"🟢 Veículo B")
                st.write(df_carro.loc[ultimo_indice, "Destino"])
                st.image("img/veiculoB.png",width=130)
                st.write(f'{df_carro.loc[ultimo_indice, "Motorista:"]}')
                

            else:
                st.write(f"🟠 Veíuclo B")
                st.write(df_carro.loc[ultimo_indice, "Destino"])
                st.image("img/veiculoB.png", width=130)
                st.write(f'{df_carro.loc[ultimo_indice, "Motorista:"]}')


# -----------------------------------------------------------------------------------------------------------

# carro 3 status   
        df_carro = df.query('Veículo == "Veículo C"')

        contagem_saidas2 = df_carro.shape[0]

        with cardc:

            ultimo_indice = df_carro.index.max()

            if contagem_saidas2 % 2 == 0:
                st.write(f"🟢 Veículo C")
                st.write(df_carro.loc[ultimo_indice, "Destino"])
                st.image("img/veiculoC.png",width=130)
                st.write(f'{df_carro.loc[ultimo_indice, "Motorista:"]}')


            else:
                st.write(f"🟠 Veículo C")
                st.write(df_carro.loc[ultimo_indice, "Destino"])
                st.image("img/veiculoC.png", width=130)
                st.write(f'{df_carro.loc[ultimo_indice, "Motorista:"]}')


# -----------------------------------------------------------------------------------------------------------

# carro D status   
        df_carro = df.query('Veículo == "Veículo D"')

        contagem_saidas2 = df_carro.shape[0]

        with cardd:

            ultimo_indice = df_carro.index.max()


            if contagem_saidas2 % 2 == 0:
                st.write(f"🟢 Veículo D")
                st.write(df_carro.loc[ultimo_indice, "Destino"])
                st.image("img/veiculoD.png",width=130)
                st.write(f'{df_carro.loc[ultimo_indice, "Motorista:"]}')


            else:
                st.write("🟠 Veículo D")
                st.write(df_carro.loc[ultimo_indice, "Destino"])
                st.image("img/veiculoD.png", width=130)
                st.write(f'{df_carro.loc[ultimo_indice, "Motorista:"]}')


# -----------------------------------------------------------------------------------------------------------
# carro 5 status   

        df_carro = df.query('Veículo == "Veículo E"')

        contagem_saidas2 = df_carro.shape[0]

        with carde:

            ultimo_indice = df_carro.index.max()


            if contagem_saidas2 % 2 == 0:
                st.write(f"🟢 Veículo E")
                st.write(df_carro.loc[ultimo_indice, "Destino"])
                st.image("img/veiculoE.png",width=180)
                st.write(f'{df_carro.loc[ultimo_indice, "Motorista:"]}')


            else:
                st.write(f"🟠 Veículo E")
                st.write(df_carro.loc[ultimo_indice, "Destino"])
                st.image("img/veiculoE.png", width=180)
                st.write(f'{df_carro.loc[ultimo_indice, "Motorista:"]}')


# -----------------------------------------------------------------------------------------------------------


    with tab2:
    
        df["classificar"] = df["Data"] + " " + df["Hora"]

        df["id"] = df['classificar'].rank()

        df.set_index = df["id"]

        df = df.sort_values(by="id",ascending=True)

        df['Km'] = df["Km"].replace(".","").replace(",","")

        lista_carros = df_Veiculos

        filter_veiculos = st.multiselect("carros",df_Veiculos,default=lista_carros)

        df_filtro = df.query('Veículo == @filter_veiculos')

        df_filtro = df_filtro.sort_index(ascending=False)
        
        df_filtro = df_filtro.drop(columns="id")
                
        st.dataframe(df_filtro,use_container_width=True,hide_index=True)
     
        df_rua = df.query('Tipo == "Entrada"')

        df_rua = df.shape[0]

        contagem_rua = df_rua % 2
        


# -----------------------------------------------------------------------------------------------------------

# METRICAS

    with card1:
        st.metric("QTD VEÍCULOS", f'🚛 {qtd_Veiculos}')

    
    with card2:
        
        st.metric("QTD RUA", f'🟠 {rua}')

    with card5:
        st.metric("CONDUTORES REGISTRADOS", f'👨‍✈️ {qtd_motoristas}')
        
    with card4:
        st.metric("QTD VIAGENS", f'🏁 {df_qtd_viagens}')

    with card3:
        st.metric("NO PÁTIO",f' 🟢{patio}')


# ----------------------------------------------------------------------------------
#atualizar dados

if st.button("🔄 Atualizar"):
    st.cache_data.clear()
    st.rerun()

# ----------------------------------------------------------------------------------
#estilizacao


top = """
            <style>
            [Data-testid="stApp"]
            {
            top: -4vw;

            }
            </style>
            """

st.markdown(top, unsafe_allow_html=True)  


# ----------------------------------------------------------------------------------

borda = """
            <style>
            [Data-testid="stColumn"]
            {
            background-color: #252629;
            border-radius: 15px;
            padding: 10px;
            text-align: center;
            opacity: 100%;
            box-shadow: 5px 5px 10px 0px rgba(0, 0, 0, 0.5); 
            }
            </style>
            """

st.markdown(borda, unsafe_allow_html=True)  

# ----------------------------------------------------------------------------------

style1 = """
            <style>
            [Data-testid="stMetricLabel"]
            {
            border-radius: 15px;
            padding: 10px;
            text-align: center;
            }
            </style>
            """

st.markdown(style1, unsafe_allow_html=True) 


# ----------------------------------------------------------------------------------

style2 = """
            <style>
            [Data-testid="stHeader"]
            {
            display: none;
            }
            </style>
            """
st.markdown(style2, unsafe_allow_html=True) 

# ----------------------------------------------------------------------------------

style3 = """
        <style>
        [Data-testid="stElementToolbarButton"]
        {
        display: none;
        }
       </style>
        """
st.markdown(style3, unsafe_allow_html=True) 

# ----------------------------------------------------------------------------------

style4 = """
    <style>
    [Data-testid="stFullScreenFrame"]
    {
    display: flex;
    justify-content: center;
    }
    </style>
"""
st.markdown(style4, unsafe_allow_html=True) 

# ----------------------------------------------------------------------------------
style5 = """
    <style>
    [data-testid="stMarkdownContainer"]
    {
    font-weight: bold;
    }
    </style>
"""
st.markdown(style5, unsafe_allow_html=True) 
# ----------------------------------------------------------------------------------

style6 = """
            <style>
            [Data-testid="stMetricValue"]
            {
            color: #3885CC;
            }
            </style>
            """

st.markdown(style6, unsafe_allow_html=True) 
