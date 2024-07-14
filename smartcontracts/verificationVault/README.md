
# Sample Hardhat Project

This project demonstrates a basic Hardhat use case. It comes with a sample contract, a test for that contract, and a Hardhat Ignition module that deploys that contract.

Try running some of the following tasks:

```shell
npx hardhat help
npx hardhat test
REPORT_GAS=true npx hardhat test
npx hardhat node
npx hardhat ignition deploy ./ignition/modules/Lock.ts
```


`npm install`

1. Deploy vUSDC Contract

2. Copy vUSDC Contract Address

3. Mint 10'000 vUSDC to main address

4. Approve to spend minted vUSDC
    - spender and amount in "xxx" (quotation marks).


5. Deploy vsVault.sol with 
    - vUSDC Contract address
    - VaultUSDC as Name
    - vUSDC as Symbol 

6. @Vault: 
    - `_deposit` the amount that should be deposited into the vault
