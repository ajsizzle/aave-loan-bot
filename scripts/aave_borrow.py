from brownie import accounts, config, interface, network
from web3 import Web3
from scripts.get_weth import get_weth


def main():
    # Deposit Money
    #* The Account that is going to call the function
    account = accounts[0]
    erc20_address = "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"
    #* Approve WETH to be deposited to Aave
    print("Getting WETH")
    get_weth(account)
    lending_pool = get_lending_pool()
    amount = Web3.toWei(0.1, "ether")
    approve_erc20(amount, lending_pool.address, erc20_address, account)
    print("Deposit...")
    tx = lending_pool.deposit(erc20_address, amount, account.address, 0, {"from": account})
    tx.wait(1)
    print("Deposit Successful.")
    avail_to_borrow = get_borrowable_data(lending_pool, account)
    #* borrowing 
    dai_to_borrow = Web3.toWei(200, "ether")
    dai_address = "0x6B175474E89094C44Da98b954EedeAC495271d0F"
    lending_pool.borrow(dai_address, dai_to_borrow, 1, 0, account.address, {"from": account})
    tx.wait(1)
    print("LFG!!!")
    avail_to_borrow = get_borrowable_data(lending_pool, account)
    #* Repaying
    approve_erc20(dai_to_borrow, lending_pool.address, dai_address, account)
    tx = lending_pool.repay(dai_address, dai_to_borrow, 1, account.address, {"from": account})
    tx.wait(1)
    get_borrowable_data(lending_pool, account)



def get_lending_pool():
    lending_pool_address_provider_address = "0xB53C1a33016B2DC2fF3653530bfF1848a515c8c5"
    lending_pool_address_provider = interface.ILendingPoolAddressesProvider(
        lending_pool_address_provider_address
    )
    lending_pool_address = lending_pool_address_provider.getLendingPool()
    lending_pool = interface.ILendingPool(lending_pool_address)
    return lending_pool
    
def approve_erc20(amount, lending_pool_address, erc20_address, account):
    print("Approving ERC20...")
    erc20 = interface.IERC20(erc20_address)
    tx = erc20.approve(lending_pool_address, amount, {"from": account})
    tx.wait(1)
    print("Approved.")
    


def get_borrowable_data(lending_pool, account):
    (
        total_collateral_eth,
        total_debt_eth,
        available_borrow_eth,
        current_liquidation_threshold,
        tlv,
        health_factor,
    ) = lending_pool.getUserAccountData(account.address)
    available_borrow_eth = Web3.fromWei(available_borrow_eth, "ether")
    total_collateral_eth = Web3.fromWei(total_collateral_eth, "ether")
    total_debt_eth = Web3.fromWei(total_debt_eth, "ether")
    print(f"You have {total_collateral_eth} worth of ETH deposited.")
    print(f"You have {total_debt_eth} worth of ETH borrowed.")
    print(f"You can borrow {available_borrow_eth} worth of ETH.")
    return (float(available_borrow_eth), float(total_debt_eth))

