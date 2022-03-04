from scripts.hepful_scripts import get_account
from brownie import interface, config, network


def get_weth():
    # Mint WETH  by depositing ETH

    # ABI
    # ADDRESS
    account = get_account()
    weth = interface.IWeth(
        config["networks"][network.show_active()]["weth_token"])
    tx = weth.deposit({"from": account, "value": 0.001 * 10 ** 18})
    tx.wait(1)
    print("Recieved 0.1 WETH")


def main():
    get_weth()
