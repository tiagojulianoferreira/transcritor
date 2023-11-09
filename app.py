import streamlit as st
from businessLogic import transcribeVideoOrchestrator
from businessLogic import transcribe_audio
from businessLogic import transcribe_audio_orchestrator

def open_buy_me_coffee():
    st.markdown('<script>document.getElementById("buy-me-coffee-btn").click();</script>',
                unsafe_allow_html=True)

def main():
    st.title("Video2Text - Transcritor de áudio em texto usando OpenAI Whisper")

    # # Embed the Buy Me a Coffee widget using the provided <script> tag
    # buy_me_coffee_script = """
    #     <script
    #         data-name="BMC-Widget"
    #         data-cfasync="false"
    #         src="https://cdnjs.buymeacoffee.com/1.0.0/widget.prod.min.js"
    #         data-id="hayerhans"
    #         data-description="If you like this, please consider supporting this work"
    #         data-message="If you like this, please consider supporting me!"
    #         data-color="#BD5FFF"
    #         data-position="Right"
    #         data-x_margin="18"
    #         data-y_margin="18">
    #     </script>
    # """
    # st.components.v1.html(buy_me_coffee_script)
    st.subheader("Não é um ChatGPT mas é honesto", divider='rainbow')
    st.write("Versão BETA - Não aguenta mais do 3-4 transcrições simultâneas. Nos testes, do Youtube levou cerca de 10-15 pra baixar e transcrever vídeos de 1h usando modelos base e small")
    # st.markdown(buy_me_coffee_script, unsafe_allow_html=True)

    # User input: model
    models = ["tiny", "base", "small", "medium", "large"]
    model = st.selectbox("Selecionar Modelo:", models)
    st.write(
        "Se você usar um modelo menor, ele será mais rápido, mas não tão preciso, enquanto um modelo maior será mais lento, mas mais preciso.")

    st.write("Você pode baixar e trascrever de um link do Youtube ou subir um arquivo de áudio a ser transcrito.")
    source = st.radio("Escolha:", ("YouTube Link", "Upload Áudio"))

    if source == "YouTube Link":
        # User input: YouTube URL
        url = st.text_input("Insira o YouTube Link:")
        if st.button("Transcribe"):
            if url:
                transcript = transcribeVideoOrchestrator(url, model)

                if transcript:
                    st.subheader("Transcrição:")
                    st.write(transcript)
                else:
                    st.error("Error occurred while transcribing.")
                    st.write("Please try again.")
    else:
        # User input: Upload Audio File
        audio_file = st.file_uploader("Upload arquivo de áudio (MP3, WAV, etc.):", type=["mp3", "wav"])
        if audio_file:
            if st.button("Transcrever"):
                transcript = transcribe_audio_orchestrator(audio_file, model)

                if transcript:
                    st.subheader("Transcrição:")
                    st.write(transcript)
                else:
                    st.error("Error occurred while transcribing.")
                    st.write("Please try again.")

    st.markdown('<div style="margin-top: 100px;"</div>', unsafe_allow_html=True)
    st.write("Inspirado no projeto https://github.com/XamHans/video-2-text")
    # st.write("Entre sua mensagem:")
    # user_message = st.text_area("Mensagem:")

    # st.markdown(f'<a href="mailto:suporte.ti.tub@ifsc.edu.br?subject=Video2Text-Help&body={user_message}">Enviar</a>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()

