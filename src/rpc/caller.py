import os
import requests
from dotenv import load_dotenv
from enums import RPCNames
from utils.handle_rpc import handle_response

load_dotenv()

ip = os.getenv("IP")
port = os.getenv("PORT")
nakama_host = f"http://{ip}:{port}"
endpoint = "?http_key=defaulthttpkey&unwrap=true"

def call_rpc(rpc_name: RPCNames, payload: dict):
    if rpc_name == RPCNames.RpcNames.Empty:
        return
    
    try:
        url = f"{nakama_host}/v2/rpc/{rpc_name}{endpoint}"
        print(f"Calling RPC: {rpc_name} with payload: {payload} at {url}")
        response = requests.post(url, json=payload)
        response.raise_for_status()
        data = response.json()
        handle_response(data, rpc_name)
    except Exception as e:
        print(f"RPC Error: {e}")
