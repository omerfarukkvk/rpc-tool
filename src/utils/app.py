import os
import tkinter as tk
from tkinter import ttk
from dotenv import load_dotenv
import os

import requests
from enums import RPCNames
from utils.handle_rpc import handle_response

combo = None
window = None
load_dotenv() # Load environment variables from .env file
ip = os.getenv("IP")
nakama_host = f"http://{ip}"
endpoint = "?http_key=defaulthttpkey&unwrap=true"

def call_rpc(rpc_name: RPCNames, payload):
    if rpc_name == RPCNames.RpcNames.Empty:
        return
    
    try:
        url = f"{nakama_host}/v2/rpc/{rpc_name}{endpoint}"
        print(f"Calling RPC: {rpc_name} with payload: {payload} at {url}")
        response = requests.post(url, json=payload)
        response.raise_for_status()
        data = response.json()
        handle_response(data)
    except:
        pass

def on_send_rpc_button_select():
    selected_value = combo.get()
    call_rpc(RPCNames.RpcNames[selected_value].value, {})
    print(f"Call RPC: {selected_value}")

def on_dropdown_select(event):
    selected_value = combo.get()
    window.title(f"Selected RPC: {selected_value}")
    print(f"Selected RPC: {selected_value}")

def set_rpc_names(root):
    global combo
    rpc_names = RPCNames.RpcNames.__members__.values()
    combo_values = [rpc.name for rpc in rpc_names]

    # Create a ComboBox with the enum values
    frame = tk.Frame(root)
    frame.pack(pady=10)

    label = tk.Label(frame, text="Select RPC:")
    label.pack(side="left", padx=(0, 5))

    combo = ttk.Combobox(frame, values=combo_values, state="readonly")
    combo.set(combo_values[0])
    combo.pack(side="left")

    button = tk.Button(frame, text="Send Rpc", command=on_send_rpc_button_select)
    button.pack(side="left", padx=(10, 0))  # Combo'nun sağına biraz boşluk

    # Bind the selection event to the on_dropdown_select function
    combo.bind("<<ComboboxSelected>>", on_dropdown_select)

def init_app():
    global window
    window = tk.Tk()
    window.title("Rpc Tool")
    window.geometry("800x400")
    window.minsize(800, 400)
    window.resizable(True, True)
    window.iconphoto(False, tk.PhotoImage(file="./assets/icon.png"))

    # Enum'dan ComboBox'u GUI'ye koy
    set_rpc_names(window)

    window.mainloop()
