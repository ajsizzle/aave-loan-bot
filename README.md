# Aave Borrow Bot 🤖
#### After completing this guide, you will have a general understanding of lending/borrowing and how to automate it.
###### 25 minute read 📖

-------
### Aave Lending and Borrowing 101
[Aave](https://aave.com/) is an open-source, decentralized liquidity protocol. It allows users to lend and borrow assets and earn interest on them. Aave is consistently one of the largest DeFi(Decentralized Finance) protocols by total volume locked (TVL). 

Now why would you want to borrow? Why not stick to selling?

Selling assets closes your position on that particular asset. This poses a conflict if you are long on that asset. You would be exiting your position much sooner forfeiting the upside potential value gain. Borrowing allows you to obtain liquidity (working capital) without needing to sell your assets.

Let's say you have 1 ETH and you want to buy MANA. 

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

## Step 1: Download Python

* The first step is to set this project up to handle a Python-based project. You can download Python [here](https://www.python.org/downloads/).
* Once you have downloaded Python, make sure to check if its properly installed by running this command in your terminal:
```
Python -V
```
You should get back something like:
```
Python 3.8.9
```

❗Note - You'll need to **install** `pipx` if this is your first time using Python. `pipx` is the `npm` of Python.

To install ```pipx```:
```
python3 -m pip install --user pipx
python3 -m pipx ensurepath
``` 

❗Note - You may need to **restart** your terminal after installing `pipx`

## Step 2: Download Brownie

*  [Brownie](https://eth-brownie.readthedocs.io/en/stable/toctree.html) is a Python-based development and testing framework for smart contracts. It specializes in utilizing the [Ethereum Virtual Machine](https://eth-brownie.readthedocs.io/en/stable/toctree.html)

*  Run this command in your terminal to install Brownie:
```
pipx install eth-brownie
```
* You can check the download was successful with this command:
```
brownie --version
```
You should see a response like
```
Brownie v1.17.1 - Python development framework for Ethereum
```

## Step 3: Create the project folder

* Navigate to the location where you want to store the project.
* Next we will initiate Brownie with the following command:
```
brownie init
```
* You should see your project folder generate new folders:

<img width="170" alt="Brownie Folder Layout" src="https://user-images.githubusercontent.com/17716182/171686945-cee24eaf-2c9a-46d9-aba1-c619da31a357.png">

## Step 4: Create the main script

1. In your scripts folder, create a new `.py` file. This will be the main script that runs your program.
2. Define your main function and test it out with a simple print statement:
```python
def main():
	print("Hello!")
```
* You should see your statement printed out in the console.
* You made it through the dreaded local environment setup! Congrats! 🎉 

## Step 5: Define your account & ERC Token to deposit

1. We need an account to deposit and withdraw funds from. This will be the account that will call the functions from the protocol.
```python
account = account[0]
```
2. Next we will need an ERC Token Address to deposit funds into.  In this example, we will use the WETH contract address.
```python
 erc20_address = "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"
```
❗Note - You will need ETH to pay for gas fees. You can obtain ETH from the Rinkeby Testnet Faucet [here.](https://rinkebyfaucet.com/)

## Step 6: Get WETH

1. We need our program to obtain WETH to use for borrowing. For this we will need another `.py` file in our scripts folder. For this example we will name it `get_weth.py`.

	❗Note - If you run into an issue with running your **main** script, you may need to add this additional file in your scripts folder to direct Python to handle multiple packages:
```
__init__.py
```

* In order to call the WETH contract, we need the **contract address** and the [**ABI**](https://www.quicknode.com/guides/solidity/what-is-an-abi). The quickest way is to compile the interface of the WETH contract and extracting the ABI from the build folder. The WETH interface can be found below:
```solidity
pragma solidity ^0.4.19;

interface IWeth {
  function allowance(address owner, address spender) external view returns (uint256 remaining);
  function approve(address spender, uint256 value) external returns (bool success);
  function balanceOf(address owner) external view returns (uint256 balance);
  function decimals() external view returns (uint8 decimalPlaces);
  function name() external view returns (string memory tokenName);
  function symbol() external view returns (string memory tokenSymbol);
  function totalSupply() external view returns (uint256 totalTokensIssued);
  function transfer(address to, uint256 value) external returns (bool success);
  function transferFrom(address from, address to, uint256 value) external returns (bool success);
  function deposit() external;
  function withdraw(uint wad) external;
}
```

* Once added to your **interfaces** folder, run the following command in the terminal:
```
brownie compile
```
* This command will compile the interface and allow it to be imported to our `get_weth.py`.

2. Now we can set a variable to the IWETH interface and pass in the token address of WETH:
```python
weth = interface.IWeth("0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2")
```

3. Next, we need to define a transaction variable to handle the deposit of WETH. Then we can add our `main()` to finish off our file:
```python
from brownie import interface


def main():
    """
    Runs the get_weth function to get WETH
    """
    get_weth()


def get_weth(account):
    print("Getting WETH...")
    weth = interface.IWeth("0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2")
    tx = weth.deposit({"from": account, "value": 0.1 * 1e18})
    tx.wait(1)
    print("Received 0.1 WETH")
    return tx
```

4. Lastly we import the `get_weth.py` file into our main script file:
```python
From scripts.get_weth import get_weth
```


