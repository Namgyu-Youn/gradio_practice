import gradio as gr
import export

""" [Environment]
- 다양한 환경 변수를 설정할 수 있다.
- Port, Flag,
"""

export GRADIO_FLAGGING_MODE="never" # Turn off flag option
export GRADIO_SERVER_PORT=8000 # Port 지정
export GRADIO_CACHE_MODE="lazy" # 캐시 파일의 생성 여부 조정 (default="eager")