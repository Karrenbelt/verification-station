// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Status {
    event VERIFIED(bytes32 txHash);

    function triggerSuccess(bytes32 _txHash) public {
        emit VERIFIED(_txHash);
    }
}
