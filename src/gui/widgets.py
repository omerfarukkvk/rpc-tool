import tkinter as tk
from tkinter import ttk
from enums import RPCNames
from rpc.caller import call_rpc

combo = None
window = None

def on_send_rpc_button_select():
    selected_value = combo.get()
    call_rpc(RPCNames.RpcNames[selected_value].value, {})
    print(f"Call RPC: {selected_value}")

def on_dropdown_select(event):
    selected_value = combo.get()
    window.title(f"Selected RPC: {selected_value}")
    print(f"Selected RPC: {selected_value}")

def set_rpc_names(root):
    global combo, window
    window = root
    rpc_names = RPCNames.RpcNames.__members__.values()
    combo_values = [rpc.name for rpc in rpc_names]

    frame = tk.Frame(root)
    frame.pack(pady=10)

    label = tk.Label(frame, text="Select RPC:")
    label.pack(side="left", padx=(0, 5))

    combo = ttk.Combobox(frame, values=combo_values, state="readonly")
    combo.set(combo_values[0])
    combo.pack(side="left")

    button = tk.Button(frame, text="Send Rpc", command=on_send_rpc_button_select)
    button.pack(side="left", padx=(10, 0))

    combo.bind("<<ComboboxSelected>>", on_dropdown_select)
