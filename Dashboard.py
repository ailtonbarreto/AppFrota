import streamlit as st
import pandas as pd
import pydeck as pdk
import mysql.connector



# ---------------------------------------------------------------------------------------------
# layout

st.set_page_config(page_title="Gestão de Frota",layout="wide",initial_sidebar_state="collapsed",page_icon="🚛")


with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html = True)

st.image('img/header.png',width=1000)



conn = mysql.connector.connect(
    host="srv1073.hstgr.io",        # ou o IP do servidor
    user="u771906953_barreto",      # seu nome de usuário no banco de dados
    password="MQPj3:6GY_hFfjA",    # sua senha do banco de dados
    database="u771906953_barreto"     # nome do banco de dados
)

# Consulta SQL
query = "SELECT * FROM TB_VIAGENS"

@st.cache_data
def load_data():
    df = pd.read_sql(query, conn)
    return df

df = load_data()


df["Data"] = pd.to_datetime(df["Data"])

df["Ano"] = df["Data"].dt.year
df["Mês"] = df["Data"].dt.month
df['Data'] = df['Data'].dt.strftime('%d/%m/%Y')






# ---------------------------------------------------------------------------------------------
# DataframeMotoristas

df_motoristas = df["Motorista"].unique()

df_Veiculos = df["Veículo"].unique()


# # ---------------------------------------------------------------------------------------------

df_tipo = df.groupby("Veículo")["Tipo"].value_counts().reset_index()

df_tipo = df_tipo.groupby("Veículo")["count"].sum().reset_index()

df_tipo["disp"] = df_tipo["count"].apply(lambda x: x % 2)

rua = (df_tipo['disp'] == 1).sum()


df["Latitude"] = df["Latitude"].astype(float)
df["Longitude"] = df["Longitude"].astype(float)


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



card1, card2, card3, card4, card5 = st.columns(5)
    
st.divider()
    
st.subheader("Status Por Veículo", anchor=False)
    
# carro A status
  
carda, cardb, cardc, cardd, carde = st.columns(5)
cardf, cardg, cardh, cardi, cardj = st.columns(5)
    
st.divider()
    
colmap, = st.columns(1)

col_df, = st.columns(1)


df_carro = df.query('Veículo == "Veículo A"')

contagem_saidas2 = df_carro.shape[0]

with carda:
    ultimo_indice = df_carro.index.max()

    if contagem_saidas2 % 2 == 0:
        st.write(f"🟡 Veículo A")
        st.write("Garagem")
        st.image("img/Busout.png",width=180)
        st.write(f'{df_carro.loc[ultimo_indice, "Motorista"]}')

   
    else:
        st.write(f"🟢 Veículo A")
        st.write(f'{df_carro.loc[ultimo_indice, "Origem"]}  -  {df_carro.loc[ultimo_indice, "Destino"]}')
        st.image("img/Bus.png", width=180)
        st.write(f'{df_carro.loc[ultimo_indice, "Motorista"]}')


            
# -----------------------------------------------------------------------------------------------------------

# Carro B status 
df_carro = df.query('Veículo == "Veículo B"')

contagem_saidas1 = df_carro.shape[0]

with cardb:
    ultimo_indice = df_carro.index.max()

    if contagem_saidas1 % 2 == 0:
        st.write(f"🟡 Veículo B")
        st.write("Garagem")
        st.image("img/Busout.png",width=180)
        st.write(f'{df_carro.loc[ultimo_indice, "Motorista"]}')
        

    else:
        st.write(f"🟢 Veíuclo B")
        st.write(f'{df_carro.loc[ultimo_indice, "Origem"]}  -  {df_carro.loc[ultimo_indice, "Destino"]}')
        st.image("img/Bus.png", width=180)
        st.write(f'{df_carro.loc[ultimo_indice, "Motorista"]}')


# -----------------------------------------------------------------------------------------------------------

# carro 3 status   
df_carro = df.query('Veículo == "Veículo C"')

contagem_saidas2 = df_carro.shape[0]

with cardc:

    ultimo_indice = df_carro.index.max()

    if contagem_saidas2 % 2 == 0:
        st.write(f"🟡 Veículo C")
        st.write("Garagem")
        st.image("img/Busout.png",width=180)
        st.write(f'{df_carro.loc[ultimo_indice, "Motorista"]}')


    else:
        st.write(f"🟢 Veículo C")
        st.write(f'{df_carro.loc[ultimo_indice, "Origem"]}  -  {df_carro.loc[ultimo_indice, "Destino"]}')
        st.image("img/Bus.png", width=180)
        st.write(f'{df_carro.loc[ultimo_indice, "Motorista"]}')


# -----------------------------------------------------------------------------------------------------------

# carro D status   
df_carro = df.query('Veículo == "Veículo D"')

contagem_saidas2 = df_carro.shape[0]

with cardd:

    ultimo_indice = df_carro.index.max()


    if contagem_saidas2 % 2 == 0:
        st.write(f"🟡 Veículo D")
        st.write("Garagem")
        st.image("img/Busout.png",width=180)
        st.write(f'{df_carro.loc[ultimo_indice, "Motorista"]}')


    else:
        st.write("🟢 Veículo D")
        st.write(f'{df_carro.loc[ultimo_indice, "Origem"]}  -  {df_carro.loc[ultimo_indice, "Destino"]}')
        st.image("img/Bus.png", width=180)
        st.write(f'{df_carro.loc[ultimo_indice, "Motorista"]}')


# -----------------------------------------------------------------------------------------------------------
# carro 5 status   

df_carro = df.query('Veículo == "Veículo E"')

contagem_saidas2 = df_carro.shape[0]

with carde:

    ultimo_indice = df_carro.index.max()


    if contagem_saidas2 % 2 == 0:
        st.write(f"🟡 Veículo E")
        st.write("Garagem")
        st.image("img/Busout.png",width=180)
        st.write(f'{df_carro.loc[ultimo_indice, "Motorista"]}')


    else:
        st.write(f"🟢 Veículo E")
        st.write(f'{df_carro.loc[ultimo_indice, "Origem"]}  -  {df_carro.loc[ultimo_indice, "Destino"]}')
        st.image("img/Bus.png", width=180)
        st.write(f'{df_carro.loc[ultimo_indice, "Motorista"]}')
        
# -----------------------------------------------------------------------------------------------------------
# carro 6 status   

df_carro = df.query('Veículo == "Veículo F"')

contagem_saidas2 = df_carro.shape[0]

with cardf:

    ultimo_indice = df_carro.index.max()


    if contagem_saidas2 % 2 == 0:
        st.write(f"🟡 Veículo F")
        st.write("Garagem")
        st.image("img/Busout.png",width=180)
        st.write(f'{df_carro.loc[ultimo_indice, "Motorista"]}')


    else:
        st.write(f"🟢 Veículo F")
        st.write(f'{df_carro.loc[ultimo_indice, "Origem"]}  -  {df_carro.loc[ultimo_indice, "Destino"]}')
        st.image("img/Bus.png", width=180)
        st.write(f'{df_carro.loc[ultimo_indice, "Motorista"]}')

                


# -----------------------------------------------------------------------------------------------------------
# carro 7 status   

df_carro = df.query('Veículo == "Veículo G"')

contagem_saidas2 = df_carro.shape[0]

with cardg:

    ultimo_indice = df_carro.index.max()


    if contagem_saidas2 % 2 == 0:
        st.write(f"🟡 Veículo G")
        st.write("Garagem")
        st.image("img/Busout.png",width=180)
        st.write(f'{df_carro.loc[ultimo_indice, "Motorista"]}')


    else:
        st.write(f"🟢 Veículo G")
        st.write(f'{df_carro.loc[ultimo_indice, "Origem"]}  -  {df_carro.loc[ultimo_indice, "Destino"]}')
        st.image("img/Bus.png", width=180)
        st.write(f'{df_carro.loc[ultimo_indice, "Motorista"]}')


# -----------------------------------------------------------------------------------------------------------
# carro 8 status   

df_carro = df.query('Veículo == "Veículo H"')

contagem_saidas2 = df_carro.shape[0]

with cardh:

    ultimo_indice = df_carro.index.max()


    if contagem_saidas2 % 2 == 0:
        st.write(f"🟡 Veículo H")
        st.write("Garagem")
        st.image("img/Busout.png",width=180)
        st.write(f'{df_carro.loc[ultimo_indice, "Motorista"]}')


    else:
        st.write(f"🟢 Veículo H")
        st.write(f'{df_carro.loc[ultimo_indice, "Origem"]}  -  {df_carro.loc[ultimo_indice, "Destino"]}')
        st.image("img/Bus.png", width=180)
        st.write(f'{df_carro.loc[ultimo_indice, "Motorista"]}')

# -----------------------------------------------------------------------------------------------------------
# carro 9 status   

df_carro = df.query('Veículo == "Veículo I"')

contagem_saidas2 = df_carro.shape[0]

with cardi:

    ultimo_indice = df_carro.index.max()


    if contagem_saidas2 % 2 == 0:
        st.write(f"🟡 Veículo I")
        st.write("Garagem")
        st.image("img/Busout.png",width=180)
        st.write(f'{df_carro.loc[ultimo_indice, "Motorista"]}')


    else:
        st.write(f"🟢 Veículo I")
        st.write(f'{df_carro.loc[ultimo_indice, "Origem"]}  -  {df_carro.loc[ultimo_indice, "Destino"]}')
        st.image("img/Bus.png", width=180)
        st.write(f'{df_carro.loc[ultimo_indice, "Motorista"]}')

# -----------------------------------------------------------------------------------------------------------
# carro 8 status   

df_carro = df.query('Veículo == "Veículo J"')

contagem_saidas2 = df_carro.shape[0]

with cardj:

    ultimo_indice = df_carro.index.max()


    if contagem_saidas2 % 2 == 0:
        st.write(f"🟡 Veículo J")
        st.write("Garagem")
        st.image("img/Busout.png",width=180)
        st.write(f'{df_carro.loc[ultimo_indice, "Motorista"]}')


    else:
        st.write(f"🟢 Veículo J")
        st.write(f'{df_carro.loc[ultimo_indice, "Origem"]}  -  {df_carro.loc[ultimo_indice, "Destino"]}')
        st.image("img/Bus.png", width=180)
        st.write(f'{df_carro.loc[ultimo_indice, "Motorista"]}')



# -----------------------------------------------------------------------------------------------------------


df["classificar"] = df["Data"]


lista_carros = df_Veiculos

df_rua = df.query('Tipo == "Entrada"')

df_rua = df.shape[0]

contagem_rua = df_rua % 2

soma_km = df["km"].sum()

df = df.loc[df.reset_index().drop_duplicates(subset='Veículo', keep='last').set_index("index").index]

# -----------------------------------------------------------------------------------------------------------

# METRICAS

with card1:
    st.metric("QTD Veículos", f'🚌 {qtd_Veiculos}')


with card2:

    st.metric("Estrada", f'🟢 {rua}')

with card5:
    st.metric("Km Rodados", f'🧭 {soma_km:,.2f}'.replace(",", "X").replace(".", ",").replace("X", "."))




with card4:
    st.metric("QTD Viagens", f'🏁 {df_qtd_viagens}')

with card3:
    st.metric("Garagem",f'🟡 {patio}')


# -------------------------------------------------------------------------------------

layer = pdk.Layer(
    "ScatterplotLayer",
    df,
    get_position=["Longitude", "Latitude"],  # Ordem: Lon, Lat
    get_radius=20000,
    get_fill_color=[0, 122, 255, 160],
    opacity=0.8,
    pickable=True
)


view_state = pdk.ViewState(
    latitude=df["Latitude"].mean(),
    longitude=df["Longitude"].mean(),
    zoom=4,
    pitch=0
)

tooltip = {
    "html": "{Veículo} - {Origem} ➝ {Destino}",
    "style": {"backgroundColor": "black", "color": "white"}
}


with colmap:
    st.write("Última Posição Conhecida")
    st.pydeck_chart(pdk.Deck(layers=[layer],initial_view_state=view_state,tooltip=tooltip))
    st.empty()
    
    
    
with col_df:
    st.write("Linhas")
    df = df[["Veículo","Origem","Destino"]]
    st.dataframe(df,use_container_width=True,hide_index=True)


# ----------------------------------------------------------------------------------
#atualizar dados

if st.button("🔄 Atualizar"):
    st.cache_data.clear()
    st.rerun()

# ----------------------------------------------------------------------------------
#estilizacao



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

hide_st_style = """
            <style>
            header {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

