// SPDX-LICENSE-Identifier: MIT
// inspired by https://solidity-by-example.org/defi/staking-rewards

pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import {ERC20} from "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import {Ownable} from "@openzeppelin/contracts/access/Ownable.sol";

import {IFlareContractRegistry} from "@flarenetwork/flare-periphery-contracts/coston2/util-contracts/userInterfaces/IFlareContractRegistry.sol";
import {IFastUpdater} from "@flarenetwork/flare-periphery-contracts/coston2/ftso/userInterfaces/IFastUpdater.sol";

contract FlareStaking is Ownable, ERC20 {
    IERC20 public immutable stakingToken;

    IFlareContractRegistry internal flareContractRegistry;
    IFastUpdater internal ftsoV2;
    uint256[] public priceFeedIndexes = [0];

    // Total staked
    uint256 public totalStaked;
    // User address => staked amount
    mapping(address => uint256) public stakedAmount;
    // User address => last staked time
    mapping(address => uint256) public lastStakedTime;
    // Reward rate (tokens per second)
    uint256 public rewardRate = 1;
        // Total rewards earned
    uint256 public totalRewardsEarned;

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 amount);

    constructor(
        address _bridgedToken
    ) Ownable(msg.sender) ERC20("Flare Staking Token", "FLRSTK") {
        stakingToken = IERC20(_bridgedToken);

        flareContractRegistry = IFlareContractRegistry(
            0xaD67FE66660Fb8dFE9d6b1b4240d8650e30F6019
        );
        ftsoV2 = IFastUpdater(
            flareContractRegistry.getContractAddressByName("FastUpdater")
        );
    }

    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake 0");

        stakingToken.transferFrom(msg.sender, address(this), _amount);

        stakedAmount[msg.sender] += _amount;
        totalStaked += _amount;

        if(lastStakedTime[msg.sender] == 0) {
            lastStakedTime[msg.sender] = block.timestamp;
        }
        else {
            _updateReward(msg.sender);
        }

        emit Staked(msg.sender, _amount);
    }

    function unstake(uint256 _amount) external {
        require(_amount > 0, "Cannot unstake 0");
        require(stakedAmount[msg.sender] >= _amount, "Insufficient balance");

        _updateReward(msg.sender);

        stakedAmount[msg.sender] -= _amount;
        totalStaked -= _amount;

        if (stakedAmount[msg.sender] == 0) {
            lastStakedTime[msg.sender] = 0;
        }

        stakingToken.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    function claimReward() external {
        _updateReward(msg.sender);

        uint256 reward = _earned(msg.sender);
        if (reward > 0) {
            _mint(msg.sender, reward);
            totalRewardsEarned += reward;
            emit RewardPaid(msg.sender, reward);
        }
    }

    function _updateReward(address _user) internal {
        if (stakedAmount[_user] > 0) {
            uint256 reward = _earned(_user);
            _mint(_user, reward);
            totalRewardsEarned += reward;
            lastStakedTime[_user] = block.timestamp;
        }
    }

    function _earned(address _user) internal view returns (uint256) {
        if (lastStakedTime[_user] == 0) {
            return 0;
        }

        uint256 userStakedTime = block.timestamp - lastStakedTime[_user];
        uint256 userStakedAmount = stakedAmount[_user];

        return userStakedTime * userStakedAmount * rewardRate;
    }

    function getTotalStakingReward() external view returns (uint256) {
        (
            uint256[] memory feedValues,
            int8[] memory decimals,
        ) = ftsoV2.fetchCurrentFeeds(priceFeedIndexes);

        uint256 rewardTokenPrice = feedValues[0];

        uint256 rewardTokenPriceAdjusted = rewardTokenPrice * (10 ** uint256(uint8(decimals[0])));

        return totalRewardsEarned * rewardTokenPriceAdjusted;
    }
}
