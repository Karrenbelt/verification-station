// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import {Test, console} from "forge-std/Test.sol";

import {Status} from "../src/Status.sol";

contract StatusTest is Test {
    Status public status;

    address public OWNER = address(0x789);
    address public USER = makeAddr("user");
    address public ATTACKER = makeAddr("attacker");

    event Verified(bytes32 txHash);

    function setUp() public {
        status = new Status(OWNER);
    }

    /**
     * constructor
     */
    function test_constructor_OwnerCannotBeZeroAddress() public {
        vm.expectRevert();
        Status newStatus = new Status(address(0));
    }

    function test_constructor_OwnerIsCorrect() public view {
        assertEq(status.owner(), OWNER);
    }

    /**
     * triggerVerified
     */
    function test_triggerVerified_RevertIfUserIsNotOwner() public {
        bytes32 txHash = keccak256("txHash");

        vm.expectRevert();
        status.triggerVerified(txHash);
    }

    function test_triggerVerified_Success() public {
        bytes32 txHash = keccak256("txHash");

        vm.prank(OWNER);
        vm.expectEmit(false, false, false, true, address(status));
        emit Verified(txHash);

        status.triggerVerified(txHash);
    }
}
