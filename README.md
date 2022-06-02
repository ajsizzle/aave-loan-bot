# Your Personal Aave Borrow Bot 🤖
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


