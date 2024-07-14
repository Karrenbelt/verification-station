// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import {Script} from "forge-std/Script.sol";

import {Status} from "../src/Status.sol";

contract Deploy is Script {
    function deploy(address _owner) public returns (address statusAddress) {
        vm.startBroadcast();
        Status status = new Status(_owner);
        vm.stopBroadcast();

        return address(status);
    }

    function run() external returns (address statusAddress) {
        try vm.envAddress("OWNER") returns (address owner) {
            return deploy(owner);
        } catch {
            revert(
                "Please sent OWNER along with the script command:\n    make deployStatus ARGS='...' OWNER='0x...'"
            );
        }
    }
}
