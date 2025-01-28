import streamlit as st
import pandas as pd

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
        st.metric("QTD Veículos", f'🚌 {qtd_Veiculos}')

    
    with card2:
        
        st.metric("Estrada", f'🟢 {rua}')

    with card5:
        st.metric("QTD Motoristas", f'👨‍✈️ {qtd_motoristas}')
        
    with card4:
        st.metric("QTD Viagens", f'🏁 {df_qtd_viagens}')

    with card3:
        st.metric("Garagem",f'🟠 {patio}')





# Simulação de dados da frota
data = {
    "Veículo": ["Ônibus A", "Ônibus B", "Ônibus C"],
    "Localização": ["Terminal 1", "Em trânsito", "Terminal 2"],
    "Motorista": ["Carlos", "Ana", "João"],
    "Status": ["Disponível", "Em serviço", "Manutenção"],
    "Consumo (L/100km)": [30, 35, 40]
}

# -------------------------------------------------------------------------------------

df = pd.DataFrame(data)



map_data = pd.DataFrame({
    "lat": [-23.5505, -23.5629, -23.5740],
    "lon": [-46.6333, -46.6465, -46.6400],
    "Veículo": ["Ônibus A", "Ônibus B", "Ônibus C"]
})
with colmap:
    st.map(map_data)


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


