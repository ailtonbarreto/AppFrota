import streamlit as st
import pandas as pd
import datetime as dt
import gspread as gs
from gspread import worksheet
import pytz

# ---------------------------------------------------------------------------------------------
# layout

st.set_page_config(page_title="Controle de Frota",layout="wide",initial_sidebar_state="collapsed",page_icon="🚛")


with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html = True)

st.image('img/header.png',width=1000)

# ---------------------------------------------------------------------------------------------
# Dataframe principal
@st.cache_data
def load_viagens():
    gc = gs.service_account("credencial.json")
    url = 'https://docs.google.com/spreadsheets/d/11tgA-emVoqMda7Y2zBKNStSbBVHqK887G6cx57AKH_c/edit?usp=sharing'
    sh = gc.open_by_url(url)
    ws = sh.get_worksheet(0)
    planilha = ws.get_all_values()
    df = pd.DataFrame(planilha[1:], columns=planilha[0])
    return df


df = load_viagens()

df[["Data", "Hora"]] = df["Carimbo de data/hora"].str.split(" ", expand=True)

df["Data"] = pd.to_datetime(df["Data"])

df = df.drop(columns="Carimbo de data/hora")

df["Ano"] = df["Data"].dt.year
df["Mês"] = df["Data"].dt.month
df['Data'] = df['Data'].dt.strftime('%d/%m/%Y')



# ---------------------------------------------------------------------------------------------
# layout

coltitile, = st.columns(1)



# ---------------------------------------------------------------------------------------------
# Dataframe viagens

viagens = df

# ---------------------------------------------------------------------------------------------
# Dataframe motoristas

df_motoristas = df["Motorista:"].unique()

df_Veiculos = df["Veículo:"].unique()


# # ---------------------------------------------------------------------------------------------

# df_tipo = df.groupby("Veiculo")["Tipo"].value_counts().reset_index()

# df_tipo = df_tipo.groupby("Veiculo")["count"].sum().reset_index()

# df_tipo["disp"] = df_tipo["count"].apply(lambda x: x % 2)

# rua = (df_tipo['disp'] == 1).sum()

# df_status = df_tipo

# df_status["status"] = df_status["disp"].replace(1,"Rua").replace(0,"Pátio")

# df_status = df_status.drop(columns=["count","disp"])

# max_date = df['Data'].max()

# # max_date.strftime('%Y-%m-%d')




# # ---------------------------------------------------------------------------------------------

# # cards

# df_qtd_viagens = df.query('Tipo == "Saída"')

# df_qtd_viagens = df_qtd_viagens["Tipo"].count()


# # -----------------------------------------------------------------------------------------------------------


# df_km_rodados = df.query('Tipo == "Entrada"')

# df_km_rodados = df_km_rodados["Km"].sum()

# # -----------------------------------------------------------------------------------------------------------

# qtd_motoristas = df_motoristas.shape[0]

# qtd_Veiculos = df_Veiculos.shape[0]

# patio = qtd_Veiculos - rua

# # -----------------------------------------------------------------------------------------------------------

# carros_disp = df.query('Tipo == "Saída"')

# carros_disp = carros_disp["Veiculo"].unique()

# carros_disp = carros_disp.shape[0]


# # -----------------------------------------------------------------------------------------------------------
# # VIAGENS

# with tab1:

#     card1, card2, card3, card4, card5 = st.columns(5)

    

#     # carro 2 status
#     with tab1:

#         st.subheader("Disponibilidade da Frota", anchor=False)  

#         card6, card7, card8, card9, card11 = st.columns(5)

#         st.subheader("Registros", anchor=False)

#         df_carro2 = df.query('Veiculo == "Strada"')

#         contagem_saidas2 = df_carro2.shape[0]

#         with card6:
#             ultimo_indice = df_carro2.index.max()

#             if contagem_saidas2 % 2 == 0:
#                 st.write(f"🟢 STRADA")
#                 st.write(df_carro2.loc[ultimo_indice, "Destino"])
#                 st.image("img/strada.png",width=130)
#                 st.write(f'{df_carro2.loc[ultimo_indice, "Motorista"]} Entregou')


                
#             else:
#                 st.write(f"🟠 STRADA")
#                 st.write(df_carro2.loc[ultimo_indice, "Destino"])
#                 st.image("img/strada.png", width=130)
#                 st.write(f'{df_carro2.loc[ultimo_indice, "Motorista"]} Pegou')


            
# # -----------------------------------------------------------------------------------------------------------

# # Carro 1 status 
#         df_carro1 = df.query('Veiculo == "Gol Branco"')

#         contagem_saidas1 = df_carro1.shape[0]

#         with card11:
#             ultimo_indice = df_carro1.index.max()

#             if contagem_saidas1 % 2 == 0:
#                 st.write(f"🟢 GOL")
#                 st.write(df_carro1.loc[ultimo_indice, "Destino"])
#                 st.image("img/gol.png",width=130)
#                 st.write(f'{df_carro1.loc[ultimo_indice, "Motorista"]} Entregou')
                

#             else:
#                 st.write(f"🟠 GOL")
#                 st.write(df_carro1.loc[ultimo_indice, "Destino"])
#                 st.image("img/gol.png", width=130)
#                 st.write(f'{df_carro1.loc[ultimo_indice, "Motorista"]} Pegou')


# # -----------------------------------------------------------------------------------------------------------

# # carro 3 status   
#         df_carro2 = df.query('Veiculo == "Caminhão Branco Pequeno"')

#         contagem_saidas2 = df_carro2.shape[0]

#         with card7:

#             ultimo_indice = df_carro2.index.max()

#             if contagem_saidas2 % 2 == 0:
#                 st.write(f"🟢 CAMINHÃO BRANCO")
#                 st.write(df_carro2.loc[ultimo_indice, "Destino"])
#                 st.image("img/caminhabranco.png",width=130)
#                 st.write(f'{df_carro2.loc[ultimo_indice, "Motorista"]} Entregou')


#             else:
#                 st.write(f" 🟠CAMINHÃO BRANCO")
#                 st.write(df_carro2.loc[ultimo_indice, "Destino"])
#                 st.image("img/caminhabranco.png", width=130)
#                 st.write(f'{df_carro2.loc[ultimo_indice, "Motorista"]} Pegou')


# # -----------------------------------------------------------------------------------------------------------

# # carro 4 status   
#         df_carro2 = df.query('Veiculo == "Caminhão Branco Thór"')

#         contagem_saidas2 = df_carro2.shape[0]

#         with card8:

#             ultimo_indice = df_carro2.index.max()


#             if contagem_saidas2 % 2 == 0:
#                 st.write(f"🟢 THÓR")
#                 st.write(df_carro2.loc[ultimo_indice, "Destino"])
#                 st.image("img/thor.png",width=130)
#                 st.write(f'{df_carro2.loc[ultimo_indice, "Motorista"]} Entregou')


#             else:
#                 st.write("🟠 THÓR")
#                 st.write(df_carro2.loc[ultimo_indice, "Destino"])
#                 st.image("img/thor.png", width=130)
#                 st.write(f'{df_carro2.loc[ultimo_indice, "Motorista"]} Pegou')


# # -----------------------------------------------------------------------------------------------------------
# # carro 5 status   

#         df_carro2 = df.query('Veiculo == "Caminhão Vermelho"')

#         contagem_saidas2 = df_carro2.shape[0]

#         with card9:

#             ultimo_indice = df_carro2.index.max()


#             if contagem_saidas2 % 2 == 0:
#                 st.write(f"🟢 CAMINHÃO VERMELHO")
#                 st.write(df_carro2.loc[ultimo_indice, "Destino"])
#                 st.image("img/vermelho.png",width=130)
#                 st.write(f'{df_carro2.loc[ultimo_indice, "Motorista"]} Entregou')



            
#             else:
#                 st.write(f" 🟠CAMINHÃO VERMELHO")
#                 st.write(df_carro2.loc[ultimo_indice, "Destino"])
#                 st.image("img/vermelho.png", width=130)
#                 st.write(f'{df_carro2.loc[ultimo_indice, "Motorista"]} Pegou')




#     col6, = st.columns(1)
    
# # -----------------------------------------------------------------------------------------------------------

#     with col6:
    
#         df["classificar"] = df["Data"] + " " + df["Hora"]

#         df["id"] = df['classificar'].rank()-1

#         df.set_index = df["id"]

#         df = df.sort_values(by="id",ascending=True)

#         df['Km'] = df["Km"].replace(".","").replace(",","")

#         df = df.drop(columns=["id","Reporte de Danos","Vistoria","classificar"])

#         lista_carros = df_Veiculos["Veiculo"].unique()

#         filter_veiculos = st.multiselect("carros",df_Veiculos["Veiculo"].unique(),default=lista_carros)

#         df_filtro = df.query('Veiculo == @filter_veiculos')

#         df_filtro = df_filtro.sort_index(ascending=False)
        
#         st.dataframe(df_filtro,use_container_width=True,hide_index=False)
     
#         df_rua = df.query('Tipo == "Entrada"')

#         df_rua = df.shape[0]

#         contagem_rua = df_rua % 2


# # -----------------------------------------------------------------------------------------------------------

# # METRICAS

#     with card1:
#         st.metric("QTD VEÍCULOS", f'🚚 {qtd_Veiculos}')

    
#     with card2:
        
#         st.metric("QTD RUA", f'🟠 {rua}')

#     with card5:
#         st.metric("CONDUTORES REGISTRADOS", f'👨‍✈️ {qtd_motoristas}')
        
#     with card4:
#         st.metric("QTD VIAGENS", f'🏁 {df_qtd_viagens}')

#     with card3:
#         st.metric("NO PÁTIO",f' 🟢{patio}')

# # -----------------------------------------------------------------------------------------------------------
# # REGISTRAR

# with tab2:

#     col1, = st.columns(1)
    
#     with col1:
#         st.subheader("Registrar Movimentação",anchor=False)  
#         coltipo, = st.columns(1)
#         cola, colb = st.columns(2)
#         colc, cold = st.columns(2)
#         cole, colf = st.columns(2)
#         colg, = st.columns(1)


#     with col1:

#         with coltipo:
#             tipo = st.selectbox("Tipo",["Entrada","Saída"])

#         with colb:
#             motorista = st.selectbox("Motorista",df_motoristas["Motorista"].unique())

#         with cola:
#             Veiculo = st.selectbox("Veiculo",df_Veiculos["Veiculo"].unique())

#         with colc:
#             date = st.date_input("Data",format="DD/MM/YYYY")

#         with cold:

#             fuso_horario = pytz.timezone("America/Sao_Paulo")

#             carimbo = dt.datetime.now(fuso_horario).hour

#             hr = dt.datetime.now().hour - 3 
            
#             hora_atual = dt.datetime.now(fuso_horario).time()

#             hora = st.text_input("horário")

#         with cole:

#             hr = dt.datetime.now(fuso_horario).hour

#             min = f"{dt.datetime.now().minute:02}"

#             hora = f'{hr}:{min}'

#             dfcarro = df.query('Veiculo == @Veiculo & Tipo == "Entrada"').reset_index()

#             indicecarro = dfcarro["Km"].max()

#             if tipo == "Entrada":
#                 quilometragem = st.number_input("Kilometragem", format="%1.0f")
#                 destino = "Focal Matriz"
#                 with colf:
#                     vistoria = st.selectbox("Vistoria",["Ok","COM DANO"])    
#             else:
#                 destino = st.text_input("Destino")
#                 quilometragem = indicecarro
#                 vistoria = "Ok"   
#             with colg:
#                 if vistoria == "COM DANO":
#                     report = st.text_area("Descrever")
#                 else:
#                     report = ""
            

#         if st.button("REGISTRAR"):

#             gc = gs.service_account("credencial.json")
            
#             url = 'https://docs.google.com/spreadsheets/d/11tgA-emVoqMda7Y2zBKNStSbBVHqK887G6cx57AKH_c/edit?usp=sharing'
#             sh = gc.open_by_url(url)
#             Worksheet = sh.get_worksheet(0)

#             date = date.strftime("%d/%m/%Y")
       
#             nova_linha = [motorista, Veiculo, date, tipo, hora,quilometragem, destino,vistoria,report]

#             print(nova_linha)

#             Worksheet.append_row(nova_linha)
            
#             st.success("Movimentação salva!")
        
#             st.cache_data.clear()
            
#             st.rerun()


# # ---------------------------------------------------------------------------------
# #EXCLUIR REGISTRO

# with tab3:

#     st.subheader("Filtrar",anchor=False)

#     col1, = st.columns(1)

#     st.subheader("Escolher Linha",anchor=False)

#     col2, = st.columns(1)

#     with col1:
        
#         st.write(max_date)

#         data_delete = st.date_input("Data da Viagem",format="DD/MM/YYYY",value="2025-01-17")

#         data_delete = data_delete.strftime("%d/%m/%Y")
        
#         df_delete = viagens.query('Data == @data_delete')

#         st.dataframe(df_delete,use_container_width=True)

#     with col2:

#         row_delete = st.selectbox("Linha", df_delete.index)

#         row = df_delete.query('index == @row_delete')

#         st.dataframe(row,use_container_width=True)

#         row_index = row.index[0]

        
#         if st.button("Excluir Viagem"):

#             gc = gs.service_account("credencial.json")

#             url = 'https://docs.google.com/spreadsheets/d/11tgA-emVoqMda7Y2zBKNStSbBVHqK887G6cx57AKH_c/edit?usp=sharing'

#             sh = gc.open_by_url(url)

#             Worksheet = sh.get_worksheet(0)

#             linha_deletar = row_index + 2

#             Worksheet.delete_rows(int(linha_deletar))
            
#             st.success("Registro Excluído")
        
#             st.cache_data.clear()
            
#             st.rerun()



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
            background-color: #ffffff;
            border-radius: 15px;
            padding: 10px;
            text-align: center;
            color: #3885CC;
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
            background-color: #ffffff;
            border-radius: 15px;
            padding: 10px;
            text-align: center;
            color: #3885CC;
            opacity: 100%;
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
