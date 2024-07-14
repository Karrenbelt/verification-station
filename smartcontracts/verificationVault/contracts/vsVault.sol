// SPDX-License-Identifier: MIT

pragma solidity ^0.8.20;

import "./ERC4626Fees.sol";

contract vsVault is ERC4626Fees  {
    address payable public vaultOwner;
    uint256 public entryFeeBasisPoints;

    //! Hardcoded operator address
    address constant operatorAddress = 0x5B38Da6a701c568545dCfcB03FcB875f56beddC4;

    modifier onlyNOperator() {
        require(msg.sender == operatorAddress, "Caller is not the Node Operator");
        _;
    }


    event NodeShares(
        uint256 nShares
    );

    uint256 public nodeShares;

    // constructor(IERC20 _asset, uint256 _basisPoints) ERC4626(_asset) ERC20("Verification Station ETH", "vsETH"){
    constructor(address _asset, uint256 _basisPoints) ERC4626(IERC20(_asset)) ERC20("Verification Station ETH", "vsETH"){
        vaultOwner = payable(msg.sender);
        entryFeeBasisPoints = _basisPoints;
        nodeShares = 0; 
    }

    /** @dev See {IERC4626-deposit}. */
    function deposit(uint256 assets, address receiver) public virtual override returns (uint256) {
        require(assets <= maxDeposit(receiver), "ERC4626: deposit more than max");

        uint256 shares = previewDeposit(assets);
        nodeShares += calculateXPercent(shares);
        _deposit(_msgSender(), receiver, assets, shares);
        afterDeposit(assets, shares);

        return shares;
    }

    /** @dev See {IERC4626-mint}.
     *
     * As opposed to {deposit}, minting is allowed even if the vault is in a state where the price of a share is zero.
     * In this case, the shares will be minted without requiring any assets to be deposited.
     */
    function mint(uint256 shares, address receiver) public virtual override returns (uint256) {
        require(shares <= maxMint(receiver), "ERC4626: mint more than max");

        uint256 assets = previewMint(shares);
        _deposit(_msgSender(), receiver, assets, shares);
        afterDeposit(assets, shares);

        return assets;
    }

    /** @dev See {IERC4626-redeem}. */
    function redeem(uint256 shares, address receiver, address owner) public virtual override returns (uint256) {
        require(shares <= maxRedeem(owner), "ERC4626: redeem more than max");

        uint256 assets = previewRedeem(shares);
        nodeShares -= calculateXPercent(shares);
        beforeWithdraw(assets, shares);
        _withdraw(_msgSender(), receiver, owner, assets, shares);

        return assets;
    }

    /** @dev See {IERC4626-withdraw}. */
    function withdraw(uint256 assets, address receiver, address owner) public virtual override returns (uint256) {
        require(assets <= maxWithdraw(owner), "ERC4626: withdraw more than max");

        uint256 shares = previewWithdraw(assets);
        beforeWithdraw(assets, shares);
        _withdraw(_msgSender(), receiver, owner, assets, shares);

        return shares;
    }

    function _entryFeeBasisPoints() internal view override returns (uint256) {
        return entryFeeBasisPoints;
    }

    function _entryFeeRecipient() internal view override returns (address) {
        return vaultOwner;
    }


    /*//////////////////////////////////////////////////////////////
                          NODE FEE CLAIM LOGIC
    //////////////////////////////////////////////////////////////*/

    function payOperators() public onlyNOperator{
        require(nodeShares > 0, "No shares to pay operators");

        uint256 assets = previewRedeem(nodeShares);
        beforeWithdraw(assets, nodeShares);
        _withdraw(_msgSender(), vaultOwner, vaultOwner, assets, nodeShares);
        emit NodeShares(nodeShares);
        nodeShares = 0;
        require(nodeShares != 0, "NodeShares not paid");
    }

    function getNodeShares() public view returns (uint256) {
        return nodeShares;
    }


    function calculateXPercent(uint256 value) public pure returns (uint256) {
        uint256 result = value * 10 / 100;
        return result;
    }
    /*//////////////////////////////////////////////////////////////
                          INTERNAL HOOKS LOGIC
    //////////////////////////////////////////////////////////////*/

    function afterDeposit(uint256 assets, uint256 shares) internal virtual {}
    
    function beforeWithdraw(uint256 assets, uint256 shares) internal virtual {}
}
