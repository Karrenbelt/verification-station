// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import {Ownable} from "@openzeppelin/contracts/access/Ownable.sol";

contract Status is Ownable{
    event Verified(bytes32 txHash);

    constructor(address _owner) Ownable(_owner) {}

    function triggerVerified(bytes32 _txHash) public onlyOwner{
        emit Verified(_txHash);
    }
}
