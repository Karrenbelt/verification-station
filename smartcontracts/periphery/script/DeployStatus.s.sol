// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import {Script} from "forge-std/Script.sol";

import {Status} from "../src/Status.sol";

contract Deploy is Script {
    function deploy() public returns (address statusAddress) {
        vm.startBroadcast();
        Status status = new Status();
        vm.stopBroadcast();

        return address(status);
    }

    function run() external returns (address statusAddress) {
        return deploy();
    }
}
