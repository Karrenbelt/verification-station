// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import {ERC20} from "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract BridgedToken is ERC20 {
    constructor()
        ERC20('Bridged Token', 'BT')
    {}

    function mint(address _to, uint256 _amount) public virtual {
        _mint(_to, _amount);
    }

    function burn(address from, uint256 _amount) public virtual {
        _burn(from, _amount);
    }
}
