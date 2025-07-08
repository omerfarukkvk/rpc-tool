import tkinter as tk
from tkinter import ttk
from enums import RPCNames

combo = None
window = None

def on_send_rpc_button_select(event):
    selected_value = combo.get()
    window.title(f"Selected RPC: {selected_value}")
    print(f"Seçilen RPC: {selected_value}")

def on_dropdown_select(event):
    selected_value = combo.get()
    window.title(f"Selected RPC: {selected_value}")
    print(f"Seçilen RPC: {selected_value}")

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
