// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import {Script} from "forge-std/Script.sol";

import {FlareStaking} from "../src/FlareStaking.sol";
import {BridgedToken} from "../src/BridgedToken.sol";

contract Deploy is Script {

    function deploy(address _account) public returns (address bridgedTokenAddress, address stakingAddress) {
        vm.startBroadcast();
        BridgedToken bridgedToken = new BridgedToken();
        bridgedToken.mint(_account, 100 ether);
        FlareStaking staking = new FlareStaking(address(bridgedToken));
        vm.stopBroadcast();

        return (address(bridgedToken), address(staking));
    }

    function run() external returns (address bridgedToken, address staking) {
        try vm.envAddress("ACCOUNT") returns (address account) {
            return deploy(account);
        } catch {
            revert(
                "Please sent ACCOUNT along with the script command:\n    make deploy ACCOUNT='0x...'"
            );
        }
    }
}