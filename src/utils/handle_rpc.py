from enums.RPCNames import RpcNames as RPC
from rpc.get_error_logs.handle_get_error_log import handle_get_error_log

def handle_response(data, rpc_name: RPC):
    print(f"Response for RPC {rpc_name}: {data}")
    match rpc_name:
        case RPC.GetErrorLogs:
            handle_get_error_log(data)
        case RPC.GetAccountInfo:
            pass
        case _:
            pass