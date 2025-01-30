import streamlit as st
import pandas as pd
import pydeck as pdk
import folium
from streamlit_folium import st_folium

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

tab1, tab2 = st.tabs(["Disponibilidade","Formulário"])

    
with tab2:
    st.subheader("Link Para Preencher",anchor=False)
    st.image("img/qr.png")



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
    
    st.divider()
    
    st.subheader("Disponibilidade da Frota", anchor=False)
    
    # carro A status
  
    carda, cardb, cardc, cardd, carde = st.columns(5)
    cardf, cardg, cardh, cardi, cardj = st.columns(5)
    
    st.divider()
    
    st.subheader("Geolocalização",anchor=False)
    
    colmap,  = st.columns(1)

    df_carro = df.query('Veículo == "Veículo A"')

    contagem_saidas2 = df_carro.shape[0]

    with carda:
        ultimo_indice = df_carro.index.max()

        if contagem_saidas2 % 2 == 0:
            st.write(f"🟠 Veículo A")
            st.write(df_carro.loc[ultimo_indice, "Destino"])
            st.image("img/Busout.png",width=180)
            st.write(f'{df_carro.loc[ultimo_indice, "Motorista:"]}')

   
        else:
            st.write(f"🟢 Veículo A")
            st.write(df_carro.loc[ultimo_indice, "Destino"])
            st.image("img/Bus.png", width=180)
            st.write(f'{df_carro.loc[ultimo_indice, "Motorista:"]}')


            
# -----------------------------------------------------------------------------------------------------------

# Carro B status 
        df_carro = df.query('Veículo == "Veículo B"')

        contagem_saidas1 = df_carro.shape[0]

        with cardb:
            ultimo_indice = df_carro.index.max()

            if contagem_saidas1 % 2 == 0:
                st.write(f"🟠 Veículo B")
                st.write(df_carro.loc[ultimo_indice, "Destino"])
                st.image("img/Busout.png",width=180)
                st.write(f'{df_carro.loc[ultimo_indice, "Motorista:"]}')
                

            else:
                st.write(f"🟢 Veíuclo B")
                st.write(df_carro.loc[ultimo_indice, "Destino"])
                st.image("img/Bus.png", width=180)
                st.write(f'{df_carro.loc[ultimo_indice, "Motorista:"]}')


# -----------------------------------------------------------------------------------------------------------

# carro 3 status   
        df_carro = df.query('Veículo == "Veículo C"')

        contagem_saidas2 = df_carro.shape[0]

        with cardc:

            ultimo_indice = df_carro.index.max()

            if contagem_saidas2 % 2 == 0:
                st.write(f"🟠 Veículo C")
                st.write(df_carro.loc[ultimo_indice, "Destino"])
                st.image("img/Busout.png",width=180)
                st.write(f'{df_carro.loc[ultimo_indice, "Motorista:"]}')


            else:
                st.write(f"🟢 Veículo C")
                st.write(df_carro.loc[ultimo_indice, "Destino"])
                st.image("img/Bus.png", width=180)
                st.write(f'{df_carro.loc[ultimo_indice, "Motorista:"]}')


# -----------------------------------------------------------------------------------------------------------

# carro D status   
        df_carro = df.query('Veículo == "Veículo D"')

        contagem_saidas2 = df_carro.shape[0]

        with cardd:

            ultimo_indice = df_carro.index.max()


            if contagem_saidas2 % 2 == 0:
                st.write(f"🟠 Veículo D")
                st.write(df_carro.loc[ultimo_indice, "Destino"])
                st.image("img/Busout.png",width=180)
                st.write(f'{df_carro.loc[ultimo_indice, "Motorista:"]}')


            else:
                st.write("🟢 Veículo D")
                st.write(df_carro.loc[ultimo_indice, "Destino"])
                st.image("img/Bus.png", width=180)
                st.write(f'{df_carro.loc[ultimo_indice, "Motorista:"]}')


# -----------------------------------------------------------------------------------------------------------
# carro 5 status   

        df_carro = df.query('Veículo == "Veículo E"')

        contagem_saidas2 = df_carro.shape[0]

        with carde:

            ultimo_indice = df_carro.index.max()


            if contagem_saidas2 % 2 == 0:
                st.write(f"🟠 Veículo E")
                st.write(df_carro.loc[ultimo_indice, "Destino"])
                st.image("img/Busout.png",width=180)
                st.write(f'{df_carro.loc[ultimo_indice, "Motorista:"]}')


            else:
                st.write(f"🟢 Veículo E")
                st.write(df_carro.loc[ultimo_indice, "Destino"])
                st.image("img/Bus.png", width=180)
                st.write(f'{df_carro.loc[ultimo_indice, "Motorista:"]}')
                
# -----------------------------------------------------------------------------------------------------------
# carro 6 status   

        df_carro = df.query('Veículo == "Veículo F"')

        contagem_saidas2 = df_carro.shape[0]

        with cardf:

            ultimo_indice = df_carro.index.max()


            if contagem_saidas2 % 2 == 0:
                st.write(f"🟠 Veículo F")
                st.write(df_carro.loc[ultimo_indice, "Destino"])
                st.image("img/Busout.png",width=180)
                st.write(f'{df_carro.loc[ultimo_indice, "Motorista:"]}')


            else:
                st.write(f"🟢 Veículo F")
                st.write(df_carro.loc[ultimo_indice, "Destino"])
                st.image("img/Bus.png", width=180)
                st.write(f'{df_carro.loc[ultimo_indice, "Motorista:"]}')

                


# -----------------------------------------------------------------------------------------------------------
# carro 7 status   

        df_carro = df.query('Veículo == "Veículo G"')

        contagem_saidas2 = df_carro.shape[0]

        with cardg:

            ultimo_indice = df_carro.index.max()


            if contagem_saidas2 % 2 == 0:
                st.write(f"🟠 Veículo G")
                st.write(df_carro.loc[ultimo_indice, "Destino"])
                st.image("img/Busout.png",width=180)
                st.write(f'{df_carro.loc[ultimo_indice, "Motorista:"]}')


            else:
                st.write(f"🟢 Veículo G")
                st.write(df_carro.loc[ultimo_indice, "Destino"])
                st.image("img/Bus.png", width=180)
                st.write(f'{df_carro.loc[ultimo_indice, "Motorista:"]}')


# -----------------------------------------------------------------------------------------------------------
# carro 8 status   

        df_carro = df.query('Veículo == "Veículo H"')

        contagem_saidas2 = df_carro.shape[0]

        with cardh:

            ultimo_indice = df_carro.index.max()


            if contagem_saidas2 % 2 == 0:
                st.write(f"🟠 Veículo H")
                st.write(df_carro.loc[ultimo_indice, "Destino"])
                st.image("img/Busout.png",width=180)
                st.write(f'{df_carro.loc[ultimo_indice, "Motorista:"]}')


            else:
                st.write(f"🟢 Veículo H")
                st.write(df_carro.loc[ultimo_indice, "Destino"])
                st.image("img/Bus.png", width=180)
                st.write(f'{df_carro.loc[ultimo_indice, "Motorista:"]}')

# -----------------------------------------------------------------------------------------------------------
# carro 9 status   

        df_carro = df.query('Veículo == "Veículo I"')

        contagem_saidas2 = df_carro.shape[0]

        with cardi:

            ultimo_indice = df_carro.index.max()


            if contagem_saidas2 % 2 == 0:
                st.write(f"🟠 Veículo I")
                st.write(df_carro.loc[ultimo_indice, "Destino"])
                st.image("img/Busout.png",width=180)
                st.write(f'{df_carro.loc[ultimo_indice, "Motorista:"]}')


            else:
                st.write(f"🟢 Veículo I")
                st.write(df_carro.loc[ultimo_indice, "Destino"])
                st.image("img/Bus.png", width=180)
                st.write(f'{df_carro.loc[ultimo_indice, "Motorista:"]}')

# -----------------------------------------------------------------------------------------------------------
# carro 8 status   

        df_carro = df.query('Veículo == "Veículo J"')

        contagem_saidas2 = df_carro.shape[0]

        with cardj:

            ultimo_indice = df_carro.index.max()


            if contagem_saidas2 % 2 == 0:
                st.write(f"🟠 Veículo J")
                st.write(df_carro.loc[ultimo_indice, "Destino"])
                st.image("img/Busout.png",width=180)
                st.write(f'{df_carro.loc[ultimo_indice, "Motorista:"]}')


            else:
                st.write(f"🟢 Veículo J")
                st.write(df_carro.loc[ultimo_indice, "Destino"])
                st.image("img/Bus.png", width=180)
                st.write(f'{df_carro.loc[ultimo_indice, "Motorista:"]}')




# -----------------------------------------------------------------------------------------------------------



    
    df["classificar"] = df["Data"] + " " + df["Hora"]

    df["id"] = df['classificar'].rank()

    df.set_index = df["id"]

    df = df.sort_values(by="id",ascending=True)

    df['Km'] = df["Km"].replace(".","").replace(",","")

    lista_carros = df_Veiculos
        
    df_rua = df.query('Tipo == "Entrada"')

    df_rua = df.shape[0]

    contagem_rua = df_rua % 2
        


# -----------------------------------------------------------------------------------------------------------

# METRICAS

    with card1:
        st.metric("QTD Veículos", f'🚌 {qtd_Veiculos}')

    
    with card2:
        
        st.metric("Estrada", f'🟢 {rua}')

    with card5:
        st.metric("QTD Motoristas", f'👨‍✈️ {qtd_motoristas}')
        
    with card4:
        st.metric("QTD Viagens", f'🏁 {df_qtd_viagens}')

    with card3:
        st.metric("Garagem",f'🟠 {patio}')


df["Latitude"] = df["Latitude"].str.replace(",", ".", regex=False)
df["Longitude"] = df["Longitude"].str.replace(",", ".", regex=False)
# -------------------------------------------------------------------------------------

df["Latitude"] = df["Latitude"].astype(float)
df["Longitude"] = df["Longitude"].astype(float)


# map_data = {
#     "lat": df["Latitude"],
#     "lon": df["Longitude"],
#     "Veículo": df["Veículo"]
# }


# # Gerando o mapa com pydeck
# deck = pdk.Deck(
#     layers=[
#         pdk.Layer(
#             "ScatterplotLayer",
#             df,  # Dados
#             get_position=["Longitude", "Latitude"],
#             get_radius=30000,
#             get_color=[0, 0, 255],
#             pickable=True
#         )
#     ],
#     initial_view_state=pdk.ViewState(
#         latitude=df["Latitude"].mean(),
#         longitude=df["Longitude"].mean(),
#         zoom=6,
#         pitch=0
#     )
# )


# Criar um mapa centrado na primeira coordenada
mapa = folium.Map(location=[-23.567, -46.633], zoom_start=6)

# Lista de coordenadas representando a rota
rota = [
    [-23.5673865, -46.6333],
    [-22.0154, -43.1729],
    [-20.536097, -49.2730],
    [-22.73172683, -45.6723],
    [-25.432956, -47.3989]
]

# Adicionar a linha da rota no mapa
folium.PolyLine(rota, color="blue", weight=5, opacity=0.7).add_to(mapa)

# Adicionar marcadores nos pontos da rota
for lat, lon in rota:
    folium.Marker([lat, lon]).add_to(mapa)

# Exibir o mapa no Streamlit
st_folium(mapa, width=700, height=500)

















# -------------------------------------------------------------------------

with colmap:
    st.pydeck_chart(deck,use_container_width=True)

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

# ----------------------------------------------------------------------------------

style7 = """
            <style>
            [Data-testid="stElementContainer"]
            {
            text-align: center;
            }
            </style>
            """

st.markdown(style7, unsafe_allow_html=True) 


