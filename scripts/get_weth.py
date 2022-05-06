from brownie import accounts, config, network, interface


def main():
    """
    Runs the get_weth function to get WETH
    """
    get_weth()


def get_weth(account):
    print("Getting Weth...")
    # ABI + Address
    weth = interface.IWeth("0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2")
    tx = weth.deposit({"from": account, "value": 0.1 * 1e18})
    tx.wait(1)
    print("Received 0.1 WETH")
    return tx
    

# AUTOMATE NETWORK CONNECTION
# def get_weth(account=None):
#     """
#     Mints WETH by depositing ETH
#     """
#     accounts = (
#         account if account else accounts.add(config["wallets"]["from_key"])
#     ) # keystore ID as arg to call
#     weth = interface.WethInterface(
#         config["networks"][network.show_active()]["weth_token"]
#     )
#     tx = weth.deposit({"from": account, "value": 0.1 * 1e18})
#     print("Received 0.1 WETH")
#     return tx