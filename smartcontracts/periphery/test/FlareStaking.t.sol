// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import {Test, console} from "forge-std/Test.sol";

import {FlareStaking} from "../src/FlareStaking.sol";
import {BridgedToken} from "../src/BridgedToken.sol";

contract FlareStakingTest is Test {
    BridgedToken bridgedToken = new BridgedToken();
    FlareStaking public staking;

    address public OWNER = msg.sender;
    address public USER = makeAddr("user");
    address public ATTACKER = makeAddr("attacker");

    function setup() public {
        staking = new FlareStaking(address(bridgedToken));

        bridgedToken.mint(address(USER), 100 ether);
    }

    function test_setup() public view {
        assertEq(bridgedToken.totalSupply(), 100);
    }
}