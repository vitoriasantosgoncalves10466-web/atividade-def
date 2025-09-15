import streamlit as st

st.set_page_config(page_title="Atendimento Jurídico", page_icon="⚖️")
st.title("Atendimento Virtual - Escritório de Advocacia")

if "messages" not in st.session_state:
    st.session_state.messages = []


faq = {
     "Quais áreas do direito vocês atendem?": "Nosso escritório atua em Direito Trabalhista, Direito de Família, Direito Civil e Direito Empresarial.",
    "Qual é o horário de atendimento?": "Atendemos de segunda a sexta, das 09:00 às 18:00.",
    "Como agendar uma consulta?": "Você pode agendar uma consulta pelo telefone (61) 3333-2222 ou pelo WhatsApp no botão abaixo.",
    "Vocês oferecem consulta online?": "Sim, oferecemos consultas online por videochamada com agendamento prévio.",
    "Qual é o valor da consulta inicial?": "A primeira consulta tem valor fixo de R$ 300,00. Casos específicos podem ter orçamento personalizado.",
    "Onde fica o escritório?": "Estamos localizados na Av. Central, nº 456, Centro - Brasília/DF.",
    "Falar com advogado": "Você pode falar diretamente com um advogado pelo WhatsApp clicando no botão abaixo.",
    }
  
for msg in st.session_state.messages: 
    with st.chat_message(msg["role"]): #Pergunta antes dos dois pontos
        st.markdown(msg["content"]) #Função semelhante a um botao onde aparecerá as respostas

pergunta = st.chat_input("Digite sua pergunta: ") #Interação para digitar

#Mostrar botões de perguntas 
for key in faq.keys():
    if st.button(key):
        pergunta = key

if pergunta:
    resposta = faq.get(pergunta, "Desculpe não tenho uma resposta para essa pergunta. Um atendente poderá te ajudar melhor!")

    st.session_state.messages.append({"role": "user", "content": pergunta})
    st.session_state.messages.append({"role": "assistant", "content": resposta})

    with st.chat_message("user"):
        st.markdown(pergunta)
    with st.chat_message("assistant"):
        st.markdown(resposta)

    if pergunta == "Falar com advogado":
        whatsapp_url = "https://wa.me/6199898951"
        st.markdown(f"[📲Clique aqui para falar no Wpp] ({whatsapp_url})")
    