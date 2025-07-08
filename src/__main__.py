import utils.app as app


"""
ip = os.getenv("IP", "84.21.171.226:7362")
nakama_host = f"http://{ip}"
endpoint = "?http_key=defaulthttpkey&unwrap=true"

def call_rpc(rpc_name: RpcNames, payload):
    try:
        response = requests.post(
            f"{nakama_host}/v2/rpc/{rpc_name}{endpoint}",
            json=payload,
        )
        response.raise_for_status()
        data = response.json()
    except:
        pass
"""

def main():
    app.init_app()

if __name__ == "__main__":
    main()