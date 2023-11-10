# Trascritor de áudio em texto usando OpenAI Whisper
Esta aplicação transcreve áudio em texto usando a biblioteca OpenAI Whisper a partir de uma URL do Youtube ou do upload direto de arquivo de áudio.

## Tecnologias
- Python 3
- [Streamlit (GUI)](https://streamlit.io/)
- [openai-whisper](https://github.com/openai/whisper)
- Debian Linux

## Instale o ffmpeg no host
apt-get install ffmpeg

## Instalação
```shell
git clone https://github.com/tiagojulianoferreira/transcritor.git
cd transcritor/
pip3 install -r requirements.txt
streamlit run app.py
```
Abra http://localhost:8501 no seu navegador

# Help
Se você tiver algum problema, tente reinstalar o pytube.
```shell
pip uninstall pytube
pip uninstall pytube3
pip install pytube
```
Se você encontrar um erro onde streamlit não é reconhecido pelo seu terminal, tente este comando em seu terminal: export PATH="$HOME/.local/bin:$PATH"

Se você ainda tiver problemas, crie uma issue.

# Inspirado em

https://github.com/XamHans/video-2-text